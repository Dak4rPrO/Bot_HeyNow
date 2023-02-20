# Bot_HeyNow


Segundo dia y medio del proyecto/desafio ChatBot (En mi caso, bot para preguntar el clima).

(1) Rasa instalado, pero no del todo configurado.
(2) Tengo funcionando Rasa con la base de datos de MongoDB Atlas (todos mis datos estaran respaldados en la nube).

- Con este comando iniciaré el servidor de Rasa y habilitaré la API de Rasa para que pueda interactuar con el bot a través de solicitudes HTTP (Aun debo seguir invesatigando como enviarle las solicitudes)
rasa run --enable-api --cors "*" --debug

- Intentare fucionar todas las tecnologias para usar la interfaz de telegram

-------------------------------------------------------------------------------------+
RESET 

NUEVO PROYECTO RECICLANDO CODIGO DEL BOT ANTERIOR

INICIO DOMINGO 22:00 HS

bot-interfaz-base de datos de MongoDB Atlas-contraseñas y usuarios-!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

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