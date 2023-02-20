""" File that contains only the function to connect to MongoDB Atlas """


def connect_mongodb():
    from pymongo import MongoClient
    """ Function to connect to MongoDB Atlas """

    client = MongoClient('mongodb+srv://MauriMiranda:perracamila24@\
                         firstchatbot-heynow.6bdrqe9.mongodb.net/test')
    db = client['Respaldo-de-datos']
    coleccion = db['Plataformas']
    return coleccion
