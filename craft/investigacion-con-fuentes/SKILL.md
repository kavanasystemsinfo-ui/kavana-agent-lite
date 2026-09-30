# Investigación con fuentes

## Cuándo se usa
Cuando hay que averiguar algo del mundo exterior: precios, límites de una API, compatibilidades, versiones, disponibilidad.

## Qué resuelve
Evita construir sobre datos que suenan plausibles y no son ciertos. Un dato equivocado en un diseño se paga tres veces: al implementar, al depurar y al explicarlo.

## Procedimiento

1. **Ir a la fuente primaria.** La documentación oficial, la web del vendedor, la respuesta de la propia API. Los resúmenes de otra IA no son fuente, son pistas.
2. **Anotar la fecha del dato.** Un límite de plan gratuito de hace un año es un dato viejo, no un dato.
3. **Distinguir "no hay" de "no he podido".** Un bloqueo, un muro de pago o un error del sitio se reportan como bloqueo. "Sin resultados" se reserva a haber buscado de verdad.
4. **Comprobar lo crítico por dos vías.** Si el dato decide dinero, seguridad o arquitectura, se confirma en dos sitios independientes.
5. **Escribir la cita.** De dónde salió, con enlace y fecha, para que cualquiera lo repita.

## Errores que evita
- Dar por bueno un dato de un resumen generado.
- Diseñar sobre una cuota o un límite que ya no existe.
- Presentar un bloqueo como una ausencia de información.
- Perder la trazabilidad de dónde salió cada cifra.

## Cómo se comprueba
Cada dato del informe tiene su enlace y su fecha, y el lector puede abrirlo y ver lo mismo.
