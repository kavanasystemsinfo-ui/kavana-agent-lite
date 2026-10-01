# Seguridad adversarial

## Cuándo se usa
Cuando el sistema recibe datos que no controlas: peticiones web, ficheros subidos, parámetros de URL, cabeceras, websockets, colas de mensajes.

## Qué resuelve
Convierte la suposición "esto no pasará" en una barrera que lo detiene aunque pase. La mayoría de los incidentes graves empiezan por una entrada que nadie validó.

## Procedimiento

1. **Listar la superficie.** Cada punto donde entra dato externo: endpoint, consumidor de cola, lector de fichero, webhook. Si no está en la lista, no se protege.
2. **Definir el contrato.** Qué forma, tamaño, tipo y rango se acepta. Todo lo que no encaje, se rechaza antes de tocar lógica de negocio.
3. **Validar en la frontera.** La comprobación vive en la capa de entrada, no en el servicio. Un validador compartido evita duplicar y olvidar.
4. **Codificar la salida.** Lo que vuelve al exterior (HTML, JSON, SQL, shell, encabezado) se escapa para su contexto. Una variable no escapa a sí misma.
5. **Limitar el radio.** Tiempo de espera, tamaño de cuerpo, profundidad de recursión, tasa de peticiones. Un bucle infinito externo no agota tu proceso.
6. **Registrar el rechazo.** Cada bloqueo deja traza: qué llegó, por qué se rechazó, de qué IP o identidad. Sin traza, no hay patrón que detectar.
7. **Probar el rechazo.** Escribe pruebas que envíen basura deliberada: SQL en un nombre, script en un comentario, 10 MB en un avatar. Cada una debe ser rechazada limpia.

## Errores que evita
- Inyección SQL porque el parámetro se concatenó sin parámetros preparados.
- XSS almacenado porque un campo de texto se renderizó sin escape HTML.
- Traversal de ruta porque un nombre de fichero llegó sin normalizar.
- Denegación de servicio porque un cuerpo de 500 MB saturó memoria.
- Fuga de datos porque un error interno devolvió la pila completa al cliente.

## Cómo se comprueba
Un escáner automatizado (o suite propia) lanza 50 variantes de entrada maliciosa contra cada punto de la lista: cero llegan a la lógica de negocio y todas dejan traza en el registro.