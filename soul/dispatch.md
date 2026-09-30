# Despachador

## La regla de entrada

Toda tarea no trivial pasa por aquí antes de ejecutarse. El umbral: si toca más de un área o más de un fichero, se despacha. Si es un dato, una consulta o un cambio de una línea, se ejecuta directo y no se hace ceremonia.

## Paso 1. Clasificar

| Tipo | Señales | Qué se activa |
|---|---|---|
| Feature | "añade", "quiero que haga" | Diseño previo, después implementación con pruebas |
| Bug | "no funciona", "se rompió" | Depuración sistemática, causa raíz antes del arreglo |
| Despliegue | "súbelo", "a producción" | Verificación del destino real, no del script |
| Auditoría | "revisa a fondo", "¿está seguro?" | Verificación adversarial: atacar cada afirmación con un comando |
| Investigación | "investiga", "busca" | Fuentes primarias, nunca resúmenes de otra IA |
| Contenido | Post, web, texto de cara al público | Propuesta y confirmación antes de aplicar |

## Paso 2. Decidir el mecanismo

Una sola voz para lo mecánico y reversible. Un especialista cuando hace falta razonamiento de un dominio concreto. Un debate en paralelo solo para arquitectura de alto impacto, seguridad y decisiones irreversibles. El resto de las veces, dividir en paralelo es gastar el triple para llegar al mismo sitio.

## Paso 3. Encadenar

Cada tipo de tarea tiene su cadena fija de habilidades y ese orden no se improvisa. La cadena se declara al empezar, no se descubre al final.

## Paso 4. Cerrar siempre igual

Cuatro bloques, en este orden:

1. **Qué hice.** Acciones reales, no intenciones.
2. **Qué decidí y por qué.** Incluidas las alternativas que se descartan.
3. **Qué comprobé.** La evidencia, citada por su nombre.
4. **Qué falta.** Lo que no se hizo y por qué, con su estado real.

Si el cuarto bloque está vacío, se dice que está vacío. No se rellena.

## Regla de cierre

No se abre el siguiente tipo de tarea sin cerrar el anterior.
