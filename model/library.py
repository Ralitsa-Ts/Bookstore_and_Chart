"""
    This module contains a class named Library,which provides
    manipulating a virtual bookstore.
"""
from book_database import Book, BookDataBase
import re


class Library:

    def __init__(self, storage, genres):
        """
            Setting the basic information about the library.
            Keyword arguments:
                * storage - a file where the book record will be stored
                * genres - a list of possible genres
            We also extract all records from the file given and create a list
            of the books and get their amount.
        """
        self.storage = storage
        self.genres = genres
        self.database = BookDataBase(self.storage)
        self._books = self.database.booklist()
        self.number_of_books = len(self._books)
        self.create_genre_dict()

    @property
    def books(self):
        """
            Getting the list of books in the library.
        """
        return self._books

    def add_book(self, book):
        """
            Add a new book to the library.If it already exists then the number
            of copies of the existing book is increased.
        """
        self.database.add_record(book)
        if book in self._books:
            index = self._books.index(book)
            new_copies = book.number_of_copies
            self._books[index].increase_number_of_copies(new_copies)
        else:
            self._books.append(book)
            self.number_of_books += 1
            self.genre_dict[book.genre].append(book)

    def remove_book(self, book):
        """
            Remove a book from the library if it exists.
        """
        if book in self._books:
            self.database.remove_record(book)
            self._books.remove(book)
            self.number_of_books -= 1
            self.genre_dict[book.genre].remove(book)

    def book_information_by_title(self, title):
        """
            Returns a list of all books with the given title.
        """
        return [book for book in self._books if re.search(title, book.title)]

    def book_information_by_author(self, author):
        """
            Returns a list of all books with the given author.
        """
        return [book for book in self._books if re.search(author, book.author)]

    def number_of_different_books(self):
        """
            Return the number of different books in the library.
        """
        return self.number_of_books

    def number_of_books_by_genres(self):
        """
            Returns a dictionary with keys - the possible genres and values -
            the amount of books in the corresponding genres.
        """
        return {genre: len(books) for genre, books in self.genre_dict.items()}

    def create_genre_dict(self):
        """
            Creates a dictionary with keys - the possible genres and values -
            lists of books in the corresponding genres.
        """
        self.genre_dict = dict()
        books = self._books
        for genre in self.genres:
            books_by_genre = [book for book in books if book.genre == genre]
            sorting = lambda x: x.title
            self.genre_dict[genre] = sorted(books_by_genre, key=sorting)

    def remove_all_data(self):
        """
            Removes all records of books in the given storage.
        """
        pass

    def return_book(self, book):
        """
            Returns a copy of the book back to the library.
        """
        book.increase_number_of_copies(1)
        remove_book(book)
        add_book(book)

    def take_book(self, book):
        """
            Takes a copy of the book from the library.
        """
        book.decrease_number_of_copies(1)
        remove_book(book)
        add_book(book)
