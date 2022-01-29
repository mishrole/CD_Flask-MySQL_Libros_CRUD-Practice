from flask import Flask, render_template, request, redirect
from books_app import app
from books_app.models import authorModel, bookModel, favoriteModel

@app.errorhandler(404)
def page_not_found(error):
    app.logger.error(error)
    return render_template('404.html'), 404

@app.route('/', methods=['GET'])
def index():
    return redirect('/authors')

@app.route('/authors', methods=['GET'])
def authors():
    authors = authorModel.Author.get_all()
    return render_template('authors.html', authors = authors)

@app.route('/create_author', methods=['POST'])
def create_author():
    data = {
        'name': request.form['name'],
    }

    authorModel.Author.save(data)
    return redirect('/authors')

@app.route('/authors/<int:id>', methods=['GET'])
def show_author(id):
    data = {
        'authorId': id
    }

    books = bookModel.Book.get_all()
    author_with_fav_books = authorModel.Author.get_fav_books_by_author(data)

    if not type(author_with_fav_books) == authorModel.Author:
        author_with_fav_books = authorModel.Author.findById(data)
        print(authorModel.Author.findById(data))

    return render_template('authors-favorites.html', author_with_fav_books = author_with_fav_books, books = books)

@app.route('/add_favorite_book/<int:id>', methods=['POST'])
def add_favorite_book(id):
    data = {
        'authorId': id,
        'bookId': request.form['book'],
    }

    favoriteModel.Favorite.add_favorite(data)
    return redirect(f'/authors/{id}')
