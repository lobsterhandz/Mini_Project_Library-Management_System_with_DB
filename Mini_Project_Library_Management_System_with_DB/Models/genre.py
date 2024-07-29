from Database.db_connection import get_db_connection
import logging
import mysql.connector

class Genre:
    def __init__(self, id, name, description, category):
        self.id = id
        self.name = name
        self.description = description
        self.category = category

    def save_to_db(self):
        connection = get_db_connection()
        if not connection:
            logging.error("Failed to get database connection")
            return
        try:
            cursor = connection.cursor()
            query = "INSERT INTO genres (name, description, category) VALUES (%s, %s, %s)"
            cursor.execute(query, (self.name, self.description, self.category))
            connection.commit()
            cursor.close()
            logging.debug(f"Genre '{self.name}' saved to the database.")
        except mysql.connector.Error as err:
            logging.error(f"Error: {err}")
        finally:
            connection.close()

    @classmethod
    def find_by_name(cls, name):
        connection = get_db_connection()
        if not connection:
            logging.error("Failed to get database connection")
            return None
        try:
            cursor = connection.cursor()
            query = "SELECT * FROM genres WHERE name = %s"
            cursor.execute(query, (name,))
            genre_data = cursor.fetchone()
            cursor.close()
            connection.close()
            if genre_data:
                return cls(*genre_data)
            return None
        except mysql.connector.Error as err:
            logging.error(f"Error: {err}")
            return None
