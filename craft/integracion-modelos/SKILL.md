# Integración de modelos

## Cuándo se usa
Cuando el sistema llama a un modelo de lenguaje, de embeddings, de visión o de audio: proveedor cloud, autoalojado, local, o cadena de varios.

## Qué resuelve
Que la llamada al modelo no sea un agujero negro: coste desconocido, latencia variable, respuesta inválida, proveedor caído, versión cambiada sin aviso.

## Procedimiento

1. **Contrato de entrada y salida.** Qué campos envías, qué campos esperas, qué tipos, qué rangos. El contrato se valida antes de enviar y al recibir.
2. **Timeout y reintentos.** Tiempo máximo por llamada (ej. 30 s). Reintento con backoff solo en errores transitorios (5xx, red). En 4xx no reintentas: arreglas la petición.
3. **Clave por entorno.** Cada entorno (desarrollo, staging, producción) usa su clave. Ninguna clave viaja en código ni en imagen de contenedor.
4. **Fallback declarado.** Qué pasa si el modelo no responde: respuesta cacheada, mensaje estático, error amable, modelo alternativo. El fallback se prueba, no se imagina.
5. **Observabilidad real.** Cada llamada registra: modelo, versión, tokens entrada/salida, latencia, coste estimado, éxito/fallo. Sin registro, no hay optimización.
6. **Versión fijada.** El nombre del modelo incluye la versión (ej. `gpt-4o-2024-08-06`). Un proveedor que cambia el comportamiento sin avisar no rompe tu contrato.
7. **Presupuesto por unidad.** Coste máximo por operación (ej. 0,02 €/resumen). Si la llamada lo supera, se rechaza antes de enviarla.

## Errores que evita
- Factura de 3.000 € porque un bucle llamó al modelo sin límite.
- Respuesta truncada porque `max_tokens` era demasiado bajo.
- Producción caída porque el proveedor cambió el formato de respuesta.
- Clave de producción en repositorio público.
- Usuario esperando 2 minutos sin indicador porque el modelo tardó y no había timeout.

## Cómo se comprueba
Simula 100 llamadas: 90 exitosas, 5 timeout, 3 error 5xx, 2 error 4xx. Verifica que latencia, coste, fallback y registro cumplen lo declarado en cada caso.