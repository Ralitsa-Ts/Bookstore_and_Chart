"""
    This module ensures that the important functions of class Library from
    the module Library work as expected.
"""
import sys
import unittest
import os
parent = os.path.normpath(os.path.dirname(os.path.dirname(os.path.abspath
                         (__file__))) + "/model")
sys.path.append(parent)
from library import Library, Book

STORE = "store.txt"
BOOK = Book("Somewhere", "Steven Law", 2000, "Fantasy", 0.2, 3)
BOOK1 = Book("Birds", "John White", 2001, "Fantasy", 3.3, 15)
BOOK2 = Book("Birds", "Steve Tyler", 2011, "Thriller", 3.3, 15)
BOOK3 = Book("Never", "Steve Tyler", 2001, "Thriller", 3.5, 15)
BOOK4 = Book("Hello", "John White", 2010, "Thriller", 3.0, 10)

class LibraryTest(unittest.TestCase):
    def add_books(self, book_list, library):
        for book in book_list:
            library.add_book(book)

    def test_add_book(self):
        Library(STORE, ["Fantasy"])
        Library.add_book(BOOK)
        self.assertEqual([BOOK], Library.books)
        self.add_books([BOOK, BOOK1], Library)
        self.assertEqual([BOOK, BOOK1], Library.books)
        os.remove(os.path.realpath(STORE))

    def test_remove_book(self):
        Library(STORE, ["Fantasy", "Thriller"])
        self.add_books([BOOK, BOOK1, BOOK1], Library)
        Library.remove_book(BOOK)
        self.assertEqual([BOOK1], Library.books)
        Library.remove_book(BOOK)
        self.assertNotEqual([], Library.books)
        Library.remove_book(BOOK1)
        self.assertEqual([], Library.books)
        os.remove(os.path.realpath(STORE))

    def test_book_information_by_title(self):
        Library(STORE, ["Fantasy", "Thriller"])
        self.add_books([BOOK, BOOK1, BOOK2], Library)
        book_birds = Library.book_information_by_title("Birds")
        self.assertEqual([BOOK1, BOOK2], book_birds)
        book_somewhere = Library.book_information_by_title("Somewhere")
        self.assertEqual([BOOK], book_somewhere)
        self.assertEqual([], Library.book_information_by_title("Haha"))
        os.remove(os.path.realpath(STORE))

    def test_book_information_by_author(self):
        Library(STORE, ["Fantasy", "Thriller"])
        self.add_books([BOOK, BOOK1, BOOK2, BOOK3, BOOK4], Library)
        book_steven = Library.book_information_by_author("Steven Law")
        self.assertEqual([BOOK], book_steven)
        book_john = Library.book_information_by_author("John White")
        self.assertEqual([BOOK1, BOOK4], book_john)
        book_steve = Library.book_information_by_author("Steve Tyler")
        self.assertEqual([BOOK2, BOOK3], book_steve)
        self.assertEqual([], Library.book_information_by_author("Haha"))
        os.remove(os.path.realpath(STORE))

    def test_number_of_different_books(self):
        Library(STORE, ["Fantasy", "Thriller"])
        self.add_books([BOOK, BOOK1, BOOK2], Library)
        self.assertEqual(3, Library.number_of_different_books())
        Library.add_book(BOOK)
        self.assertEqual(3, Library.number_of_different_books())
        Library.remove_book(BOOK1)
        self.assertEqual(2, Library.number_of_different_books())
        os.remove(os.path.realpath(STORE))

    def test_number_of_books_by_genres(self):
        Library(STORE, ["Fantasy", "Thriller"])
        self.add_books([BOOK, BOOK1, BOOK2], Library)
        actual_result = Library.number_of_books_by_genres()
        self.assertEqual({'Fantasy': 2, 'Thriller': 1}, actual_result)
        Library.add_book(BOOK3)
        actual_result = Library.number_of_books_by_genres()
        self.assertEqual({'Fantasy': 2, 'Thriller': 2}, actual_result)
        Library.remove_book(BOOK1)
        actual_result = Library.number_of_books_by_genres()
        self.assertEqual({'Fantasy': 1, 'Thriller': 2}, actual_result)
        Library.remove_book(BOOK)
        actual_result = Library.number_of_books_by_genres()
        self.assertEqual({'Fantasy': 0, 'Thriller': 2}, actual_result)
        os.remove(os.path.realpath(STORE))

    def test_create_genre_dict(self):
        Library(STORE, ["Fantasy", "Thriller"])
        self.add_books([BOOK, BOOK1, BOOK2], Library)
        Library.create_genre_dict()
        expected_dict = {"Fantasy": [BOOK1, BOOK], "Thriller": [BOOK2]}
        self.assertEqual(expected_dict, Library.genre_dict)
        Library.add_book(BOOK3)
        expected_dict["Thriller"].append(BOOK3)
        self.assertEqual(expected_dict, Library.genre_dict)
        os.remove(os.path.realpath(STORE))

if __name__ == '__main__':
    unittest.main()
