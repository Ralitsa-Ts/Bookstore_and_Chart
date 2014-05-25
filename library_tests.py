from library import Library, Book
import unittest
import os
STORE = "storage.txt"


class LibraryTest(unittest.TestCase):
    def test_add_book(self):
        possible_genres = ["Fantasy"]
        library = Library(STORE, possible_genres)
        book = Book("Somewhere", "Steven Law", 2000, "Fantasy", 0.2, 3)
        book1 = Book("Birds", "John White", 2001, "Fantasy", 3.3, 15)
        library.add_book(book)
        self.assertEqual([book], library.books)
        library.add_book(book)
        library.add_book(book1)
        self.assertEqual([book, book1], library.books)
        os.remove(os.path.realpath(STORE))

    def test_remove_book(self):
        possible_genres = ["Fantasy", "Thriller"]
        library = Library(STORE, possible_genres)
        book = Book("Somewhere", "Steven Law", 2000, "Fantasy", 0.2, 3)
        book1 = Book("Birds", "John White", 2001, "Thriller", 3.3, 15)
        library.add_book(book)
        library.add_book(book1)
        library.add_book(book1)
        library.remove_book(book)
        self.assertEqual([book1], library.books)
        library.remove_book(book)
        self.assertNotEqual([], library.books)
        library.remove_book(book1)
        self.assertEqual([], library.books)
        os.remove(os.path.realpath(STORE))

    def test_book_information_by_title(self):
        possible_genres = ["Fantasy", "Thriller"]
        library = Library(STORE, possible_genres)
        book = Book("Somewhere", "Steven Law", 2000, "Fantasy", 0.2, 3)
        book1 = Book("Birds", "John White", 2001, "Thriller", 3.3, 15)
        book2 = Book("Birds", "Steve Tyler", 2011, "Thriller", 3.3, 15)
        library.add_book(book)
        library.add_book(book1)
        library.add_book(book2)
        book_birds = library.book_information_by_title("Birds")
        self.assertEqual([book1, book2], book_birds)
        book_somewhere = library.book_information_by_title("Somewhere")
        self.assertEqual([book], book_somewhere)
        self.assertEqual([], library.book_information_by_title("Haha"))
        os.remove(os.path.realpath(STORE))

    def test_book_information_by_author(self):
        possible_genres = ["Fantasy", "Thriller"]
        library = Library(STORE, possible_genres)
        book = Book("Somewhere", "Steven Law", 2000, "Fantasy", 0.2, 3)
        book1 = Book("Birds", "John White", 2001, "Thriller", 3.3, 15)
        book2 = Book("Birds", "Steve Tyler", 2012, "Thriller", 3.5, 10)
        book3 = Book("Never", "Steve Tyler", 2001, "Thriller", 3.5, 15)
        book4 = Book("Hello", "John White", 2010, "Thriller", 3.0, 10)
        library.add_book(book)
        library.add_book(book1)
        library.add_book(book2)
        library.add_book(book3)
        library.add_book(book4)
        book_steven = library.book_information_by_author("Steven Law")
        self.assertEqual([book], book_steven)
        book_john = library.book_information_by_author("John White")
        self.assertEqual([book1, book4], book_john)
        book_steve = library.book_information_by_author("Steve Tyler")
        self.assertEqual([book2, book3], book_steve)
        self.assertEqual([], library.book_information_by_author("Haha"))
        os.remove(os.path.realpath(STORE))

    def test_number_of_different_books(self):
        pass

    def test_number_of_books_by_genres(self):
        pass

    def test_create_genre_dict(self):
        pass

if __name__ == '__main__':
    unittest.main()