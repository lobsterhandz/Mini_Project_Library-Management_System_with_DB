from Database.db_connection import get_db_connection
import logging

class User:
    def __init__(self, name, library_id, id=None):
        self.name = name
        self.library_id = library_id
        self.id = id  # added id to the constructor

    def save_to_db(self):
        connection = get_db_connection()
        cursor = connection.cursor()
        query = "INSERT INTO users (name, library_id) VALUES (%s, %s)"
        cursor.execute(query, (self.name, self.library_id))
        connection.commit()
        cursor.close()
        connection.close()

    @classmethod
    def find_by_id(cls, user_id):
        connection = get_db_connection()
        cursor = connection.cursor()
        query = "SELECT * FROM users WHERE id = %s"
        cursor.execute(query, (user_id,))
        user_data = cursor.fetchone()
        cursor.close()
        connection.close()
        if user_data:
            return cls(user_data[1], user_data[2], user_data[0])  # pass id as well
        return None

    @classmethod
    def find_by_library_id(cls, library_id):
        connection = get_db_connection()
        cursor = connection.cursor()
        query = "SELECT * FROM users WHERE library_id = %s"
        cursor.execute(query, (library_id,))
        user_data = cursor.fetchone()
        cursor.close()
        connection.close()
        if user_data:
            return cls(user_data[1], user_data[2], user_data[0])  # pass id as well
        return None

    @staticmethod
    def borrow(user_id, book_id):
        connection = get_db_connection()
        cursor = connection.cursor()
        query = "INSERT INTO borrowed_books (user_id, book_id, borrow_date) VALUES (%s, %s, CURDATE())"
        try:
            cursor.execute(query, (user_id, book_id))
            connection.commit()
        except Exception as e:
            logging.error(f"Error borrowing book: {e}")
            raise
        finally:
            cursor.close()
            connection.close()

    @staticmethod
    def return_book(user_id, book_id):
        connection = get_db_connection()
        cursor = connection.cursor()
        query = "UPDATE borrowed_books SET return_date = CURDATE() WHERE user_id = %s AND book_id = %s AND return_date IS NULL"
        try:
            cursor.execute(query, (user_id, book_id))
            connection.commit()
        except Exception as e:
            logging.error(f"Error returning book: {e}")
            raise
        finally:
            cursor.close()
            connection.close()

    def display_borrowed_books(self):
        connection = get_db_connection()
        cursor = connection.cursor()
        query = """
            SELECT b.title, bb.borrow_date, bb.return_date 
            FROM borrowed_books bb 
            JOIN books b ON bb.book_id = b.id 
            WHERE bb.user_id = %s
        """
        cursor.execute(query, (self.id,))
        books = cursor.fetchall()
        cursor.close()
        connection.close()

        for book in books:
            return_date = book[2] if book[2] else "Not returned"
            print(f"Title: {book[0]}, Borrowed on: {book[1]}, Returned on: {return_date}")

