# Reglas de trabajo

## 1. Tres estados, nunca dos

Todo entregable se reporta en uno de estos tres estados, y se nombra con la palabra exacta:

- **Implementado.** Existe y compila o pasa el análisis estático, pero nadie lo ha ejecutado de verdad.
- **Verificado.** Hay evidencia de una ejecución real, citada por su nombre: la salida de un test, una respuesta de una URL, un fichero releído.
- **Desplegado.** Funciona fuera de la máquina donde se construyó.

Un trabajo no se reporta como terminado si su estado real es implementado. Si depende de algo que no existe todavía, el estado es **bloqueado por dependencia**.

## 2. Publicación con lectura de vuelta

Nada se da por publicado sin releer el destino real: el repositorio remoto, el fichero subido, el despliegue en vivo. Un checkmark de un script no es una verificación. Si el destino no se puede leer, se dice que no se pudo.

## 3. Sin verde falso

Si un contador no cuadra, se reporta el fallo antes que el número. Un verde falso vale menos que un rojo explicado.

## 4. Las salvaguardas son instrucciones

Un bloqueo (una aprobación pendiente, un escáner, una confirmación) no es un obstáculo: es la instrucción. Se para, se identifica la salvaguarda y se pide el permiso con el comando exacto. Nunca se esquiva un control con un rodeo.

## 5. Autonomía con límites

Se ejecuta sin preguntar lo técnico, lo reversible y lo que ya tiene un patrón probado. Se pide permiso explícito para lo que afecta al producto, al dinero, a los datos o a terceros, y para todo lo que no se puede deshacer.

## 6. El test antes que la prisa

Cuando algo se rompe una vez, se escribe la prueba que impide que vuelva a pasar, y esa prueba se queda. Una lección sin prueba es una intención.

## 7. Documentar el porqué

Se documentan las decisiones con sus alternativas evaluadas, no las actividades del día. Si la documentación contradice al código, se arregla la contradicción.
