# Configuración y secretos

## Cuándo se usa
Cuando el sistema necesita valores que cambian por entorno: claves de API, DSN de base de datos, feature flags, timeouts, URLs de proveedores, certificados.

## Qué resuelve
Elimina "funciona en mi máquina" y "la clave está en el repo". Configuración y secretos fuera del código, versionados por entorno, rotables sin despliegue.

## Procedimiento

1. **Doce factores: config en entorno.** Código lee `os.getenv("DATABASE_URL")`, `os.getenv("OPENAI_API_KEY")`. Ningún valor sensible en código, ni en `.env` commiteado, ni en imagen Docker.
2. **Esquema de configuración.** Clase/estructura que valida al arranque: tipos, requeridos, rangos, valores por defecto solo para no sensibles. Falla rápido si falta algo.
3. **Secretos en gestor dedicado.** Vault, AWS Secrets Manager, 1Password CLI, Doppler, SOPS+age. El secreto nunca toca disco en texto plano. El contenedor lo recibe en memoria al iniciar.
4. **Entornos aislados.** Desarrollo, staging, producción = conjuntos de secretos distintos. Ningún secreto de producción en máquina de desarrollador.
5. **Feature flags como config.** `FF_NUEVO_PAGO=true` en entorno. Código: `if config.ff_nuevo_pago: ...`. Sin flag = camino viejo. Rollback = cambiar variable, no código.
6. **Rotación sin redeploy.** El gestor inyecta versión nueva; la app recarga en caliente (SIGHUP, watcher, TTL cache). Clave rotada = clave vieja invalidada en < 5 min.
7. **Auditoría de acceso.** Quién leyó qué secreto y cuándo. Alerta si secreto de producción se lee desde IP no reconocida o fuera de ventana de despliegue.

## Errores que evita
- Clave de producción en GitHub porque alguien hizo `echo $API_KEY > .env` y commit.
- Despliegue roto porque `DATABASE_URL` faltaba en staging y nadie lo validó al arranque.
- Incidente de 2 horas rotando clave porque la app no recarga sin reinicio.
- Feature flag hardcodeada en `if (false)` que nadie encuentra al hacer rollback.
- Secreto compartido entre entornos: fuga en dev = comprometido en prod.

## Cómo se comprueba
Arranca la app en entorno limpio solo con variables de entorno inyectadas por el gestor. Verifica: arranca en < 10 s, schema valida todo, rota un secreto y la app lo usa sin reinicio, auditoría registra la lectura, cero secretos en imagen Docker (`docker save | grep -i secret`).