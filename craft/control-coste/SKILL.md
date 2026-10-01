# Control de coste

## Cuándo se usa
Cuando el sistema consume recursos que se facturan: tokens de modelo, segundos de CPU, GB de almacenamiento, peticiones a API, ancho de banda, instancias.

## Qué resuelve
Que el coste sea predecible, visible y acotado. Un sistema sin control de coste crece hasta que la factura obliga a apagarlo.

## Procedimiento

1. **Unidad de coste.** Define qué se mide: €/1k tokens, €/hora instancia, €/GB mes, €/M peticiones. Una sola unidad por recurso.
2. **Presupuesto por operación.** Cada acción del usuario tiene un techo (ej. "resumir documento ≤ 0,05 €"). Si la estimación supera el techo, la acción se rechaza o se degrada.
3. **Medición en tiempo real.** Cada operación suma su coste a un contador del periodo (hora, día, mes). El contador vive en almacenamiento persistente, no en memoria.
4. **Alerta por tramos.** Avisos al 50 %, 80 %, 95 % del presupuesto del periodo. La alerta llega a quien decide, no solo al log.
5. **Degradación elegante.** Al 95 %, las operaciones no críticas se desactivan (ej. análisis opcional, enriquecimiento, reintentos extra). El núcleo sigue.
6. **Informe periódico.** Resumen semanal: coste total, por operación, por recurso, tendencia, previsión fin de mes. Sin informe, el coste es una sorpresa.
7. **Revisión de proveedores.** Cada trimestre: ¿sigue siendo el mejor precio/rendimiento? Cambiar de proveedor es una operación normal, no una excepción.

## Errores que evita
- Factura de fin de mes 10× lo estimado porque nadie midió por operación.
- Servicio caído porque se agotó la cuota de API y no había degradación.
- Instancias "temporales" corriendo 6 meses sin etiqueta de propietario.
- Cambio de modelo que duplica el coste por token y nadie lo nota hasta la factura.
- Alerta que llega al canal técnico pero nadie con poder de gasto la ve.

## Cómo se comprueba
Ejecuta 1.000 operaciones simuladas con coste variable. Verifica: contador coincide con suma unitaria, alerta dispara en los tramos, degradación desactiva lo declarado, informe cierra cifras sin huecos.