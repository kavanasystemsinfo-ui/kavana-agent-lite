# Testing y calidad

## Cuándo se usa
Cuando el código cambia y hay que garantizar que no se rompe lo que ya funcionaba. Señales: commit nuevo, PR, release, refactor, arreglo de bug.

## Qué resuelve
Convierte la esperanza "probablemente funcione" en evidencia "esto pasa y esto no". Sin tests, cada cambio es una apuesta.

## Procedimiento

1. **Pirámide real.** Tests unitarios (rápidos, muchos), de integración (lentos, pocos), de contrato (uno por frontera). Sin pirámide, la suite tarda horas o no cubre nada.
2. **Test que falla antes.** Para cada arreglo o feature, el test se escribe en rojo primero. Si no falla antes, no prueba lo que crees.
3. **Nombres que explican.** `test_usuario_sin_saldo_no_puede_comprar` dice qué y por qué. `test_compra_1` no dice nada.
4. **Datos de prueba controlados.** Fábricas o builders, no fixtures compartidos. Un test modifica sus datos, no los del vecino.
5. **Determinismo.** Mismo input → mismo output siempre. Nada de `Thread.sleep`, fechas reales, orden de hash, red externa. Lo no determinista se moca en la frontera.
6. **Cobertura por riesgo, no porcentaje.** El 80 % de cobertura en código trivial vale menos que el 20 % en la ruta de pago.
7. **Suite rápida en CI.** Unidad + contrato < 3 min. Integración en job aparte. Si la suite lenta bloquea merges, la gente la salta.

## Errores que evita
- Bug regresivo en producción porque nadie escribió test para el caso borde.
- Suite que tarda 40 minutos y nadie la corre en local.
- Test frágil que falla al cambiar un nombre de variable sin tocar lógica.
- Fixture compartida que rompe 10 tests al cambiar un campo.
- Cobertura 90 % en getters/setters y 0 % en la máquina de estados.

## Cómo se comprueba
Ejecuta la suite en CI: unidad+contrato < 3 min, 0 tests frágiles en 100 corridas, cada bug histórico tiene su test de regresión que falla si se revierte el arreglo.