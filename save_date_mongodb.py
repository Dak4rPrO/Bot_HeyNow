""" File that contains only the function to send the data to MongoDB Atlas """

from connect_mongodb import connect_mongodb


def save_date(city, temperature, description):
    """ function to save date in MongoDB Atlas """

    plataforma = event.text
    database = connect_mongodb()
    
    database.insert_one(userid = {
        plataforma: {
            'clave21': 'valor21',
            'clave22': 'valor22'
        }
    })
    