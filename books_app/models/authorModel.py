from books_app.config.mysqlconnection import connectToMySQL
from books_app.models import bookModel

class Author:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.books = []

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM authors;"
        results = connectToMySQL('books_schema').query_db(query)

        authors = []

        for author in results:
            authors.append(cls(author))
        
        return authors

    @classmethod
    def findById(cls, data):
        query = "SELECT * FROM authors WHERE id = %(authorId)s;"
        results = connectToMySQL('books_schema').query_db(query, data)

        author = []

        if results:
            if len(results) > 0:
                author = results[0]

        return author

    @classmethod
    def save(cls, data):
        query = "INSERT INTO authors (name, created_at, updated_at) VALUES (%(name)s, NOW(), NOW())"
        return connectToMySQL('books_schema').query_db(query, data)

    @classmethod
    def get_fav_books_by_author(cls, data):
        query = "SELECT DISTINCT * from books JOIN favorites ON books.id = favorites.book_id JOIN authors ON authors.id = favorites.author_id WHERE author_id = %(authorId)s;"
        results = connectToMySQL('books_schema').query_db(query, data)

        author = []

        if results:
            if len(results) > 0:
                author = cls(results[0])

        for row_from_db in results:
            book_data = {
                'id': row_from_db['id'],
                'title': row_from_db['title'],
                'num_of_pages': row_from_db['num_of_pages'],
                'created_at': row_from_db['created_at'],
                'updated_at': row_from_db['updated_at']
            }

            author.books.append(bookModel.Book(book_data))

        return author

    # @classmethod
    # def add_favorite_book(data):
    #     query = "INSERT INTO favorites (author_id, book_id) VALUES (%(authorId)s, %(bookId)s);"
    #     return connectToMySQL('books_schema').query_db(query, data)