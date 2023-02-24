# Bot_HeyNow  

RE-INICIO JUEVES 14:30 HS (UN DIA PARA TERMINAR)  
  
Primera idea de como serian las iteraciones:

(1) /guardar  
(2) /mirar  
(3) /borrar  
  
(1) /guardar  
usuario: action: /guardar  
bot: msg: "Por favor, indique una plataforma"  
usuario: msg: "Facebook"  
bot: msg: "Indique usuario"  
usuario: msg: "nuevousuario1"  
bot: msg: "Indique contraseña"  
usuario: msg: "contraseña1234"  
bot: msg: "Datos registrados con exito"  
bot: msg: "Para ver los datos escriba */mirar*  
  
(2) /mirar  
usuario: action: /mirar  
bot: msg: "Ingrese la plataforma que desea ver"  
usuario: msg: "Instagram"  
bot: msg: "Estas son todas sus cuentas registradas"  
bot: Usuario: abcd_1  
     Contraseña: aqweasd1  
     Usuario: qwer_2  
     Contraseña: zxcvb2  
  
(3) /borrar  
usuario: action: /borrar  
bot: msg: "Ingrese una plataforma"  
usuario: msg: "Instagram"  
bot: msg: "Estas son todas sus cuentas registradas"  
bot: Usuario: abcd_1  
     Contraseña: aqweasd1  
     Usuario: qwer_2  
     Contraseña: zxcvb2  
bot: msg: "Seleccione el usuario que desea borrar"  
usuario: msg "qwer_2"  
bot: msg: "Usuario y contraseña eliminados"

----------------------------------------------------------------

Al final termine agragando mas funciones, estas son:

Comandos disponibles:
    
/start: Inicia el bot y crea una nueva colección en la base de datos.

/insertar <coleccion>: Crea la colección indicada.         
/insertar <coleccion>, <username> <contraseña>: De esta manera creara una coleccion (aunque no esta creada) e insertara un usuario y contraseña en ella.

/listar: Muestra las colecciones existentes en la base de datos.

/mostrar <coleccion>: Muestra todos los usuarios y contraseñas almacenados en la colección indicada.

/borrar <coleccion>: Borra la colección indicada. La colección debe estar vacía.

/quitar <coleccion>, <usuario>: Indicando el usuario de una coleccion, borrara todos sus datos.

/help: Muestra los comandos disponibles.

----------------------------------------------------------------

- Todas los comandos funcionan como Dios manda.
- No estan testeados al 100%, podrian mejorar.
- Al final las iteraciones usuario-bot se hacen desde el mismo apartado de mensajes del usuario.
- Por alguna razon que no encontre, el bot solo funciona en dispositivos enlazados a mi cuenta de Telegram.
- Solo use Python, Telegram, Mongodb Atlas y Microsoft Azure.
- A pesar de que lo intente por todo 1 dia, no pude correr el bot en un servidor web.
- Si le hubiera podido dedicar todos los dias, me gustaria haber probado enlazar GPT3 al bot, y tambien una api del clima (mis 3 principales ideas del bot en 1).
- Solo vi 2 video tutoriales, documentacion de pymongo, telethon y Microsoft (esta ultima no me sirvio de nada), extenciones de Visual Code supieron ayudar, y por ultimo pero no menos importante, chatgpt para debuguear.
