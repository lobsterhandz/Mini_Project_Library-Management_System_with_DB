import mysql.connector
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def get_db_connection():
    logging.debug('Getting database connection')
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Laserface2024$",
        database="LibraryDB"
    )
