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


class LibraryTest(unittest.TestCase):
    def setUp(self):
        self.store = "store.txt"
        self.books = [Book("Somewhere", "Steve Law", 2000, "Fantasy", 0.2, 3),
                      Book("Birds", "John White", 2001, "Fantasy", 3.3, 15),
                      Book("Birds", "Steve Tyler", 2011, "Thriller", 3.3, 15),
                      Book("Never", "Steve Tyler", 2001, "Thriller", 3.5, 15),
                      Book("Hello", "John White", 2010, "Thriller", 3.0, 10)]

    def add_books(self, book_list, library):
        for book in book_list:
            library.add_book(book)

    def test_add_book(self):
        Library(self.store, ["Fantasy"])
        Library.add_book(self.books[0])
        self.assertEqual([self.books[0]], Library.books)
        self.add_books([self.books[0], self.books[1]], Library)
        self.assertEqual([self.books[0], self.books[1]], Library.books)
        os.remove(os.path.realpath(self.store))

    def test_remove_book(self):
        Library(self.store, ["Fantasy", "Thriller"])
        self.add_books([self.books[0], self.books[1], self.books[1]], Library)
        Library.remove_book(self.books[0])
        self.assertEqual([self.books[1]], Library.books)
        Library.remove_book(self.books[0])
        self.assertNotEqual([], Library.books)
        Library.remove_book(self.books[1])
        self.assertEqual([], Library.books)
        os.remove(os.path.realpath(self.store))

    def test_book_information_by_title(self):
        Library(self.store, ["Fantasy", "Thriller"])
        self.add_books([self.books[0], self.books[1], self.books[2]], Library)
        book_birds = Library.book_information_by_title("Birds")
        self.assertEqual([self.books[1], self.books[2]], book_birds)
        book_somewhere = Library.book_information_by_title("Somewhere")
        self.assertEqual([self.books[0]], book_somewhere)
        self.assertEqual([], Library.book_information_by_title("Haha"))
        os.remove(os.path.realpath(self.store))

    def test_book_information_by_author(self):
        Library(self.store, ["Fantasy", "Thriller"])
        self.add_books(self.books, Library)
        book_steven = Library.book_information_by_author("Steve Law")
        self.assertEqual([self.books[0]], book_steven)
        book_john = Library.book_information_by_author("John White")
        self.assertEqual([self.books[1], self.books[4]], book_john)
        book_steve = Library.book_information_by_author("Steve Tyler")
        self.assertEqual([self.books[2], self.books[3]], book_steve)
        self.assertEqual([], Library.book_information_by_author("Haha"))
        os.remove(os.path.realpath(self.store))

    def test_number_of_different_books(self):
        Library(self.store, ["Fantasy", "Thriller"])
        self.add_books([self.books[0], self.books[1], self.books[2]], Library)
        self.assertEqual(3, Library.number_of_different_books())
        Library.add_book(self.books[0])
        self.assertEqual(3, Library.number_of_different_books())
        Library.remove_book(self.books[1])
        self.assertEqual(2, Library.number_of_different_books())
        os.remove(os.path.realpath(self.store))

    def test_number_of_books_by_genres(self):
        Library(self.store, ["Fantasy", "Thriller"])
        self.add_books([self.books[0], self.books[1], self.books[2]], Library)
        actual_result = Library.number_of_books_by_genres()
        self.assertEqual({'Fantasy': 2, 'Thriller': 1}, actual_result)
        Library.add_book(self.books[3])
        actual_result = Library.number_of_books_by_genres()
        self.assertEqual({'Fantasy': 2, 'Thriller': 2}, actual_result)
        Library.remove_book(self.books[1])
        actual_result = Library.number_of_books_by_genres()
        self.assertEqual({'Fantasy': 1, 'Thriller': 2}, actual_result)
        Library.remove_book(self.books[0])
        actual_result = Library.number_of_books_by_genres()
        self.assertEqual({'Fantasy': 0, 'Thriller': 2}, actual_result)
        os.remove(os.path.realpath(self.store))

    def test_create_genre_dict(self):
        Library(self.store, ["Fantasy", "Thriller"])
        self.add_books([self.books[0], self.books[1], self.books[2]], Library)
        Library.create_genre_dict()
        expected_dict = {"Fantasy": [self.books[1], self.books[0]],
                         "Thriller": [self.books[2]]}
        self.assertEqual(expected_dict, Library.genre_dict)
        Library.add_book(self.books[3])
        expected_dict["Thriller"].append(self.books[3])
        self.assertEqual(expected_dict, Library.genre_dict)
        os.remove(os.path.realpath(self.store))

if __name__ == '__main__':
    unittest.main()
