from books_app import app
from books_app.controllers import authorsController, booksController

if __name__ == '__main__':
    app.run( debug = True, port = 8091 )