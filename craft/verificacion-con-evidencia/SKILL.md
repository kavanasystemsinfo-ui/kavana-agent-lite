# Verificación con evidencia

## Cuándo se usa
Antes de decir que algo está hecho, y siempre que alguien pregunte por el estado de un trabajo.

## Qué resuelve
Elimina la distancia entre "lo he hecho" y "funciona". La mayor parte de la desconfianza con agentes no viene de que fallen, sino de que informan de un éxito que nadie ha comprobado.

## Procedimiento

1. **Nombrar el estado exacto.** Implementado (existe y compila), verificado (hay una ejecución real) o desplegado (funciona fuera de tu máquina). Si depende de algo que no existe, bloqueado por dependencia.
2. **Citar la evidencia por su nombre.** El comando y su salida, la URL y su respuesta, el fichero releído. "Los tests pasan" no es evidencia; el nombre de la batería y su resultado sí.
3. **Leer de vuelta el destino.** Si algo se publicó, se subió o se envió, se relee del destino real. Un checkmark de un script no demuestra nada.
4. **Reportar el fallo antes que el número.** Si un contador no cuadra, ese fallo es el titular.
5. **Dejar escrito lo que falta.** Una lista vacía se declara vacía, no se rellena con relleno.

## Errores que evita
- Reportar como desplegado lo que solo está implementado.
- Aceptar el autoinforme de un subagente, de un script o de un tercero sin comprobarlo.
- Dar por bueno un despliegue porque la interfaz del proveedor está verde.
- Esconder un rojo porque el resto está en verde.

## Cómo se comprueba
Por cada afirmación del informe, existe un comando, una URL o un fichero que la respalda, y quien lo lee puede repetirlo.
