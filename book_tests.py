"""
    This module ensures that the important functions of class Book from
    the module book work as expected
"""
from book import Book
import unittest


class BookTest(unittest.TestCase):
    def test_book_equals(self):
        book1 = Book("Birds", "John White", 3.3, 2001, "Fantasy", 15)
        book2 = Book("Birds", "John Black", 3.3, 2001, "Fantasy", 15)
        book3 = Book("Birds", "John White", 4.3, 2001, "Fantasy", 1)
        self.assertEqual(book1, book1)
        self.assertEqual(book1, book3)
        self.assertNotEqual(book1, book2)

    def test_book_information(self):
        book = Book("My war", "Carl Son", 3, 1988, "Mystery", 2)
        print(book)
        self.assertEqual("<Book Information>\nTitle:My war\nAuthor:Carl " +
                         "Son\nPublished in:1988\nGenre:Mystery\n" +
                         "Rating:3\nNumber of copies:2\n", str(book))

    def test_is_available(self):
        book1 = Book("Lords", "Steven Moore", 2, 2000, "Thriller", 0)
        book2 = Book("Lords", "Steven Moore", 2, 2000, "Thriller", 10)
        self.assertFalse(book1.is_available())
        self.assertTrue(book2.is_available())

    def test_decrease_number_of_copies(self):
        book = Book("Lords", "Steven Moore", 2, 2000, "Thriller", 15)
        book.decrease_number_of_copies(10)
        self.assertEqual(5, book.number_of_copies)
        book.decrease_number_of_copies(6)
        self.assertNotEqual(-1, book.number_of_copies)
        self.assertEqual(0, book.number_of_copies)

    def test_increase_number_of_copies(self):
        book = Book("Lords", "Steven Moore", 2, 2000, "Thriller", 0)
        book.increase_number_of_copies(10)
        self.assertEqual(10, book.number_of_copies)
        book.increase_number_of_copies(5)
        self.assertNotEqual(10, book.number_of_copies)
        self.assertEqual(15, book.number_of_copies)

    def test_decrease_rating(self):
        book = Book("What", "Steven Law", 0.1, 2000, "Thriller", 0)
        book.decrease_rating()
        self.assertEqual(0, book.rating)
        book.decrease_rating()
        self.assertNotEqual(-0.1, book.rating)

    def test_increase_rating(self):
        book = Book("What", "Steven Law", 4.9, 2000, "Thriller", 0)
        book.increase_rating()
        self.assertEqual(5, book.rating)
        book.increase_rating()
        self.assertNotEqual(5.1, book.rating)

if __name__ == '__main__':
    unittest.main()
