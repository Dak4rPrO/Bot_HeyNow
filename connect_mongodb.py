""" File that contains only the function to connect to MongoDB Atlas """

from pymongo import MongoClient


def connect_mongodb():
    """ Function to connect to MongoDB Atlas """

    server = MongoClient('mongodb+srv://MauriMiranda:perracamila24@\
                         firstchatbot-heynow.6bdrqe9.mongodb.net/test')
    db = server['climate']
    database = db['climate']
    return database
