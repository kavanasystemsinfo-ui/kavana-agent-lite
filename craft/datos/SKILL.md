# Datos

## Cuándo se usa
Cuando el sistema guarda, lee, transforma o mueve información que importa. Señales: tabla nueva, migración, ETL, caché, exportación, sincronización entre servicios.

## Qué resuelve
Evita que los datos se corrompan, se pierdan o mientan. Un fallo de lógica se arregla volviendo a desplegar; un dato malo persiste hasta que alguien lo limpia a mano.

## Procedimiento

1. **Declarar el esquema.** Cada tabla, colección o mensaje tiene un contrato escrito: campos, tipos, nulos, claves, unicidad. Lo que no está en el contrato no existe.
2. **Validar a la entrada.** Antes de persistir, el dato pasa por el validador del esquema. Un `null` en campo obligatorio niega la escritura, no la arruina.
3. **Migraciones reversibles.** Cada cambio de esquema tiene su `down`. Si no se puede revertir en 5 minutos, el cambio no entra.
4. **Índices por consulta.** Un índice se crea porque una consulta real lo necesita, no por anticipación. El índice que no usan las consultas solo frena escrituras.
5. **Transacciones por invariante.** Si dos escrituras deben ocurrir juntas o ninguna, van en la misma transacción. La consistencia eventual se documenta y se mide.
6. **Borrado lógico, no físico.** Un registro se marca `eliminado_en`, no se borra. La consulta por defecto filtra ese campo; la auditoría lo agradece.
7. **Comprobar la integridad.** Un job periódico recorre las claves foráneas, unicidades y rangos declarados. Lo que no cuadre, alerta.

## Errores que evita
- Clave foránea rota porque se borró el padre sin revisar hijos.
- Duplicado silencioso porque faltaba unicidad en el índice.
- Migración que deja la base a medias y no hay forma de volver atrás.
- Consulta que tarda 30 segundos porque nadie creó el índice que pedía.
- Dato sensible en log porque se serializó la entidad entera.

## Cómo se comprueba
La suite de integridad recorre el esquema declarado y reporta cero violaciones. Una migración de prueba aplica y revierte en una base limpia sin errores.