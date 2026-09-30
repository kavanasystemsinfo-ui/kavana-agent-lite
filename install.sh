#!/usr/bin/env bash
# Instala KAVANA Agent Lite en una herramienta de agentes.
#
#   ./install.sh --tool claude        instala en la configuracion personal
#   ./install.sh --tool opencode --project
#   ./install.sh --tool hermes --dry-run
#
# Soporta tres herramientas: claude, opencode y hermes.
set -euo pipefail

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TOOL=""
MODE="global"
DRY=0

uso() {
  cat <<'FIN'
Uso: ./install.sh --tool <claude|opencode|hermes> [--project] [--dry-run]

  --tool      herramienta destino (obligatorio)
  --project   instala en el proyecto actual en vez de en la configuracion personal
  --dry-run   ensena lo que haria sin tocar nada
FIN
}

while [ $# -gt 0 ]; do
  case "$1" in
    --tool) TOOL="${2:-}"; shift 2 ;;
    --project) MODE="project"; shift ;;
    --dry-run) DRY=1; shift ;;
    -h|--help) uso; exit 0 ;;
    *) echo "Opcion no reconocida: $1"; uso; exit 1 ;;
  esac
done

if [ -z "$TOOL" ]; then uso; exit 1; fi

case "$TOOL" in
  claude)   CARPETA=".claude";  REGLAS="CLAUDE.md"; GLOBAL="$HOME/.claude" ;;
  opencode) CARPETA=".opencode"; REGLAS="AGENTS.md"; GLOBAL="${XDG_CONFIG_HOME:-$HOME/.config}/opencode" ;;
  hermes)   CARPETA=".hermes";  REGLAS="AGENTS.md"; GLOBAL="$HOME/.hermes" ;;
  *) echo "Herramienta no soportada: $TOOL (usa claude, opencode o hermes)"; exit 1 ;;
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
