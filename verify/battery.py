#!/usr/bin/env python3
"""Bateria de comprobacion de KAVANA Agent Lite.

Comprueba el estado real del repositorio, no su intencion: que la puerta exista y
funcione, que el manifiesto quepa en una pantalla, que las skills sigan la
plantilla y que lo que el README promete exista de verdad.

Uso:
    python3 verify/battery.py
    python3 verify/battery.py --json
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent

SECCIONES = [
    "## Cuando se usa",
    "## Que resuelve",
    "## Procedimiento",
    "## Errores que evita",
    "## Como se comprueba",
]
SECCIONES = [s.replace("Cuando", "Cu" + chr(225) + "ndo").replace("Que", "Qu" + chr(233))
              .replace("Como", "C" + chr(243) + "mo") for s in SECCIONES]

LICENCIAS = re.compile(r"\b(MIT|Apache|GPL|BSD)\b", re.IGNORECASE)

resultados = []


def check(codigo, nombre, ok, detalle):
    resultados.append({"codigo": codigo, "nombre": nombre, "ok": bool(ok), "detalle": detalle})


def run(args):
    p = subprocess.run(args, cwd=REPO, capture_output=True, text=True)
    return p.returncode, (p.stdout + p.stderr).strip()


def leer(rel):
    p = REPO / rel
    return p.read_text(encoding="utf-8") if p.exists() else ""


# B01 el manifiesto cabe en una pantalla
lineas = [l for l in leer("README.md").splitlines() if l.strip()]
check("B01", "El manifiesto cabe en una pantalla", bool(lineas) and len(lineas) <= 30,
      str(len(lineas)) + " lineas no vacias (limite 30)")

# B02 la puerta esta completa
piezas = ["guard/scan.py", "guard/reglas.md", "guard/pre-commit", "guard/patterns.example.txt"]
faltan = [p for p in piezas if not (REPO / p).exists()]
check("B02", "La puerta esta completa", not faltan,
      "faltan: " + ", ".join(faltan) if faltan else "4 piezas presentes")

# B03 la prueba negativa pasa
code, out = run([sys.executable, "guard/scan.py", "--self-test"])
check("B03", "La prueba negativa de la puerta pasa", code == 0,
      out.splitlines()[-1] if out else "sin salida")

# B04 el repositorio pasa su propia puerta
code, out = run([sys.executable, "guard/scan.py"])
check("B04", "El repositorio pasa su propia puerta", code == 0,
      out.splitlines()[-1] if out else "sin salida")

# B05 gancho valido y listas locales fuera del control de versiones
code, _ = run(["bash", "-n", "guard/pre-commit"])
gi = leer(".gitignore")
ignoradas = all(x in gi for x in ["guard/patterns.local.txt", "guard/allow.local.txt"])
check("B05", "El gancho es valido y las listas locales no se publican",
      code == 0 and ignoradas,
      "sintaxis=" + ("ok" if code == 0 else "error") + ", listas ignoradas=" + str(ignoradas))

# B06 las skills siguen la plantilla
skills = sorted((REPO / "craft").glob("*/SKILL.md"))
malas = []
for s in skills:
    txt = s.read_text(encoding="utf-8")
    falta = [sec for sec in SECCIONES if sec not in txt]
    if falta:
        malas.append(s.parent.name + " (falta " + ", ".join(f.replace("## ", "") for f in falta) + ")")
check("B06", "Todas las skills siguen la plantilla", bool(skills) and not malas,
      str(len(skills)) + " skills" + (", fuera de plantilla: " + "; ".join(malas) if malas else ""))

# B07 lo que el README promete existe
promesas = ["install.sh", "verify/battery.py"]
ausentes = [p for p in promesas if not (REPO / p).exists()]
check("B07", "Los comandos del README existen", not ausentes,
      "faltan: " + ", ".join(ausentes) if ausentes else "2 comandos verificados")

# B08 si se cita una licencia, el fichero existe
readme = leer("README.md")
cita = LICENCIAS.search(readme)
hay_licencia = (REPO / "LICENSE").exists()
check("B08", "La licencia citada existe como fichero",
      (cita is None) or hay_licencia,
      ("cita " + cita.group(0) + ", fichero " + ("presente" if hay_licencia else "AUSENTE"))
      if cita else "ninguna licencia concreta citada (pendiente): correcto")

# B09 el roadmap interno no esta en el repositorio
intrusos = [str(p.relative_to(REPO)) for p in REPO.rglob("kavanaagent*")
            if ".git" not in p.parts]
check("B09", "El roadmap interno no esta en el repositorio", not intrusos,
      "encontrado: " + ", ".join(intrusos) if intrusos else "ninguna copia interna")

# B10 la raiz contiene solo lo esperado
esperado = {".gitignore", "README.md", "install.sh", "soul", "craft", "guard", "verify", "docs", "LICENSE"}
raiz = {p.name for p in REPO.iterdir() if p.name != ".git"}
sobran = sorted(raiz - esperado)
check("B10", "La raiz contiene solo lo esperado", not sobran,
      "sobran: " + ", ".join(sobran) if sobran else "estructura limpia")


def main():
    parser = argparse.ArgumentParser(description="Bateria de comprobacion")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    fallos = [r for r in resultados if not r["ok"]]
    if args.json:
        print(json.dumps({"resultados": resultados, "fallos": len(fallos)}, ensure_ascii=False, indent=2))
    else:
        print("Bateria KAVANA Agent Lite: " + str(len(resultados) - len(fallos)) + "/" + str(len(resultados)) + " OK")
        for r in resultados:
            marca = "OK  " if r["ok"] else "FALLO"
            print("  [" + marca + "] " + r["codigo"] + "  " + r["nombre"] + ": " + r["detalle"])
    return 1 if fallos else 0


if __name__ == "__main__":
    sys.exit(main())
