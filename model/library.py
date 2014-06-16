"""
    This module contains a class named Library,which provides
    manipulating a virtual bookstore.
"""
import re

from book_database import Book, BookDataBase
STORAGE = "database.txt"
GENRES = ["Fantasy", "Drama", "Romance", "Thriller"]

class Library:

    @staticmethod
    def __init__(storage=None, genres=None):
        """
            Setting the basic information about the library.
            Keyword arguments:
                * storage - a file where the book record will be stored
                * genres - a list of possible genres
            We also extract all records from the file given and create a list
            of the books and get their amount.
        """
        if storage is None:
            Library.storage = STORAGE
        else:
            Library.storage = storage
        if genres is None:
            Library.genres = GENRES
        else:
            Library.genres = genres
        Library.database = BookDataBase(Library.storage)
        Library.books = Library.database.booklist()
        Library.number_of_books = len(Library.books)
        Library.create_genre_dict()


    @staticmethod
    def add_book(book):
        """
            Add a new book to the library.If it already exists then the number
            of copies of the existing book is increased.
        """
        Library.database.add_record(book)
        if book in Library.books:
            index = Library.books.index(book)
            new_copies = book.number_of_copies
            Library.books[index].increase_number_of_copies(new_copies)
        else:
            Library.books.append(book)
            Library.number_of_books += 1
            Library.genre_dict[book.genre].append(book)

    @staticmethod
    def remove_book(book):
        """
            Remove a book from the library if it exists.
        """
        if book in Library.books:
            Library.database.remove_record(book)
            Library.books.remove(book)
            Library.number_of_books -= 1
            Library.genre_dict[book.genre].remove(book)

    @staticmethod
    def book_information_by_title(title):
        """
            Returns a list of all books with the given title.
        """
        return [book for book in Library.books if re.search(title, book.title)]

    @staticmethod
    def book_information_by_author(author):
        """
            Returns a list of all books with the given author.
        """
        return [book for book in Library.books if
                re.search(author, book.author)]

    @staticmethod
    def number_of_different_books():
        """
            Return the number of different books in the library.
        """
        return Library.number_of_books

    @staticmethod
    def number_of_books_by_genres():
        """
            Returns a dictionary with keys - the possible genres and values -
            the amount of books in the corresponding genres.
        """
        return {genre: len(books) for genre, books in
                Library.genre_dict.items()}

    @staticmethod
    def create_genre_dict():
        """
            Creates a dictionary with keys - the possible genres and values -
            lists of books in the corresponding genres.
        """
        Library.genre_dict = dict()
        books = Library.books
        for genre in Library.genres:
            books_by_genre = [book for book in books if book.genre == genre]
            sorting = lambda x: x.title
            Library.genre_dict[genre] = sorted(books_by_genre, key=sorting)

    @staticmethod
    def remove_all_data():
        """
            Removes all records of books in the given storage.
        """
        pass

    @staticmethod
    def manipulation(book):
        remove_book(book)
        add_book(book)

    @staticmethod
    def return_book(book):
        """
            Returns a copy of the book back to the library.
        """
        book.increase_number_of_copies(1)
        manipulation(book)

    @staticmethod
    def take_book(book):
        """
            Takes a copy of the book from the library.
        """
        book.decrease_number_of_copies(1)
        manipulation(book)

    @staticmethod
    def like_book(book):
        """
            Increases the book's rating.
        """
        book.increase_rating()
        manipulation(book)

    @staticmethod
    def dislike_book(book):
        """
            Decreases the book's rating.
        """
        book.decrease_rating()
        manipulation(book)
