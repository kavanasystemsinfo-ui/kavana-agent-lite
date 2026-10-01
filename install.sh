#!/usr/bin/env bash
# Instala KAVANA Agent Lite en una herramienta de agentes.
#
#   ./install.sh --tool claude              instala en la configuracion personal
#   ./install.sh --tool claude --gancho     instala y enciende la puerta
#   ./install.sh --tool opencode --project
#   ./install.sh --tool hermes --dry-run
#   ./install.sh --gancho                   solo enciende la puerta en el
#                                           repositorio git donde estes
#
# Soporta cuatro herramientas: claude, opencode, hermes y codex.
set -euo pipefail

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TOOL=""
MODE="global"
DRY=0
GANCHO=0

uso() {
  cat <<'FIN'
Uso: ./install.sh --tool <claude|opencode|hermes|codex> [--project] [--dry-run] [--gancho]
     ./install.sh --gancho

  --tool      herramienta destino
  --project   instala en el proyecto actual en vez de en la configuracion personal
  --dry-run   ensena lo que haria sin tocar nada
  --gancho    enciende la puerta (gancho de pre-commit) en el repositorio git
              donde estes. Con --tool hace las dos cosas.
FIN
}

while [ $# -gt 0 ]; do
  case "$1" in
    --tool) TOOL="${2:-}"; shift 2 ;;
    --project) MODE="project"; shift ;;
    --dry-run) DRY=1; shift ;;
    --gancho) GANCHO=1; shift ;;
    -h|--help) uso; exit 0 ;;
    *) echo "Opcion no reconocida: $1"; uso; exit 1 ;;
  esac
done

if [ -z "$TOOL" ] && [ "$GANCHO" != "1" ]; then uso; exit 1; fi

# La puerta. El escaner vive en este clon, asi que el gancho lo llama por ruta
# absoluta y sirve para cualquier repositorio, no solo para este.
instalar_gancho() {
  local repo_root hook
  if ! repo_root="$(git rev-parse --show-toplevel 2>/dev/null)"; then
    echo "La puerta necesita un repositorio git y aqui no lo hay."
    echo "Entra en el repositorio que quieras proteger y vuelve a ejecutarlo."
    return 1
  fi
  hook="$repo_root/.git/hooks/pre-commit"
  ajeno=0
  if [ -e "$hook" ] && ! grep -qE "KAVANA Agent Lite|guard/scan.py" "$hook" 2>/dev/null; then
    ajeno=1
  fi
  if [ "$DRY" = "1" ]; then
    echo "[dry-run] escribiria el gancho en $hook apuntando a $REPO_DIR/guard/scan.py"
    [ "$ajeno" = "1" ] && echo "[dry-run] ojo: ahi ya hay un gancho ajeno y no lo pisaria"
    return 0
  fi
  if [ "$ajeno" = "1" ]; then
    echo "Ya hay un gancho pre-commit en $repo_root y no es mio: no lo piso."
    echo "Guardalo o mezclalo a mano y despues vuelve a ejecutar esto."
    return 1
  fi
  cat > "$hook" <<FIN
#!/usr/bin/env bash
# KAVANA Agent Lite: puerta de pre-commit. Corta el commit si el escaner
# encuentra contaminacion (credenciales, claves, rutas personales, datos de
# personas, cifras de maquina o restos de saneado).
set -euo pipefail

ESCANER="$REPO_DIR/guard/scan.py"
PYTHON="\${PYTHON:-python3}"

if [ ! -f "\$ESCANER" ]; then
  echo "Aviso: no encuentro el escaner en \$ESCANER."
  echo "El commit pasa sin la puerta. Reinstalala desde el clon."
  exit 0
fi

if ! "\$PYTHON" "\$ESCANER" --staged; then
  echo ""
  echo "Commit cortado por la puerta."
  echo "Si un hallazgo es un falso positivo, declaralo en $REPO_DIR/guard/allow.local.txt (no se publica)."
  exit 1
fi
FIN
  chmod +x "$hook"
  echo "Puerta encendida: $hook"
  echo "Comprueba que corta de verdad: crea un fichero con una cadena que parezca"
  echo "un token, anadelo al indice (git add) y prueba a commitear. No debe pasar."
}

if [ "$GANCHO" = "1" ]; then
  instalar_gancho || { [ -z "$TOOL" ] && exit 1; }
  if [ -z "$TOOL" ]; then echo; exit 0; fi
  echo
fi

case "$TOOL" in
  claude)   CARPETA=".claude";  REGLAS="CLAUDE.md"; GLOBAL="$HOME/.claude" ;;
  opencode) CARPETA=".opencode"; REGLAS="AGENTS.md"; GLOBAL="${XDG_CONFIG_HOME:-$HOME/.config}/opencode" ;;
  hermes)   CARPETA=".hermes";  REGLAS="AGENTS.md"; GLOBAL="$HOME/.hermes" ;;
  codex)    CARPETA=".codex";   REGLAS="AGENTS.md"; GLOBAL="$HOME/.codex" ;;
  *) echo "Herramienta no soportada: $TOOL (usa claude, opencode, hermes o codex)"; exit 1 ;;
esac

if [ "$MODE" = "project" ]; then DESTINO="$PWD/$CARPETA"; else DESTINO="$GLOBAL"; fi

echo "Herramienta: $TOOL"
echo "Destino:     $DESTINO"
echo

if [ "$DRY" = "1" ]; then
  echo "[dry-run] crearia $DESTINO/skills/ con las skills de craft/"
  echo "[dry-run] escribiria $DESTINO/$REGLAS con la identidad y las reglas de soul/"
  echo "[dry-run] copiaria guard/ y verify/ en $DESTINO/kavana-agent-lite/"
  exit 0
fi

mkdir -p "$DESTINO/skills"

# Reglas: identidad + reglas de trabajo + despachador, en un solo fichero
{
  echo "# Reglas de trabajo"
  echo
  for f in "$REPO_DIR"/soul/*.md; do
    cat "$f"
    echo
    echo "---"
    echo
  done
} > "$DESTINO/$REGLAS"

# Skills
n_skills=0
for d in "$REPO_DIR"/craft/*/; do
  [ -d "$d" ] || continue
  nombre="$(basename "$d")"
  rm -rf "$DESTINO/skills/$nombre"
  cp -r "$d" "$DESTINO/skills/$nombre"
  n_skills=$((n_skills + 1))
done

# La puerta y la bateria, para que quien instale pueda comprobar por su cuenta
mkdir -p "$DESTINO/kavana-agent-lite"
cp -r "$REPO_DIR/guard" "$DESTINO/kavana-agent-lite/"
cp -r "$REPO_DIR/verify" "$DESTINO/kavana-agent-lite/"

echo "Instaladas $n_skills skills en $DESTINO/skills/"
echo "Reglas escritas en $DESTINO/$REGLAS"
echo
cat <<'FIN'
Este script no puede comprobar por ti que la herramienta las haya cargado.
Una instalacion no esta terminada hasta que compruebes tres cosas:

  1. IDENTIDAD   pregunta: "quien eres y como trabajas?"
     Esperado: responde con los tres estados (implementado, verificado, desplegado).
  2. LISTADO     pregunta: "que skills tienes disponibles?"
     Esperado: aparecen las de craft/ por su nombre.
  3. CARGA REAL  pide que lea una skill concreta y reproduzca su contenido.
     Un listado no es una carga.

Reinicia la herramienta antes de comprobar: la configuracion no se recarga en caliente.
FIN
