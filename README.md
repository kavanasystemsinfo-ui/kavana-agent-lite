# KAVANA Agent Lite

Un método para dirigir agentes de IA con criterio de ingeniería. No es un prompt largo: es una forma de trabajar que separa lo que está implementado, lo que está verificado y lo que está desplegado, y que no da nada por bueno sin evidencia.

## Para quién es

Para quien trabaja con agentes y está cansado de entregas que suenan bien y no se sostienen.

## Las tres reglas

1. **Tres estados, nunca dos.** Un trabajo está implementado, verificado o desplegado, y se nombra con la palabra exacta. Nunca se reporta como terminado si solo está implementado.
2. **Lectura de vuelta.** Nada se da por publicado sin releer el destino real. Un checkmark de un script no es una verificación.
3. **Sin verde falso.** Si un contador no cuadra, se reporta el fallo antes que el número.

## Qué hay

- `soul/` — identidad, reglas, despachador (cómo clasifica, encadena y cierra)
- `craft/` — 16 skills (procedimientos), una por carpeta, misma plantilla
- `guard/` — escáner (6 detectores) + pre-commit que corta commits (`--gancho`, ver `docs/verificar.md`)
- `verify/` — batería 10 checks reales (caza fallos de verdad)
- `install.sh` — instala en claude, opencode, hermes, codex
- `LICENSE` — MIT

## Empezar

```bash
./install.sh --tool claude --gancho   # o opencode, hermes, codex
./verify/battery.py               # 10/10 OK
python3 guard/scan.py             # Puerta: limpio
```

## Verificar instalación (3 pasos)

1. Pregunta: "quien eres y como trabajas?" → responde con tres estados
2. Pregunta: "que skills tienes disponibles?" → lista 16 skills
3. Pide leer una skill y reproducir su contenido → no es un listado

## Qué no hace

No decide producto, no sustituye criterio, no guarda contexto de negocio.

## Licencia

MIT — uso libre, incluso comercial.