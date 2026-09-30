# Qué cuenta como contaminación

La puerta existe porque publicar el trabajo de un agente no es publicar su contenido, sino su criterio. Lo que se cuela no suele ser un secreto evidente, que se ve a simple vista, sino el decorado: el nombre de un producto propio dentro de un ejemplo, una ruta del equipo donde se desarrolló, la foto del estado de un servidor concreto o el rastro que deja una sustitución automática de nombres.

Ese material enseña más de lo que quieres enseñar y además se lee mal. Un documento saneado a medias delata que lo has saneado.

## Categorías que cortan el paso (BLOCK)

| Categoría | Qué busca |
|---|---|
| Credencial | Cadenas con la forma de un token de proveedor, claves de API o claves privadas |
| Ruta personal | Rutas del equipo donde se trabajó: la carpeta personal del sistema, la de un usuario concreto o rutas de Windows con nombre de usuario |

## Categorías que exigen revisión (REVIEW)

| Categoría | Qué busca |
|---|---|
| Término propio | Nombres de productos, clientes o personas, desde una lista local que no se publica |
| Cifra de máquina | Porcentajes de memoria o disco, tamaños y antigüedad de copias de seguridad |
| Resto de saneado | Un sustituto de nombre usado como nombre propio, señal de una sustitución automática |
| Dato personal | Direcciones de correo y formas de contacto |

## Por qué la lista de términos no está en el repositorio

Porque publicarla sería publicar justo lo que protege. Vive en `guard/patterns.local.txt`, ignorado por git, y cada persona que use esto escribe la suya. El repositorio solo incluye `guard/patterns.example.txt` con marcadores.

Lo mismo con las excepciones: `guard/allow.local.txt` permite declarar falsos positivos con la forma `ruta:detector`, y tampoco se publica.

## Lo que el escáner no puede hacer

No entiende de contexto. Un caso real reescrito a mano puede pasar la puerta y seguir siendo un caso real. Por eso la regla principal del proyecto no es escanear, es escribir desde cero: el escáner es la red, no el criterio.
