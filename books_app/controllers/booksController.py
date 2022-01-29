from flask import Flask, render_template, request, redirect
from books_app import app
from books_app.models import bookModel, authorModel, favoriteModel

@app.route('/books', methods=['GET'])
def books():
    books = bookModel.Book.get_all()
    return render_template('books.html', books = books)

@app.route('/create_book', methods=['POST'])
def create_book():
    data = {
        'title': request.form['title'],
        'pages': request.form['pages'],
    }

    bookModel.Book.save(data)
    return redirect('/books')

@app.route('/books/<int:id>', methods=['GET'])
def show_book(id):
    data = {
        'bookId': id
    }

    authors = authorModel.Author.get_all()
    book_with_fav_authors = bookModel.Book.get_authors_by_fav_book(data)

    if not type(book_with_fav_authors) == bookModel.Book:
        book_with_fav_authors = bookModel.Book.findById(data)
    
    return render_template('books-favorites.html', book_with_fav_authors = book_with_fav_authors, authors = authors)

@app.route('/add_favorite_author/<int:id>', methods=['POST'])
def add_favorite_author(id):
    data = {
        'bookId': id,
        'authorId': request.form['author'],
    }

    favoriteModel.Favorite.add_favorite(data)
    return redirect(f'/books/{id}')

