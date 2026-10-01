# Observabilidad

## Cuándo se usa
Cuando el sistema está en producción y hay que saber qué pasa sin adivinar. Señales: latencia rara, error 5xx, usuario reporta "va lento", capacity planning, post-mortem.

## Qué resuelve
Elimina la caja negra. Sin observabilidad, un incidente dura horas porque nadie sabe por dónde empezar.

## Procedimiento

1. **Tres pilares, no uno.** Logs (qué pasó), métricas (cuánto/qué tan seguido), trazas (por dónde fue). Los tres enlazados por `trace_id`.
2. **Logs estructurados.** JSON con campos fijos: `timestamp`, `level`, `service`, `trace_id`, `span_id`, `message`, `contexto`. Sin `printf` suelto.
3. **Métricas con cardinalidad acotada.** Contadores, histogramas, gauges. Etiquetas: `route`, `status`, `handler`. Nunca `user_id`, `request_id`, `session_id` — explotan la base.
4. **Trazas por petición.** Cada petición entrante inicia una traza; cada llamada saliente (DB, HTTP, cola) crea un span. Propaga `traceparent` (W3C).
5. **Alertas por síntoma, no por causa.** "Latencia p99 > 2s en /pago" dispara. "CPU > 80 %" no: a veces es normal, a veces no.
6. **Dashboards por rol.** Operación: rojo/verde por servicio. Negocio: pedidos/min, errores de pago. Desarrollo: latencia por endpoint, tasa de error por versión.
7. **Retención y coste.** Logs calientes 7 días, fríos 90 días. Métricas 13 meses. Trazas 10 % muestreo (100 % en errores). El coste se revisa cada trimestre.

## Errores que evita
- Incidente de 3 horas porque los logs no tienen `trace_id` y no se puede correlacionar.
- Alerta que dispara 50 veces al día y la gente la silencia.
- Métrica `http_requests_total{user_id="..."}` que hace caer Prometheus.
- Dashboard que muestra "todo verde" pero los usuarios ven errores.
- Post-mortem que dice "no sabemos qué pasó" porque no hay trazas.

## Cómo se comprueba
Despliega en staging: genera 1.000 peticiones reales. Verifica: cada una tiene traza completa, logs JSON parseables, métricas en dashboard, alerta de prueba dispara y resuelve en < 2 min.