from Database.db_connection import get_db_connection
import logging
import mysql.connector

class Book:
    def __init__(self, id, title, author_id, genre_id, isbn, pub_date, available=True):
        self.id = id
        self.title = title
        self.author_id = author_id
        self.genre_id = genre_id
        self.isbn = isbn
        self.pub_date = pub_date
        self.available = available

    def save_to_db(self):
        connection = get_db_connection()
        if not connection:
            logging.error("Failed to get database connection")
            return
        try:
            cursor = connection.cursor()
            query = "INSERT INTO books (title, author_id, genre_id, isbn, publication_date, availability) VALUES (%s, %s, %s, %s, %s, %s)"
            cursor.execute(query, (self.title, self.author_id, self.genre_id, self.isbn, self.pub_date, self.available))
            connection.commit()
            cursor.close()
            logging.debug(f"Book '{self.title}' saved to the database.")
        except mysql.connector.Error as err:
            logging.error(f"Error: {err}")
        finally:
            connection.close()

    @classmethod
    def find_by_isbn(cls, isbn):
        connection = get_db_connection()
        if not connection:
            logging.error("Failed to get database connection")
            return None
        try:
            cursor = connection.cursor()
            query = "SELECT * FROM books WHERE isbn = %s"
            cursor.execute(query, (isbn,))
            book_data = cursor.fetchone()
            cursor.close()
            connection.close()
            if book_data:
                return cls(*book_data)
            return None
        except mysql.connector.Error as err:
            logging.error(f"Error: {err}")
            return None

    @classmethod
    def borrow(cls, isbn):
        connection = get_db_connection()
        if not connection:
            logging.error("Failed to get database connection")
            return
        try:
            cursor = connection.cursor()
            cursor.execute("START TRANSACTION")
            query = "SELECT availability FROM books WHERE isbn = %s FOR UPDATE"
            cursor.execute(query, (isbn,))
            availability = cursor.fetchone()[0]
            if availability == 0:
                cursor.execute("ROLLBACK")
                logging.error(f"Book with ISBN '{isbn}' is already borrowed.")
                return
            update_query = "UPDATE books SET availability = 0 WHERE isbn = %s"
            cursor.execute(update_query, (isbn,))
            cursor.execute("COMMIT")
            logging.debug(f"Book with ISBN '{isbn}' status set to borrowed in the database.")
        except mysql.connector.Error as err:
            cursor.execute("ROLLBACK")
            logging.error(f"Error: {err}")
        finally:
            cursor.close()
            connection.close()

    @classmethod
    def return_book(cls, isbn):
        connection = get_db_connection()
        if not connection:
            logging.error("Failed to get database connection")
            return
        try:
            cursor = connection.cursor()
            update_query = "UPDATE books SET availability = 1 WHERE isbn = %s"
            cursor.execute(update_query, (isbn,))
            connection.commit()
            cursor.close()
            logging.debug(f"Book with ISBN '{isbn}' status set to available in the database.")
        except mysql.connector.Error as err:
            logging.error(f"Error: {err}")
        finally:
            connection.close()
