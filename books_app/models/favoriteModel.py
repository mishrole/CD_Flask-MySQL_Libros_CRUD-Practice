from books_app.config.mysqlconnection import connectToMySQL

class Favorite:

    @staticmethod
    def add_favorite(data):
        query = "INSERT INTO favorites (author_id, book_id) VALUES (%(authorId)s, %(bookId)s);"
        return connectToMySQL('books_schema').query_db(query, data)