import apiData
from datetime import datetime
from telethon import TelegramClient, events
from pymongo import MongoClient

# CONEXION A MONGODB ATLAS
clientMongodb = MongoClient('mongodb+srv://MauriMiranda:*******@\
							firstchatbot-heynow.6bdrqe9.mongodb.net/test')
db = clientMongodb['Respaldo-de-datos']

# CONEXION AL BOT DE TELEGRAM
clientTelegram = TelegramClient('session', apiData.api_id, apiData.api_hash)


@clientTelegram.on(events.NewMessage(chats=apiData.chatName))
async def my_bot(event):
	
	user_id = event.sender_id
	text = event.text.strip()
	
	# PRINT PARA DEBUGUEAR EN CONSOLA
	print(event.text)

	# MANEJO DE COMANDOS
	if text.startswith('/'):
		# COMANDO DE INICIO
		if text == '/start':

			start = "Hola, bienvenido al bot de prueba. Escribe /help para ver \
los comandos disponibles."

			await clientTelegram.send_message(apiData.chatName, f"{start}")

		# COMANDO DE AYUDA
		elif text == '/help':

			help_text = "Comandos disponibles:\n"

			help_start = "\n/start: Inicia el bot y crea una nueva colección en \
la base de datos.\n"

			help_insertar = "\n/insertar <coleccion>: Crea la colección indicada.\
						   \n/insertar <coleccion>, <username> <contraseña>: \
De esta manera creara una coleccion (aunque no esta \
creada) e insertara un usuario y contraseña en \
ella.\n"

			help = "\n/help: Muestra los comandos disponibles."

			help_listar = "\n/listar: Muestra las colecciones existentes en la \
base de datos.\n"

			help_mostrar = "\n/mostrar <coleccion>: Muestra todos los usuarios y \
contraseñas almacenados en la colección indicada.\n"

			help_borrar = "\n/borrar <coleccion>: Borra la colección indicada\
. La colección debe estar vacía.\n"

			help_quitar = "\n/quitar <coleccion>, <usuario>: Indicando el \
usuario de una coleccion, borrara todos sus datos.\n"

			await clientTelegram.send_message(apiData.chatName, f"{help_text}\
				{help_start}{help_insertar}{help_listar}{help_mostrar}{help_borrar}{help_quitar}{help}")

		# LISTAR TODAS LAS COLECCIONES
		elif text == '/listar':
			# Obtener una lista de todas las colecciones en la base de datos.
			collections = db.list_collection_names()
			# Crear un mensaje que contenga la lista de colecciones.
			message = "Colecciones en la base de datos:\n\n"
			message += "\n".join(collections)
			# Enviar el mensaje al chat de Telegram.
			await clientTelegram.send_message(apiData.chatName, message)
		
		# MOSTRAR DATOS DE COLECCIONES
		elif text.startswith('/mostrar '):
			coleccion_name = text[9:].strip()
			coleccion = db.get_collection(coleccion_name)

			if coleccion_name not in db.list_collection_names():
				await clientTelegram.send_message(apiData.chatName, f'La colección "{coleccion_name}" no existe.')
			else:
				# Obtener todos los documentos de la colección.
				documentos = coleccion.find()
				# Crear un mensaje que contenga la lista de usuarios y contraseñas.
				message = f"Usuarios y contraseñas en la colección {coleccion_name}:\n\n"
				for documento in documentos:
					message += f"User: {documento['usuario']} | Clave: {documento['contraseña']}\n"
				# Enviar el mensaje al chat de Telegram.
				await clientTelegram.send_message(apiData.chatName, message)

		# GUARDAR COLECCION E INSERTAR DATOS EN COLECCION
		elif text.startswith('/insertar '):
			command_parts = text[10:].split(',', 1)
			coleccion_name = command_parts[0]
			coleccion = db.get_collection(coleccion_name)

			if len(command_parts) == 1:
				# Si el comando solo contiene el nombre de la colección,
				# verifica si la colección existe y si no, crea la colección.
				if coleccion_name in db.list_collection_names():
					await clientTelegram.send_message(apiData.chatName, f"La colección {coleccion_name} ya existe. Para insertar datos, utiliza el siguiente formato: /insertar {coleccion_name}, usuario, contraseña")
				else:
					db.create_collection(coleccion_name)
					await clientTelegram.send_message(apiData.chatName, f"La colección {coleccion_name} no existía y ha sido creada. Para insertar datos, utiliza el siguiente formato: /insertar {coleccion_name}, usuario, contraseña")
			else:
				# Insertamos los datos en la colección.
				if coleccion:
					usuario, contraseña = command_parts[1].strip().split(' ')
					data = {
						'user_id': user_id,
						'usuario': usuario,
						'contraseña': contraseña,
						'timestamp': datetime.now(),
						}
					coleccion.insert_one(data)
					await clientTelegram.send_message(apiData.chatName, f"Usuario y contraseña insertados en la colección {coleccion_name}.")

		# BORRAR COLECCION
		elif text.startswith('/borrar '):
			coleccion_name = text[8:].strip()
			coleccion = db.get_collection(coleccion_name)

			if coleccion_name not in db.list_collection_names():
				await clientTelegram.send_message(apiData.chatName, f'La colección "{coleccion_name}" no existe.')
			else:
				# Verificar si la colección está vacía.
				if coleccion.estimated_document_count() == 0:
					# Borrar la colección.
					db.drop_collection(coleccion_name)
					await clientTelegram.send_message(apiData.chatName, f'La colección "{coleccion_name}" ha sido borrada.')
				else:
					await clientTelegram.send_message(apiData.chatName, f'La colección "{coleccion_name}" no está vacía y no puede ser borrada.')

		# QUITAR DATOS DE UNA COLECCION
		elif text.startswith('/quitar '):
			command_parts = text[8:].split(',', 1)
			coleccion_name = command_parts[0]
			coleccion = db.get_collection(coleccion_name)

			if coleccion_name not in db.list_collection_names():
				await clientTelegram.send_message(apiData.chatName, f'La colección "{coleccion_name}" no existe.')
			else:
				if coleccion.count_documents({}) == 0:
					await clientTelegram.send_message(apiData.chatName, f'La colección "{coleccion_name}" está vacía.')
				elif len(command_parts) != 2:
					await clientTelegram.send_message(apiData.chatName, f'Para quitar datos de la colección "{coleccion_name}", utiliza el siguiente formato: /quitar {coleccion_name}, usuario')
				else:
					usuario = command_parts[1].strip()
					data = coleccion.find_one({'usuario': usuario})
					if data is None:
						await clientTelegram.send_message(apiData.chatName, f'El usuario "{usuario}" no existe en la colección "{coleccion_name}".')
					else:
						coleccion.delete_one({'usuario': usuario})
						await clientTelegram.send_message(apiData.chatName, f"Usuario y contraseña borrados de la colección {coleccion_name}.")

		# COMANDO NO VALIDO
		else:
			await clientTelegram.send_message(apiData.chatName, "Comando no válido. Escribe /help para ver los comandos disponibles y la sintaxis correcta.")


clientTelegram.start()
clientTelegram.run_until_disconnected()
