# Despliegue verificado

## Cuándo se usa
En cualquier puesta en producción: servicio, web, función, base de datos o fichero publicado.

## Qué resuelve
Separa "el proveedor ha aceptado el envío" de "el sistema funciona para quien lo usa". Son dos cosas distintas y la segunda es la única que importa.

## Procedimiento

1. **Antes de publicar:** batería en verde y árbol de trabajo limpio. Nunca se despliega con pruebas rojas.
2. **Publicar** con el mecanismo del proyecto, no con uno improvisado.
3. **Comprobar la URL viva**, desde fuera y sin sesión iniciada. Un 200 en la portada no basta: comprueba el flujo que importa.
4. **Comprobar que lo desplegado es lo que tienes.** Compara el identificador del commit publicado con el local. Un despliegue que sirve código viejo parece funcionar.
5. **Ver un flujo real de principio a fin**, con datos de prueba, y anotar el resultado.
6. **Tener plan de vuelta.** Saber cómo se revierte antes de necesitarlo.

## Errores que evita
- Dar por bueno un despliegue porque el panel está verde.
- Publicar código viejo por caché y perseguir un fallo que ya estaba arreglado.
- Detectar el fallo en producción y sin plan de vuelta.
- Olvidar el caso de quien entra sin sesión.

## Cómo se comprueba
La URL responde, el identificador desplegado coincide con el local y un flujo real funciona desde fuera. Los tres, no dos.
