# Cómo comprobar que esto funciona

Cinco minutos, tres comprobaciones. No hace falta creerse nada.

## 1. La puerta corta de verdad

```bash
python3 guard/scan.py --self-test      # debe decir: Prueba negativa OK
python3 guard/scan.py                  # debe decir: Puerta: limpio
```

Para verla fallar a propósito, crea un fichero con una cadena que parezca un token y una ruta de una carpeta personal, añádelo al índice de git y prueba a commitear. El gancho corta el commit y dice qué ha encontrado. Si no lo corta, la puerta no sirve.

## 2. El estado del repositorio

```bash
python3 verify/battery.py
```

Imprime diez comprobaciones sobre el estado real: que el manifiesto quepa en una pantalla, que la puerta esté completa y en verde, que las skills sigan la plantilla y que lo que promete el README exista. Cualquier fallo sale con su nombre y su detalle.

## 3. Que la herramienta lo carga

Después de `./install.sh --tool <la tuya>`, reinicia la herramienta y pregunta tres cosas en este orden:

- **Quién eres y cómo trabajas.** Debe responder con los tres estados de entrega: implementado, verificado y desplegado.
- **Qué skills tienes.** Deben aparecer las de `craft/` por su nombre.
- **Lee una skill concreta.** Un listado no es una carga: si no reproduce el contenido, no la ha cargado.

## Qué NO prueba esto

Que el agente sea bueno. Prueba que está instalado, que las reglas llegan y que la puerta impide publicar lo que no debe. El criterio se demuestra trabajando, no instalando.
