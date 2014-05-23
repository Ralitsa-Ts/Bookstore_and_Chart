from book import Book
import unittest

BOOK_INFORMATION = ("Birds", "John White", 3.3, 2001, "Fantasy", 5)
BOOK_INFORMATION1 = ("Birds", "John white", 3.3, 2011, "Fantasy", 0)
BOOK_INFORMATION2 = ("Domino", "Peter Clark", 2, 2000, "Thriller", 3)


class BookTest(unittest.TestCase):
    def test_book_equals(self):
        self.assertEqual(Book(*BOOK_INFORMATION), Book(*BOOK_INFORMATION))
        self.assertNotEqual(Book(*BOOK_INFORMATION), Book(*BOOK_INFORMATION1))

    def test_is_available(self):
        self.assertFalse(Book(*BOOK_INFORMATION1).is_available())
        self.assertTrue(Book(*BOOK_INFORMATION2).is_available())

    def test_decrease_number_of_copies(self):
        book = Book(*BOOK_INFORMATION)
        book.decrease_number_of_copies(10)
        self.assertEqual(0, book.number_of_copies)

    def test_increase_number_of_copies(self):
        book = Book(*BOOK_INFORMATION1)
        new_number_of_copies = book.number_of_copies + 10
        book.increase_number_of_copies(10)
        self.assertEqual(new_number_of_copies, book.number_of_copies)

    def test_decrease_rating(self):
        pass

    def test_increase_rating(self):
        pass

if __name__ == '__main__':
    unittest.main()
