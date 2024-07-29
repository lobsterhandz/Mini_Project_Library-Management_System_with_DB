# test_connection.py
from Database.db_connection import get_db_connection

def test_connection():
    try:
        connection = get_db_connection()
        if connection.is_connected():
            print("Successfully connected to the database")
            connection.close()
    except mysql.connector.Error as err:
        print(f"Error: {err}")

if __name__ == "__main__":
    test_connection()
