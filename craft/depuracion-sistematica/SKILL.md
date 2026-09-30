# Depuración sistemática

## Cuándo se usa
Cuando algo no funciona y la causa no es evidente. Señales: "no funciona", "falla a veces", "esto antes iba", un test rojo sin motivo claro.

## Qué resuelve
Convierte un problema difuso en una causa concreta y en un arreglo que no vuelve. Sin este orden, lo normal es parchear el síntoma y volver a verlo en dos semanas con otra cara.

## Procedimiento

1. **Reproducir.** Consigue el fallo de forma repetible y anota el comando exacto. Un fallo que no se reproduce no se puede arreglar, solo se puede esconder.
2. **Acotar.** Divide el sistema por la mitad y comprueba en qué mitad está. Repite. Adivinar es más lento que partir en dos.
3. **Escribir la prueba que falla.** Antes de tocar el arreglo, deja el fallo escrito en una prueba que hoy está en rojo. Esa prueba es lo que impide que vuelva.
4. **Causa raíz.** Explica el fallo en una frase que empiece por "esto pasa porque". Si la frase necesita un "y además", hay dos fallos.
5. **Arreglo mínimo.** Lo más pequeño que deja la prueba en verde. Nada de arreglos de paso.
6. **Comprobar el conjunto.** Ejecuta toda la batería, no solo la prueba nueva.
7. **Anotar.** Qué se aprendió y dónde, para que el siguiente no repita el camino.

## Errores que evita
- Arreglar el síntoma y dar por cerrado un problema que sigue vivo.
- Cambiar tres cosas a la vez y no saber cuál lo arregló.
- Cerrar sin prueba, de modo que el fallo vuelve sin avisar.
- Confundir "ya no lo veo" con "ya no está".

## Cómo se comprueba
La prueba escrita en el paso 3 falla antes del arreglo y pasa después, y la batería completa queda en verde.
