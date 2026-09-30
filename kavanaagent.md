# kavanaagent.md — Roadmap de KAVANA Agent Lite

Este fichero es la única fuente de verdad del estado del proyecto. Se actualiza al cerrar cada bloque de trabajo, no al final. Una casilla solo se marca con evidencia citada (un comando, una URL o un fichero), nunca porque "ya debería estar".

**Regla de oro de este fichero: se publica con el repo.** Todo lo que se escriba aquí tiene que poder leerlo un desconocido. Lo que no cumpla eso no vive aquí.

- Última actualización: 2026-09-30
- Fase actual: 1, La puerta
- Visibilidad del repo: privado hasta la fase 5

## 1. Reglas no negociables

1. **Nada reciclado.** Los ejemplos y las skills se escriben desde cero para este repo. Motivo medido: al reciclar material de la versión completa, dos pasadas de limpieza de nombres dejaron seis ficheros de utilidad de proyectos reales, veinticuatro líneas con restos de saneado y el nombre de un producto vivo sobreviviendo. Renombrar no limpia: el decorado de un caso real viaja dentro del ejemplo.
2. **La puerta primero.** Antes de escribir contenido, el escáner que impide que ese contenido se contamine.
3. **Sin datos de nadie.** Ni nombres de personas ni de proyectos, ni rutas del equipo donde se desarrolla, ni el estado de un servidor concreto, ni cifras de una máquina concreta (memoria, disco, antigüedad de copias).
4. **Un fichero, una lección.** Si dos ficheros enseñan lo mismo, sobra uno.
5. **Cada afirmación del README se puede ejecutar o citar.** Si no, fuera.
6. **Sin comparativas con la versión privada.** Una tabla de "esto sí, esto no" habla de cuánto se guarda quien publica, no de criterio.

## 2. Decisiones tomadas

| Fecha | Decisión | Por qué |
|---|---|---|
| 2026-09-30 | El repo nace privado | Publicar antes de que la puerta esté en verde repite el fallo anterior |
| 2026-09-30 | Nombre: KAVANA Agent Lite | Decisión del propietario |
| 2026-09-30 | Tres capas: soul, craft y guard | Separar identidad, oficio y control. Ninguna carpeta de proyecto |
| 2026-09-30 | Sin inventario de la versión completa | Cuenta cantidad, no criterio |
| 2026-09-30 | Este roadmap es publicable | Vive en el repo y se publicará con él |

## 3. Decisiones abiertas

- [ ] Licencia: permisiva (uso libre, incluso comercial) o restrictiva (lectura pública con derechos reservados). Es estrategia, no técnica.
- [ ] Idioma del README público: español, inglés o los dos.
- [ ] Herramientas soportadas en el instalador: recortar a tres.
- [ ] Momento de pasar el repo a público.

## 4. Fases

### Fase 1: La puerta (actual)

- [ ] `guard/scan.py`: escáner que corre antes del commit. Detecta términos de dominio del autor, nombres de proyectos y de personas, rutas personales, formas de credencial (token, clave, cadena firmada), restos de saneado automático y rutas absolutas de un equipo concreto.
- [ ] `guard/reglas.md`: qué se considera contaminación y por qué, con los casos ya medidos.
- [ ] `guard/pre-commit`: gancho que ejecuta el escáner y corta el commit.
- [ ] Prueba negativa obligatoria: meter a propósito un caso real y comprobar que el escáner lo caza.

**Terminado cuando:** el escáner pasa en verde sobre el esqueleto del repo, y falla con mensaje claro ante un caso real metido a propósito, y el gancho corta el commit de verdad.

### Fase 2: El alma

- [ ] `soul/identity.md`: quién es, para quién trabaja y qué no hace.
- [ ] `soul/rules.md`: los tres estados de entrega, publicación con lectura de vuelta, salvaguardas, límites de autonomía y honestidad sobre lo no verificado.
- [ ] `soul/dispatch.md`: la regla de entrada, la clasificación de tareas y el cierre con formato fijo.
- [ ] `README.md`: el manifiesto, menos de treinta líneas, entendible por alguien no técnico en menos de tres minutos.

**Terminado cuando:** el README se entiende sin contexto previo y la carpeta `soul/` describe el comportamiento completo sin nombrar ningún proyecto.

### Fase 3: El oficio

- [ ] Plantilla única de skill, con la misma estructura en todas.
- [ ] Entre ocho y doce skills escritas desde cero, una por área: depuración, despliegue, revisión de código, documentación veraz, investigación con fuentes primarias, seguridad adversarial, datos, interfaz, integración de modelos y control de coste.
- [ ] Cada skill con un ejemplo inventado y genérico, nunca adaptado de un caso real.

**Terminado cuando:** cada skill se puede leer sin saber nada del autor y enseña un procedimiento, no una anécdota.

### Fase 4: La prueba

- [ ] Batería corta de ocho a diez casos, ejecutable por cualquiera, que imprime un informe real con sus fallos.
- [ ] `install.sh` para tres herramientas, con verificación en tres pasos: identidad, listado y carga real.
- [ ] Un documento que explique al lector cómo comprobarlo él mismo en cinco minutos.

**Terminado cuando:** en una máquina limpia, instalar y verificar funciona de principio a fin y la batería imprime un informe con al menos un fallo real cazado.

### Fase 5: Publicación

- [ ] Pasar el repo a público.
- [ ] Releer el README en frío, como si no fuera propio.
- [ ] Revisar los enlaces de la web y retirar los que apunten a repos inexistentes.
- [ ] Prueba externa: que alguien ajeno siga las instrucciones sin ayuda.

**Terminado cuando:** un desconocido instala, verifica y entiende el método sin preguntar nada.

## 5. Qué no entra nunca

- Inventario de skills de la versión completa.
- Tabla comparativa entre la versión pública y la privada.
- Scripts de operación de proyectos reales.
- Estado de seguridad de un servidor concreto.
- Cifras de una máquina concreta (memoria, disco, antigüedad de las copias).
- Historial de git de la versión privada.
- Ejemplos reciclados y saneados.

## 6. Bitácora

- **2026-09-30.** Nace el proyecto. Repo creado en privado con este roadmap. Se descarta reaprovechar el intento anterior. Se decide empezar por la puerta y no por el contenido.

## 7. Cómo se actualiza este fichero

Al cerrar cada bloque de trabajo: marcar solo lo verificado, mover a la tabla de decisiones lo que cambie y con qué motivo, añadir una línea a la bitácora, y actualizar la fecha y la fase actual. Si una casilla lleva dos bloques sin poder marcarse, se escribe en la bitácora por qué.
