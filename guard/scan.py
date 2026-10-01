#!/usr/bin/env python3
"""Escaner de contaminacion de KAVANA Agent Lite.

Corre antes de cada commit y corta el paso si encuentra material que no debe
publicarse: credenciales, datos personales, rutas del equipo donde se desarrollo
el trabajo, cifras de una maquina concreta y restos de un saneado automatico de
nombres.

La lista de terminos propios (nombres de productos, de personas y de clientes) NO
vive en este repositorio. Se carga de guard/patterns.local.txt, que esta ignorado
por git: publicar esa lista seria publicar justo lo que protege.

Uso:
    python3 guard/scan.py                  escanea el repositorio
    python3 guard/scan.py --staged         solo lo que esta en el indice de git
    python3 guard/scan.py --audit RUTA     audita material externo
    python3 guard/scan.py --self-test      prueba negativa con casos sinteticos
    python3 guard/scan.py --json           salida legible por la bateria
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
PATTERNS_LOCAL = REPO / "guard" / "patterns.local.txt"
ALLOW_LOCAL = REPO / "guard" / "allow.local.txt"

SKIP_DIRS = {".git", "node_modules", "__pycache__", ".venv", "venv", "dist", "build"}
MAX_BYTES = 512 * 1024

BLOCK = "BLOCK"
REVIEW = "REVIEW"

# Las dos raices personales se construyen por partes a proposito: si aparecieran
# literales en este fichero, el escaner se delataria a si mismo.
RAIZ_ROOT = "/" + "root/"
RAIZ_HOME = "/" + "home/"

DETECTORS = [
    ("credencial", BLOCK, re.compile(
        r"\b(gh[pousr]_[A-Za-z0-9]{20,}"
        r"|github_pat_[A-Za-z0-9_]{20,}"
        r"|sk-(?:ant-|proj-|live-|test-|svcacct-)?[A-Za-z0-9_-]{20,}"
        r"|AIza[0-9A-Za-z_-]{30,}"
        r"|nvapi-[A-Za-z0-9_-]{20,}"
        r"|xox[baprs]-[A-Za-z0-9-]{10,}"
        r"|AKIA[0-9A-Z]{16}"
        r"|eyJ[A-Za-z0-9_-]{20,}\.[A-Za-z0-9_-]{10,})")),
    ("clave-privada", BLOCK, re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----")),
    ("ruta-personal", BLOCK, re.compile(
        "(" + re.escape(RAIZ_ROOT) + "|" + re.escape(RAIZ_HOME) + r"[A-Za-z0-9._-]+/)")),
    ("dato-personal", REVIEW, re.compile(r"\b[\w.+-]+@[\w-]+\.[A-Za-z]{2,}\b")),
    ("cifra-de-maquina", REVIEW, re.compile(
        r"(backups?[^\n]{0,40}\b[0-9]+\s*d[i]as"
        r"|[0-9]{1,3}\s?%\s*de\s+(memoria|RAM|disco)"
        r"|[0-9]+(?:[.,][0-9]+)?\s?(?:GB|MB|TB)\s+de\s+(memoria|RAM|disco))", re.IGNORECASE)),
    ("resto-de-saneado", REVIEW, re.compile(
        "(de el " + "usuario|el " + "usuario's|el " + "usuario(?=" + r"\s+(prefers|prefiere|says|dice|uses|wants|asked|trajo|suele|accede|OK)))")),
]


def local_terms():
    """Terminos propios, desde un fichero que no se publica."""
    if not PATTERNS_LOCAL.exists():
        return []
    out = []
    for line in PATTERNS_LOCAL.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line and not line.startswith("#"):
            out.append(line)
    return out


def allowed(path, detector):
    """Excepciones locales, tambien fuera del repositorio."""
    if not ALLOW_LOCAL.exists():
        return False
    for line in ALLOW_LOCAL.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        pat, _, only = line.partition(":")
        if not path.startswith(pat) and not Path(path).match(pat):
            continue
        if not only or only.strip() == detector:
            return True
    return False


def mask(value):
    value = value.strip()
    if len(value) <= 6:
        return value[0] + "***"
    return value[:4] + "..." + str(len(value)) + " caracteres"


def readable(path):
    try:
        if path.stat().st_size > MAX_BYTES:
            return False
        path.read_text(encoding="utf-8")
        return True
    except (UnicodeDecodeError, OSError):
        return False


def scan_file(path, terms, rel):
    findings = []
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return findings
    term_re = None
    if terms:
        term_re = re.compile("|".join(re.escape(t) for t in terms), re.IGNORECASE)
    for number, line in enumerate(text.splitlines(), 1):
        for name, severity, pattern in DETECTORS:
            for match in pattern.finditer(line):
                if allowed(rel, name):
                    continue
                findings.append({"detector": name, "severity": severity, "file": rel,
                                 "line": number, "snippet": mask(match.group(0))})
        if term_re and term_re.search(line):
            for match in term_re.finditer(line):
                if allowed(rel, "termino-propio"):
                    continue
                findings.append({"detector": "termino-propio", "severity": REVIEW, "file": rel,
                                 "line": number, "snippet": mask(match.group(0))})
    return findings


def collect(root):
    """Recorre un arbol externo (para --audit)."""
    out = []
    for path in sorted(root.rglob("*")):
        if not path.is_file() or (SKIP_DIRS & set(path.parts)) or not readable(path):
            continue
        out.append(str(path.relative_to(root)))
    return out


def tracked_files():
    """Ficheros que git publicaria. La puerta no juzga listas locales ni borradores."""
    try:
        out = subprocess.run(["git", "ls-files"], cwd=REPO,
                             capture_output=True, text=True, check=True).stdout
    except (subprocess.CalledProcessError, FileNotFoundError):
        return collect(REPO)
    return [l for l in out.splitlines() if l.strip() and readable(REPO / l)]


def raiz_del_directorio():
    """El repositorio git del directorio actual, que no es lo mismo que la carpeta
    del escaner. El gancho se ejecuta en el repositorio que se esta commiteando, y
    es ese indice el que hay que juzgar: mirar el del escaner deja pasar secretos
    en cualquier otro repositorio."""
    try:
        out = subprocess.run(["git", "rev-parse", "--show-toplevel"],
                             capture_output=True, text=True, check=True).stdout.strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        return None
    return Path(out) if out else None


def staged_files(raiz):
    try:
        out = subprocess.run(["git", "diff", "--cached", "--name-only", "--diff-filter=ACM"],
                             cwd=raiz, capture_output=True, text=True, check=True).stdout
    except (subprocess.CalledProcessError, FileNotFoundError):
        return []
    return [l for l in out.splitlines() if l.strip()]


def run(paths, root, terms):
    findings = []
    for rel in paths:
        path = root / rel
        if path.is_file():
            findings.extend(scan_file(path, terms, rel))
    return findings


def report(findings, as_json):
    if as_json:
        print(json.dumps({"findings": findings}, ensure_ascii=False, indent=2))
    else:
        if not findings:
            print("Puerta: limpio. 0 hallazgos.")
        for f in findings:
            print(f"{f['file']}:{f['line']}: [{f['severity']}] {f['detector']}: {f['snippet']}")
        if findings:
            blocks = sum(1 for f in findings if f["severity"] == BLOCK)
            print(f"Total: {len(findings)} hallazgos ({blocks} de bloqueo).")
    return 1 if findings else 0


# Los casos sinteticos de la prueba se construyen por fragmentos: si estuvieran
# escritos enteros, el escaner los cazaria en su propio fichero y la prueba
# seria imposible de mantener limpia.
def _sucio():
    tok = "gh" + "p_" + "A" * 36
    tok_proj = "sk-" + "proj-" + "B" * 32
    tok_live = "sk-" + "live-" + "C" * 32
    ruta = "/" + "ho" + "me/" + "analista" + "/proyectos/app/.env"
    cifra = str(94) + "% de " + "memoria"
    copia = "el backup tiene " + str(30) + " dias"
    sanea = "PC de " + "el " + "usuario, verificado ayer"
    correo = "soporte" + chr(64) + "ejemplo" + ".test"
    return chr(10).join([
        "# Notas internas de despliegue", "",
        "Token de acceso: " + tok, "Clave de proyecto: " + tok_proj,
        "Clave de servicio: " + tok_live, "Ruta del equipo: " + ruta,
        "El servicio aguanta con la " + cifra, copia,
        "Hardware del equipo (" + sanea + ")", "Contacto: " + correo, ""])


def _limpio():
    return chr(10).join([
        "# Notas de despliegue", "",
        "Antes de dar un despliegue por bueno, comprueba tres cosas: que la URL viva responde,",
        "que el commit desplegado coincide con el local y que un flujo real funciona desde fuera.", "",
        "Si una de las tres falla, el despliegue no esta hecho, por muy verde que este la interfaz.",
        "El prefijo sk- por si solo no es un secreto: sk-corto no debe contar como credencial.",
        ""])


def self_test():
    """Prueba negativa: casos sinteticos que el escaner debe cazar, y ruido cero."""
    expected = {"credencial", "ruta-personal", "dato-personal"}
    terms = ["producto-de-ejemplo-cliente-x"]
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        (root / "sucio.md").write_text(_sucio(), encoding="utf-8")
        (root / "limpio.md").write_text(_limpio(), encoding="utf-8")
        dirty = run(["sucio.md"], root, terms)
        clean = run(["limpio.md"], root, terms)
    found = {f["detector"] for f in dirty}
    ok = True
    missing = expected - found
    if missing:
        print("FALLO: el escaner no detecta " + str(sorted(missing)))
        ok = False
    if not any(f["severity"] == BLOCK for f in dirty):
        print("FALLO: ningun hallazgo de bloqueo en el caso sucio")
        ok = False
    if clean:
        print("FALLO: el caso limpio produce " + str(len(clean)) + " hallazgos")
        ok = False
    if ok:
        print("Prueba negativa OK: " + str(len(dirty)) + " hallazgos en el caso sucio ("
              + str(len(found)) + " detectores: " + ", ".join(sorted(found)) + "), 0 en el limpio.")
    return 0 if ok else 1


def main():
    parser = argparse.ArgumentParser(description="Escaner de contaminacion")
    parser.add_argument("--staged", action="store_true", help="solo el indice de git")
    parser.add_argument("--audit", metavar="RUTA", help="audita material externo")
    parser.add_argument("--self-test", action="store_true", help="prueba negativa")
    parser.add_argument("--json", action="store_true", help="salida en JSON")
    args = parser.parse_args()

    if args.self_test:
        return self_test()

    terms = local_terms()
    if args.audit:
        root = Path(args.audit).resolve()
        paths = collect(root)
    elif args.staged:
        raiz = raiz_del_directorio()
        if raiz is None:
            print("No hay repositorio git en el directorio actual: no hay indice que revisar.")
            return 0
        root, paths = raiz, staged_files(raiz)
    else:
        root, paths = REPO, tracked_files()
    return report(run(paths, root, terms), args.json)


if __name__ == "__main__":
    sys.exit(main())
