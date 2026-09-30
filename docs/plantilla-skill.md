# Plantilla de skill

Toda skill de `craft/` usa esta estructura, en este orden y con estos títulos. La batería de `verify/` lo comprueba: una skill fuera de plantilla falla.

```markdown
# <Nombre de la skill>

## Cuándo se usa
La señal concreta que hace falta para que alguien la cargue. Sin contexto de ningún proyecto.

## Qué resuelve
El problema real, en dos o tres líneas. Qué pasa si no se aplica.

## Procedimiento
Pasos numerados, en orden. Cada paso verificable.

## Errores que evita
Los fallos concretos que esta skill previene, uno por línea.

## Cómo se comprueba
La comprobación que demuestra que se aplicó bien.
```

## Reglas de escritura

- Un fichero, una lección. Si dos skills enseñan lo mismo, sobra una.
- El ejemplo que se use tiene que ser inventado. Nunca adaptado de un caso real: el decorado de un caso real viaja dentro del ejemplo aunque cambies los nombres.
- Sin cifras de máquinas concretas, sin rutas del equipo donde se escribió y sin nombres de nadie.
- Frases cortas. Si una frase necesita dos comas explicativas, son dos frases.
