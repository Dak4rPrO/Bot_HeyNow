""" File that contains only the function to send the data to MongoDB Atlas """

from connect_mongodb import connect_mongodb


def save_date(city, temperature, description):
    """ function to save date in MongoDB Atlas """

    database = connect_mongodb()
    database.insert_one({
        'city': city, 'temperature': temperature, 'description': description
    })
