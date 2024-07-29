from Models.book import Book
from Models.user import User
from Models.author import Author
from Models.genre import Genre
from Database.db_connection import get_db_connection
import logging

class Library:
    def __init__(self):
        self.books = []
        self.users = []
        self.authors = []
        self.genres = []

    def add_book(self, title, author_name, isbn, pub_date, genre_name):
        # Check if author exists and get ID
        author_id = self.get_author_id(author_name)
        if not author_id:
            print(f"Author '{author_name}' not found. Please add the author first.")
            return

        # Check if genre exists and get ID
        genre_id = self.get_genre_id(genre_name)
        if not genre_id:
            print(f"Genre '{genre_name}' not found. Please add the genre first.")
            return

        new_book = Book(None, title, author_id, genre_id, isbn, pub_date, True)
        new_book.save_to_db()

    def get_author_id(self, author_name):
        connection = get_db_connection()
        cursor = connection.cursor()
        query = "SELECT id FROM authors WHERE name = %s"
        cursor.execute(query, (author_name,))
        result = cursor.fetchone()
        cursor.close()
        connection.close()
        if result:
            return result[0]
        return None

    def get_genre_id(self, genre_name):
        connection = get_db_connection()
        cursor = connection.cursor()
        query = "SELECT id FROM genres WHERE name = %s"
        cursor.execute(query, (genre_name,))
        result = cursor.fetchone()
        cursor.close()
        connection.close()
        if result:
            return result[0]
        return None

    def borrow_book(self, isbn, user_library_id):
        book = Book.find_by_isbn(isbn)
        user = User.find_by_library_id(user_library_id)
        if book and user and book.available:
            try:
                Book.borrow(book.isbn)
                User.borrow(user.id, book.id)  # use user.id instead of user.library_id
                return True, f"Book with ISBN '{isbn}' borrowed successfully by user '{user_library_id}'."
            except Exception as e:
                logging.error(f"Error borrowing book: {e}")
                return False, f"Error borrowing book: {e}"
        return False, f"Failed to borrow the book with ISBN '{isbn}'."

    def return_book(self, isbn, user_library_id):
        book = Book.find_by_isbn(isbn)
        user = User.find_by_library_id(user_library_id)
        if book and user:
            try:
                Book.return_book(book.isbn)
                User.return_book(user.id, book.id)  # use user.id instead of user.library_id
                return True, f"Book with ISBN '{isbn}' returned successfully by user '{user_library_id}'."
            except Exception as e:
                logging.error(f"Error returning book: {e}")
                return False, f"Error returning book: {e}"
        return False, f"Failed to return the book with ISBN '{isbn}'."

    def find_book_by_isbn(self, isbn):
        return Book.find_by_isbn(isbn)

    def display_all_books(self):
        connection = get_db_connection()
        cursor = connection.cursor()
        query = """
            SELECT b.title, a.name as author, g.name as genre, b.isbn, b.availability 
            FROM books b 
            JOIN authors a ON b.author_id = a.id 
            JOIN genres g ON b.genre_id = g.id
        """
        cursor.execute(query)
        books = cursor.fetchall()
        cursor.close()
        connection.close()
        
        for book in books:
            status = "Available" if book[4] else "Borrowed"
            print(f"Title: {book[0]}, Author: {book[1]}, Genre: {book[2]}, ISBN: {book[3]}, Status: {status}")

    # User operations
    def add_user(self, name, library_id):
        user = User(name, library_id)
        try:
            user.save_to_db()
            self.users.append(user)
            print(f"User '{name}' added.")
        except Exception as e:
            print(f"Error: {e}")
            print(f"User with library ID '{library_id}' already exists.")

    def find_user_by_id(self, library_id):
        return User.find_by_library_id(library_id)

    def display_all_users(self):
        connection = get_db_connection()
        cursor = connection.cursor()
        query = "SELECT * FROM users"
        cursor.execute(query)
        users = cursor.fetchall()
        cursor.close()
        connection.close()
        
        for user in users:
            print(f"Name: {user[1]}, Library ID: {user[2]}")

    # Author operations
    def add_author(self, name, biography):
        author = Author(name, biography)
        author.save_to_db()
        self.authors.append(author)
        return author

    def display_all_authors(self):
        connection = get_db_connection()
        cursor = connection.cursor()
        query = "SELECT * FROM authors"
        cursor.execute(query)
        authors = cursor.fetchall()
        cursor.close()
        connection.close()
        
        for author in authors:
            print(f"Name: {author[1]}, Biography: {author[2]}")

    # Genre operations
    def add_genre(self, name, description, category):
        genre = Genre(name, description, category)
        genre.save_to_db()
        self.genres.append(genre)
        return genre

    def display_all_genres(self):
        connection = get_db_connection()
        cursor = connection.cursor()
        query = "SELECT * FROM genres"
        cursor.execute(query)
        genres = cursor.fetchall()
        cursor.close()
        connection.close()
        
        for genre in genres:
            print(f"Name: {genre[1]}, Description: {genre[2]}, Category: {genre[3]}")

