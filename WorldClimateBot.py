from telethon import TelegramClient, events
import apiData
from datetime import datetime


def connect_mongodb():
    from pymongo import MongoClient
    """ Function to connect to MongoDB Atlas """

    client = MongoClient('mongodb+srv://MauriMiranda:perracamila24@\
                         firstchatbot-heynow.6bdrqe9.mongodb.net/test')
    db = client['Respaldo-de-datos']
    coleccion = db['Plataformas']
    return coleccion


client = TelegramClient('session', apiData.api_id, apiData.api_hash)

@client.on(events.NewMessage(chats=apiData.chatName))

async def my_event_handler(event):
  
  data = {
    'user_id': event.sender_id,
    'text': event.text,
    }

  print(event.text)
  respuesta = event.text

  if not respuesta:
    await client.send_message(apiData.chatName, "No se pudo procesar su solicitud.")
    
  coleccion = connect_mongodb()
  result = coleccion.insert_one(data)
  if result.inserted_id:
    print("Mensaje guardado en la base de datos")
  else:
    print("No se pudo guardar el mensaje en la base de datos")
  
  if respuesta == '/start':
    await client.send_message(apiData.chatName, "Hola, bienvenido al bot de prueba.\
    \n\nEscribe /help para ver los comandos disponibles.")
  if respuesta == '/help':
    await client.send_message(apiData.chatName, "Comandos disponibles:\
    \n\n/start: Inicia el bot\
    \n/help: Muestra los comandos disponibles\
    \n/guardar: Guardar los datos de usuario y contraseña\
    \n/mirar: Ver los datos guardados\
    \n/borrar: Borrar los datos guardados")
    
  plataforma = event.text
  coleccion = connect_mongodb()
  
  coleccion.insert_one({
        'user_id': event.sender_id,
        'plataforma': {
            plataforma: {
                'usuario': event.text
            }
        }
    })


client.start()
client.run_until_disconnected()

