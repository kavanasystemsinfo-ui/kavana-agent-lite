# Interfaz

## Cuándo se usa
Cuando alguien usa el sistema: página, formulario, botón, menú, notificación, error visible, carga, respuesta táctil.

## Qué resuelve
Que la persona haga lo que vino a hacer sin adivinar, sin esperar y sin romperse. Una interfaz que exige instrucciones es una interfaz que falla.

## Procedimiento

1. **Un objetivo por pantalla.** Qué decide o consigue el usuario aquí. Si hay dos, son dos pantallas.
2. **Estado visible siempre.** Cargando, vacío, error, éxito, guardando. Ningún estado se queda en "no pasa nada".
3. **Entrada perdonable.** El usuario escribe mal, pulsa dos veces, recarga, vuelve atrás. El sistema no explota ni duplica.
4. **Acción primaria evidente.** El botón principal tiene el verbo de la acción ("Guardar", "Enviar", "Confirmar"). No "Aceptar" genérico.
5. **Feedback en 100 ms.** Click → cambio visual. Petición → indicador. Sin respuesta percibida, el usuario repite.
6. **Error accionable.** "Fallo de servidor" no sirve. "El correo ya existe, usa recupera contraseña" sí. El mensaje dice qué hacer.
7. **Accesible por defecto.** Contraste, foco visible, etiquetas en inputs, orden de tabulación, texto alternativo. No es opcional, es la base.

## Errores que evita
- Usuario envía tres veces el formulario porque no vio que se enviaba.
- Pantalla en blanco 5 segundos sin indicador de carga.
- Error "400 Bad Request" mostrado tal cual al usuario.
- Botón "Eliminar" al lado de "Guardar" sin confirmación distinta.
- Formulario que pierde lo escrito al recargar por un fallo de validación.

## Cómo se comprueba
Recorrido manual de los 5 flujos principales: cada uno llega a su objetivo, muestra estado en cada paso, recupera de error y se navega solo con teclado.