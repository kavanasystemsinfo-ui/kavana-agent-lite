# Revisión de código

## Cuándo se usa
Cuando un cambio llega a revisión y hay que decidir si entra. Señales: PR abierto, commit en rama compartida, parche recibido por otro canal.

## Qué resuelve
Evita que entre código que rompe, que esconde deuda o que nadie podrá mantener. Una revisión que solo busca estilo deja pasar los fallos que duelen en producción.

## Procedimiento

1. **Leer el diff completo.** Sin saltar ficheros. Si el diff supera 400 líneas, pedir que se divida; una revisión grande no se hace bien.
2. **Ejecutar la batería local.** Antes de opinar, que los tests, linter y typecheck pasen en tu máquina. Un rojo ajeno no se revisa.
3. **Buscar la intención.** Cada cambio debe responder a un porqué. Si el autor no lo escribió, pregunta. Un cambio sin intención es ruido.
4. **Comprobar los bordes.** Entradas nulas, límites de array, tiempo de espera, permiso denegado, dato corrupto. Ahí es donde falla lo que pasa tests.
5. **Verificar que la prueba falla antes.** Si el cambio arregla algo, la prueba asociada debe estar en rojo en el commit anterior. Si no, el arreglo no está probado.
6. **Señalar, no arreglar.** Escribe el comentario con la ubicación exacta (`fichero:línea`) y el problema. El autor arregla; tú verificas la siguiente ronda.
7. **Aprobar solo cuando todo cuadra.** Verde en batería, intención clara, bordes cubiertos, prueba que fallaba y ahora pasa. Sin eso, no apruebas.

## Errores que evita
- Aprobar un cambio que rompe la batería en la máquina del revisor.
- Dejar pasar un arreglo sin prueba que lo respalde.
- Confundir preferencia de estilo con error de lógica.
- Callar un borde descubierto porque "el autor ya lo sabrá".
- Aprobar a ciegas porque el autor tiene buen historial.

## Cómo se comprueba
En la siguiente ronda, el diff resuelve cada comentario sin introducir rojos nuevos, y la batería completa queda en verde.