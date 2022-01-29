Create database books_schema;
use books_schema;

create table authors (
    id int primary key auto_increment,
    name varchar(45),
    created_at datetime,
    updated_at datetime
);

create table books (
    id int primary key auto_increment,
    title varchar(45),
    num_of_pages int,
    created_at datetime,
    updated_at datetime
);

create table favorites (
    author_id int not null,
    book_id int not null,
    primary key(author_id, book_id)
);

-- # Listar autores que no hayan sido marcados como favorito
-- SELECT DISTINCT * FROM authors
-- WHERE authors.id NOT IN (
-- SELECT * FROM (
-- SELECT DISTINCT authors.id FROM authors 
-- JOIN favorites ON authors.id = favorites.author_id 
-- JOIN books ON books.id = favorites.book_id 
-- WHERE book_id = 6
-- ) AS temp);