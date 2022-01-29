from books_app.config.mysqlconnection import connectToMySQL
from books_app.models import authorModel

class Book:
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.num_of_pages = data['num_of_pages']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.authors = []
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM books;"
        results = connectToMySQL('books_schema').query_db(query)
        books = []

        for book in results:
            books.append(cls(book))

        return books

    @classmethod
    def findById(cls, data):
        query = "SELECT * FROM books WHERE id = %(bookId)s;"
        results = connectToMySQL('books_schema').query_db(query, data)
        
        book = []

        if results:
            if len(results) > 0:
                book = results[0]

        return book

    @classmethod
    def save(cls, data):
        query = "INSERT INTO books (title, num_of_pages, created_at, updated_at) VALUES (%(title)s, %(pages)s, NOW(), NOW());"
        return connectToMySQL('books_schema').query_db(query, data)

    @classmethod
    def get_authors_by_fav_book(cls, data):
        query = "SELECT DISTINCT * FROM authors JOIN favorites ON authors.id = favorites.author_id JOIN books ON books.id = favorites.book_id WHERE book_id = %(bookId)s;"
        results = connectToMySQL('books_schema').query_db(query, data)

        book = []

        if results:
            if len(results) > 0:
                book = cls(results[0])

        for row_from_db in results:
            author_data = {
                'id': row_from_db['id'],
                'name': row_from_db['name'],
                'created_at': row_from_db['created_at'],
                'updated_at': row_from_db['updated_at']
            }

            book.authors.append(authorModel.Author(author_data))

        return book

    # @classmethod
    # def add_favorite_author(data):
    #     query = "INSERT INTO favorites (author_id, book_id) VALUES (%(authorId)s, %(bookId)s);"
    #     return connectToMySQL('books_schema').query_db(query, data)