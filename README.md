# KAVANA Agent Lite

Un método para dirigir agentes de IA con criterio de ingeniería. No es un prompt largo: es una forma de trabajar que separa lo que está implementado, lo que está verificado y lo que está desplegado, y que no da nada por bueno sin evidencia.

## Para quién es

Para quien trabaja con agentes y está cansado de entregas que suenan bien y no se sostienen.

## Las tres reglas

1. **Tres estados, nunca dos.** Un trabajo está implementado, verificado o desplegado, y se nombra con la palabra exacta. Nunca se reporta como terminado si solo está implementado.
2. **Lectura de vuelta.** Nada se da por publicado sin releer el destino real. Un checkmark de un script no es una verificación.
3. **Sin verde falso.** Si un contador no cuadra, se reporta el fallo antes que el número.

## Cómo está montado

- `soul/`: quién es el agente, cómo decide y cómo cierra.
- `craft/`: procedimientos por área, uno por fichero, con la misma estructura.
- `guard/`: el escáner y la puerta que impide publicar lo que no debe salir.

## Empezar

```bash
./install.sh --tool claude        # o opencode, o hermes
./verify/battery.py               # comprueba el estado real del repositorio
```

## Qué no hace

No decide producto, no sustituye el criterio de quien lo usa y no guarda contexto de ningún negocio concreto.

## Estado

En construcción. La licencia está pendiente de decisión.
