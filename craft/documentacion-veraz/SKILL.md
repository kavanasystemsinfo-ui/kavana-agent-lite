# Documentación veraz

## Cuándo se usa
Al cerrar una decisión técnica, al cambiar el comportamiento de algo o cuando alguien nuevo tiene que entender el proyecto.

## Qué resuelve
Una documentación que miente cuesta más que no tenerla: hace perder el tiempo a quien confía en ella. El objetivo no es documentar mucho, es que lo escrito siga siendo cierto.

## Procedimiento

1. **Documentar decisiones, no actividad.** Lo que se hizo hoy no interesa; por qué se eligió esto y qué se descartó, sí.
2. **Cada decisión con su alternativa.** Qué se valoró y por qué se dejó fuera. Sin la alternativa, la decisión parece arbitraria.
3. **Un cambio de comportamiento obliga a tocar la documentación** en el mismo cambio, no en uno posterior que nunca llega.
4. **Si el documento contradice al código, gana el código.** Se arregla la contradicción el mismo día que se detecta.
5. **Marcar lo viejo como viejo.** Los documentos con fecha que parecen actuales son la peor trampa: se les pone una nota que avisa de a qué fecha se refieren.

## Errores que evita
- READMEs que describen una versión que ya no existe.
- Decisiones sin contexto, imposibles de revisar después.
- Métricas congeladas presentadas como actuales.
- Documentar por documentar, hasta que nadie encuentra nada.

## Cómo se comprueba
Se coge el documento, se siguen sus pasos tal cual y el resultado es el que describe. Si no, el documento está mal.
