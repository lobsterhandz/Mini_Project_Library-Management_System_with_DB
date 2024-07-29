from Database.db_connection import get_db_connection
import mysql.connector

class Author:
    def __init__(self, name, biography):
        self.__name = name
        self.__biography = biography

    @property
    def name(self):
        return self.__name

    @property
    def biography(self):
        return self.__biography

    def save_to_db(self):
        connection = get_db_connection()
        cursor = connection.cursor()
        query = "INSERT INTO authors (name, biography) VALUES (%s, %s)"
        cursor.execute(query, (self.name, self.biography))
        connection.commit()
        cursor.close()
        connection.close()

    @classmethod
    def find_by_name(cls, name):
        connection = get_db_connection()
        cursor = connection.cursor()
        query = "SELECT * FROM authors WHERE name = %s"
        cursor.execute(query, (name,))
        author_data = cursor.fetchone()
        cursor.close()
        connection.close()
        if author_data:
            return cls(*author_data[1:])  # Assuming author_data[0] is the id
        return None
from Database.db_connection import get_db_connection
import logging

class Author:
    def __init__(self, id, name, biography):
        self.id = id
        self.name = name
        self.biography = biography

    def save_to_db(self):
        connection = get_db_connection()
        if not connection:
            logging.error("Failed to get database connection")
            return
        try:
            cursor = connection.cursor()
            query = "INSERT INTO authors (name, biography) VALUES (%s, %s)"
            cursor.execute(query, (self.name, self.biography))
            connection.commit()
            cursor.close()
            logging.debug(f"Author '{self.name}' saved to the database.")
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
            query = "SELECT * FROM authors WHERE name = %s"
            cursor.execute(query, (name,))
            author_data = cursor.fetchone()
            cursor.close()
            connection.close()
            if author_data:
                return cls(*author_data)
            return None
        except mysql.connector.Error as err:
            logging.error(f"Error: {err}")
            return None
