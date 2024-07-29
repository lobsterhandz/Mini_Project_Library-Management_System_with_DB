# Library Management System

## Overview

The Library Management System is a command-line-based application designed to streamline the management of books, users, authors, and genres within a library. This project demonstrates the use of Object-Oriented Programming (OOP) principles in Python, including encapsulation, inheritance, and polymorphism.

## Features

- **Book Operations:**
  - Add a new book
  - Borrow a book
  - Return a book
  - Search for a book
  - Display all books

- **User Operations:**
  - Add a new user
  - View user details
  - Display all users

- **Author Operations:**
  - Add a new author
  - View author details
  - Display all authors

- **Genre Operations:**
  - Add a new genre
  - View genre details
  - Display all genres

## Getting Started

### Prerequisites

- Python 3.x installed on your system.

### Installation

1. Clone the repository:
    ```bash
    git clone <repository_url>
    ```

2. Navigate to the project directory:
    ```bash
    cd library_management
    ```

### Usage

1. Run the application:
    ```bash
    python main.py
    ```

2. Follow the on-screen prompts to interact with the Library Management System.

## Project Structure

- `main.py`: Main script to run the application.
- `book.py`: Contains the `Book` class.
- `user.py`: Contains the `User` class.
- `author.py`: Contains the `Author` class.
- `genre.py`: Contains the `Genre` class.
- `library.py`: Contains the `Library` class with methods for managing books, users, authors, and genres.

# Library Management System with Database Integration

## Objective
Develop a robust Library Management System that integrates with a MySQL database to manage books, authors, genres, and users efficiently.

## Features
- Add, borrow, return, and search for books
- Manage users, authors, and genres
- User-friendly command-line interface
- Data persistence with MySQL

## Setup
1. Clone the repository:
    ```sh
    git clone https://github.com/lobsterhandz/Mini_Project_Library_Management_System.git
    cd Mini_Project_Library_Management_System
    ```

2. Set up the MySQL database:
    - Run the SQL scripts in `database/create_tables.sql` to create the necessary tables.
    - **Optional:** Run the `database/seed_data.sql` script to populate the database with initial data. This can be useful for testing and demonstration purposes.

3. Ensure you have Python installed (Python 3.6 or higher).

4. (Optional) Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

5. Install dependencies:
    ```sh
    pip install mysql-connector-python
    ```

## Usage
Run the `main.py` script:
```sh
python main.py

