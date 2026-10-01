# Las 16 skills, una por una

- **`concurrencia-estado`** — Concurrencia y estado. Evita corrupción de datos, trabajo duplicado, bloqueos infinitos y estados imposibles.
- **`configuracion-secretos`** — Configuración y secretos. Elimina "funciona en mi máquina" y "la clave está en el repo".
- **`control-coste`** — Control de coste. Que el coste sea predecible, visible y acotado.
- **`datos`** — Datos. Evita que los datos se corrompan, se pierdan o mientan.
- **`depuracion-sistematica`** — Depuración sistemática. Convierte un problema difuso en una causa concreta y en un arreglo que no vuelve.
- **`despliegue-verificado`** — Despliegue verificado. Separa "el proveedor ha aceptado el envío" de "el sistema funciona para quien lo usa".
- **`documentacion-veraz`** — Documentación veraz. Una documentación que miente cuesta más que no tenerla: hace perder el tiempo a quien confía en ella.
- **`integracion-modelos`** — Integración de modelos. Que la llamada al modelo no sea un agujero negro: coste desconocido, latencia variable, respuesta inválida, proveedor caído, versión cambiada sin aviso.
- **`interfaz`** — Interfaz. Que la persona haga lo que vino a hacer sin adivinar, sin esperar y sin romperse.
- **`investigacion-con-fuentes`** — Investigación con fuentes. Evita construir sobre datos que suenan plausibles y no son ciertos.
- **`observabilidad`** — Observabilidad. Elimina la caja negra.
- **`revision-de-codigo`** — Revisión de código. Evita que entre código que rompe, que esconde deuda o que nadie podrá mantener.
- **`seguridad-adversarial`** — Seguridad adversarial. Convierte la suposición "esto no pasará" en una barrera que lo detiene aunque pase.
- **`testing-calidad`** — Testing y calidad. Convierte la esperanza "probablemente funcione" en evidencia "esto pasa y esto no".
- **`verificacion-con-evidencia`** — Verificación con evidencia. Elimina la distancia entre "lo he hecho" y "funciona".
- **`versionado-compatibilidad`** — Versionado y compatibilidad. Permite evolucionar el sistema sin forzar a todos a actualizar a la vez.

## Cómo se usan

No hay que invocarlas a mano. `soul/dispatch.md` clasifica la tarea y encadena las que tocan, en orden. Cada skill es un procedimiento y trae su propia comprobación: si no se puede comprobar, no está terminada.

## Cómo se añade una

Copia `docs/plantilla-skill.md`, rellena las cinco secciones y guarda el fichero como `craft/<nombre>/SKILL.md`. La batería (B06) comprueba que la plantilla se respeta, y también que este índice las siga listando todas.
