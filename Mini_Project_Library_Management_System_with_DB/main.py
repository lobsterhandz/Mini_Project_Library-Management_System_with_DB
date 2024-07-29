from Models.library import Library
from Utils.validation import validate_isbn, validate_user_id, validate_name, validate_date

def main():
    library = Library()

    while True:
        print("\nWelcome to the Library Management System!\n")
        print("Main Menu:")
        print("1. Book Operations")
        print("2. User Operations")
        print("3. Author Operations")
        print("4. Genre Operations")
        print("5. Quit")

        choice = input("Select an option: ")

        if choice == '1':
            book_operations(library)
        elif choice == '2':
            user_operations(library)
        elif choice == '3':
            author_operations(library)
        elif choice == '4':
            genre_operations(library)
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

def book_operations(library):
    while True:
        print("\nBook Operations:")
        print("1. Add a new book")
        print("2. Borrow a book")
        print("3. Return a book")
        print("4. Search for a book")
        print("5. Display all books")
        print("6. Back to Main Menu")

        choice = input("Select an option: ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            isbn = input("Enter book ISBN: ")
            pub_date = input("Enter publication date (YYYY-MM-DD): ")
            genre = input("Enter genre: ")
            if not validate_isbn(isbn):
                print("Invalid ISBN format. Please try again.")
                continue
            if not validate_date(pub_date):
                print("Invalid date format. Please try again.")
                continue
            library.add_book(title, author, isbn, pub_date, genre)
        elif choice == '2':
            isbn = input("Enter book ISBN: ")
            if not validate_isbn(isbn):
                print("Invalid ISBN format. Please try again.")
                continue
            user_id = input("Enter user ID: ")
            if not validate_user_id(user_id):
                print("Invalid user ID format. Please try again.")
                continue
            success, message = library.borrow_book(isbn, user_id)
            print(message)
        elif choice == '3':
            isbn = input("Enter book ISBN: ")
            if not validate_isbn(isbn):
                print("Invalid ISBN format. Please try again.")
                continue
            user_id = input("Enter user ID: ")
            if not validate_user_id(user_id):
                print("Invalid user ID format. Please try again.")
                continue
            success, message = library.return_book(isbn, user_id)
            print(message)
        elif choice == '4':
            isbn = input("Enter book ISBN: ")
            if not validate_isbn(isbn):
                print("Invalid ISBN format. Please try again.")
                continue
            book = library.find_book_by_isbn(isbn)
            if book:
                status = "Available" if book.available else "Borrowed"
                print(f"Title: {book.title}, Author: {book.author}, ISBN: {book.isbn}, Status: {status}")
            else:
                print("Book not found.")
        elif choice == '5':
            library.display_all_books()
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

def user_operations(library):
    while True:
        print("\nUser Operations:")
        print("1. Add a new user")
        print("2. View user details")
        print("3. Display all users")
        print("4. Back to Main Menu")

        choice = input("Select an option: ")

        if choice == '1':
            name = input("Enter user name: ")
            user_id = input("Enter library ID: ")
            if not validate_user_id(user_id):
                print("Invalid user ID format. Please try again.")
                continue
            library.add_user(name, user_id)
        elif choice == '2':
            user_id = input("Enter library ID: ")
            if not validate_user_id(user_id):
                print("Invalid user ID format. Please try again.")
                continue
            user = library.find_user_by_id(user_id)
            if user:
                print(f"Name: {user.name}, Library ID: {user.library_id}")
                user.display_borrowed_books()
            else:
                print("User not found.")
        elif choice == '3':
            library.display_all_users()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

def author_operations(library):
    while True:
        print("\nAuthor Operations:")
        print("1. Add a new author")
        print("2. Display all authors")
        print("3. Back to Main Menu")

        choice = input("Select an option: ")

        if choice == '1':
            name = input("Enter author name: ")
            biography = input("Enter author biography: ")
            if not validate_name(name):
                print("Invalid author name. Please try again.")
                continue
            success, message = library.add_author(name, biography)
            print(message)
        elif choice == '2':
            library.display_all_authors()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

def genre_operations(library):
    while True:
        print("\nGenre Operations:")
        print("1. Add a new genre")
        print("2. Display all genres")
        print("3. Back to Main Menu")

        choice = input("Select an option: ")

        if choice == '1':
            name = input("Enter genre name: ")
            description = input("Enter genre description: ")
            category = input("Enter genre category: ")
            if not validate_name(name):
                print("Invalid genre name. Please try again.")
                continue
            success, message = library.add_genre(name, description, category)
            print(message)
        elif choice == '2':
            library.display_all_genres()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
