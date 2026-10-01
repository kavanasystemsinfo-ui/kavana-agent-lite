# Cómo comprobar que esto funciona

Cinco minutos, tres comprobaciones. No hace falta creerse nada.

## Antes de empezar

Hace falta `bash`, `git` y `python3` (probado con 3.11), y tener ya instalada la herramienta de agentes a la que le vas a copiar esto. Todo se ejecuta desde la raíz del repositorio clonado. Los scripts no llaman a la red: leen ficheros locales y usan git en local.

Si git no tiene identidad configurada, el commit de la prueba fallará por un motivo que no es la puerta. Configúrala antes: `git config user.name` y `git config user.email`.

## 1. La puerta corta de verdad

El escáner no se enciende solo: hay que instalarlo como gancho del repositorio que quieras proteger. El gancho llama al escáner de este clon por ruta absoluta, así que sirve para cualquier repositorio, no solo para este. Entra en el que quieras proteger y ejecuta:

```bash
./install.sh --gancho                 # sobre el repositorio git donde estes
./install.sh --tool claude --gancho   # o las dos cosas a la vez
```

Si ya tuvieras un gancho `pre-commit` propio, no lo pisa: avisa y no toca nada.

Copiar `guard/pre-commit` a mano a otro repositorio no sirve: esa copia busca el escáner dentro del repositorio donde se ejecuta y, al no encontrarlo, avisa y deja pasar el commit. Para proteger cualquier repositorio usa `--gancho`, que apunta al escáner por ruta absoluta.

El escáner, con gancho o sin él, se puede lanzar siempre:

```bash
python3 guard/scan.py --self-test      # debe decir: Prueba negativa OK
python3 guard/scan.py                  # debe decir: Puerta: limpio
```

Para verla fallar a propósito, crea un fichero con una cadena que parezca un token y una ruta de una carpeta personal, añádelo al índice de git y prueba a commitear. El gancho corta el commit y dice qué ha encontrado. Si el commit pasa, la puerta no está encendida en ese repositorio: comprueba que exista `.git/hooks/pre-commit`.

## 2. El estado del repositorio

```bash
python3 verify/battery.py
```

Imprime diez comprobaciones sobre el estado real: que el manifiesto quepa en una pantalla, que la puerta esté completa y en verde, que las skills sigan la plantilla y que lo que promete el README exista. Cualquier fallo sale con su nombre y su detalle.

B05 no se conforma con que el gancho esté bien escrito: comprueba que esté instalado en este repositorio. Si sale en rojo con `SIN encender`, es que te falta el paso 1.

La batería juzga este repositorio. No sirve para auditar proyectos ajenos, porque comprueba cosas como que el manifiesto quepa en una pantalla o que el roadmap interno no esté versionado.

## 3. Que la herramienta lo carga

Después de `./install.sh --tool <la tuya>`, reinicia la herramienta y pregunta tres cosas en este orden:

- **Quién eres y cómo trabajas.** Debe responder con los tres estados de entrega: implementado, verificado y desplegado.
- **Qué skills tienes.** Deben aparecer las de `craft/` por su nombre.
- **Lee una skill concreta.** Un listado no es una carga: si no reproduce el contenido, no la ha cargado.

## Desinstalar y actualizar

Para desinstalar, borra lo que dejó el instalador en el destino: `skills/`, el fichero de reglas (`CLAUDE.md` o `AGENTS.md`) y la carpeta `kavana-agent-lite/`. Si encendiste la puerta con `--gancho`, borra también `.git/hooks/pre-commit` del repositorio donde la pusiste.

Para actualizar, trae los cambios al clon (`git pull`) y repite `./install.sh --tool <la tuya> --gancho`. El instalador sobrescribe sus propias skills y su fichero de reglas, no los mezcla: si le has añadido reglas propias a ese fichero, guárdalas aparte antes.

## Dónde está cada cosa

- Las 16 skills, con una línea cada una: `docs/skills.md`.
- Los seis detectores, su severidad y su motivo: `guard/reglas.md`.
- Términos propios para tus proyectos: copia `guard/patterns.example.txt` a `guard/patterns.local.txt`. Ese fichero no se publica.
- Falsos positivos: declara el caso en `guard/allow.local.txt`. Tampoco se publica.

## Qué NO prueba esto

Que el agente sea bueno. Prueba que está instalado, que las reglas llegan y que la puerta impide publicar lo que no debe. El criterio se demuestra trabajando, no instalando.
