# Versionado y compatibilidad

## Cuándo se usa
Cuando una API, esquema, evento o contrato cambia y hay consumidores que no se pueden romper. Señales: endpoint nuevo, campo eliminado, tipo cambiado, enum extendido, cabecera distinta.

## Qué resuelve
Permite evolucionar el sistema sin forzar a todos a actualizar a la vez. Sin estrategia de versión, cada cambio es un riesgo de rotura.

## Procedimiento

1. **Versionar en la URL o cabecera.** `/v1/recursos`, `Accept: application/vnd.miapi.v2+json`. La versión viaja en la petición, no en el código.
2. **Contrato explícito.** OpenAPI/AsyncAPI generado desde código, versionado en git. Lo que no está en el contrato no existe.
3. **Regla de compatibilidad.** Aditivo = compatible (nuevo campo opcional, nuevo endpoint, nuevo valor en enum documentado). Sustractivo = breaking (borrar campo, cambiar tipo, endurecer validación).
4. **Deprecación con fecha.** Lo que se va a quitar se marca `deprecated: true` con `sunset: "2026-12-31"`. Se avisa a consumidores 3 meses antes.
5. **Adaptadores, no bifurcación.** Un cambio breaking se implementa en versión nueva; la vieja delega a un adaptador que traduce. Nada de `if version == 1` esparcido.
6. **Tests de contrato.** Consumer-driven contracts (Pact) o tests de esquema contra versión anterior. Un breaking sin test no entra.
7. **Lifecycle documentado.** `SUPPORTED` (parches + features), `DEPRECATED` (solo seguridad), `RETIRED` (apagado). Cada versión tiene dueño y fecha de revisión.

## Errores que evita
- Consumidor roto en producción porque se eliminó un campo "que nadie usaba".
- Dos años manteniendo código zombie porque no hubo plan de retiro.
- `if (version === 1) { ... } else { ... }` en 40 ficheros.
- Nuevo endpoint que rompe cliente viejo porque cambió el formato de fecha.
- Enum extendido en servidor que hace explotar validación estricta en cliente.

## Cómo se comprueba
Suite de contrato: petición v1 contra código v2 → respuesta válida v1. Petición v2 contra código v1 → error 406 documentado. Tests de Pact pasan en CI para cada versión `SUPPORTED`.