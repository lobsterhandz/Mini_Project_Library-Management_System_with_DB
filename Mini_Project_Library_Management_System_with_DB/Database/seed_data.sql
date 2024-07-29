USE library_db;

-- Add initial data for authors
INSERT INTO authors (name, biography) VALUES ('J.K. Rowling', 'British author'), ('George R.R. Martin', 'American novelist');

-- Add initial data for genres
INSERT INTO genres (name, description, category) VALUES ('Fantasy', 'Fictional genre with magical elements', 'Fiction'), ('Science Fiction', 'Fictional genre dealing with futuristic concepts', 'Fiction');

-- Add initial data for books
INSERT INTO books (title, author_id, genre_id, isbn, publication_date, availability) VALUES ('Harry Potter and the Philosopher''s Stone', 1, 1, '9780747532743', '1997-06-26', 1), ('A Game of Thrones', 2, 1, '9780553103540', '1996-08-06', 1);

-- Add initial data for users
INSERT INTO users (name, library_id) VALUES ('Alice', 'U123'), ('Bob', 'U456');
