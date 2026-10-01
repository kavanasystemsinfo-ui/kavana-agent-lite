# Concurrencia y estado

## Cuándo se usa
Cuando varias peticiones tocan el mismo recurso a la vez: doble clic, reintentos, colas, workers paralelos, WebSockets, tareas programadas que se solapan.

## Qué resuelve
Evita corrupción de datos, trabajo duplicado, bloqueos infinitos y estados imposibles. Sin control de concurrencia, "funciona en mi máquina" muere en producción.

## Procedimiento

1. **Identificar la sección crítica.** Qué recurso (fila, fichero, clave de caché, dispositivo) no admite escrituras simultáneas. Si no está identificado, no se protege.
2. **Elegir el primitivo adecuado.**
   - Fila BD: `SELECT ... FOR UPDATE` / `UPDATE ... WHERE version = X` (optimista).
   - Clave distribuida: Redis `SET NX EX` + Lua para renovación.
   - Fichero: `flock` / `open(O_EXCL)`.
   - Operación larga: token de idempotencia en la petición.
3. **Idempotencia por defecto.** Toda mutación acepta `Idempotency-Key`. Mismo key → mismo resultado, sin efecto lateral doble. La clave la genera el cliente, el servidor la almacena con TTL.
4. **Timeout y reintento acotado.** Espera máxima (ej. 5 s). Backoff exponencial + jitter. Máximo 3 reintentos. Sin límite, un deadlock cuelga el hilo.
5. **Orden global de locks.** Si se toman varios, siempre en el mismo orden (ej. `ORDER BY id`). Distinto orden = deadlock garantizado.
6. **Estado visible.** Cada recurso tiene `estado` (pendiente, procesando, completado, fallido) y `actualizado_en`. Una consulta dice en qué va, no "no sé".
7. **Observar la contención.** Métrica `lock_wait_ms`, `reintentos_total`, `idempotency_hits`. Si sube, hay diseño que arreglar, no hardware que comprar.

## Errores que evita
- Doble cargo porque el usuario pulsó dos veces y no hubo idempotencia.
- Fila bloqueada 30 s porque un worker murió con la transacción abierta.
- Deadlock en producción porque servicio A toma (1,2) y servicio B toma (2,1).
- Contador desfasado porque dos hilos leen-escriben sin `FOR UPDATE`.
- Trabajo repetido 50 veces porque el consumidor de cola no ack y reencola infinito.

## Cómo se comprueba
Simula 1.000 peticiones concurrentes contra el mismo recurso (herramienta de carga o script). Verifica: cero escrituras perdidas, cero duplicados por idempotencia, latencia p99 < 200 ms, cero deadlocks, métricas de contención registradas.