"""
    This module ensures that the important functions of class BookDataBase
    from the module book_database work as expected.
"""
import sys
import os
import unittest
parent = os.path.normpath(os.path.dirname(os.path.dirname(os.path.abspath
                         (__file__))) + "/model")
sys.path.append(parent)
from book_database import Book, BookDataBase, MissingBookError


class BookDataBaseTest(unittest.TestCase):
    def setUp(self):
        self.file = "test.txt"

    def test_booklist(self):
        database = BookDataBase(self.file)
        book = Book("What", "Steven Law", 2000, "Thriller", 0.2, 3)
        book1 = Book("What", "Steven Maw", 2000, "Thriller", 0.2, 20)
        book2 = Book("Go", "Steven Law", 2000, "Thriller", 0.2, 20)
        booklist = [book, book1, book2]
        with open(self.file, 'w') as file:
            file.write("What+Steven Law+2000+Thriller+0.2+3\n")
            file.write("What+Steven Maw+2000+Thriller+0.2+20\n")
            file.write("Go+Steven Law+2000+Thriller+0.2+20\n")
        self.assertEqual(booklist, database.booklist())
        os.remove(os.path.realpath(self.file))

    def test_add_record(self):
        database = BookDataBase(self.file)
        book = Book("Somewhere", "Steven Law", 2000, "Fantasy", 0.2, 3)
        book1 = Book("What", "Steven Maw", 2000, "Triller", 0.2, 20)
        book2 = Book("Go", "Steven Law", 2000, "Thriller", 0.2, 20)
        book3 = Book("Go", "Steven Law", 2000, "Thriller", 0.8, 12)
        booklist = [book, book1, book2]
        expected_records = [book.special_record() for book in booklist]
        database.add_record(book)
        database.add_record(book1)
        database.add_record(book2)
        with open(self.file, 'r') as file:
            actual_records = file.readlines()
        self.assertEqual(expected_records, actual_records)
        database.add_record(book3)
        book3.increase_number_of_copies(20)
        booklist = [book, book1, book3]
        new_expected_records = [book.special_record() for book in booklist]
        with open(self.file, 'r') as file:
            updated_records = file.readlines()
        self.assertEqual(new_expected_records, updated_records)
        os.remove(os.path.realpath(self.file))

    def test_remove_record(self):
        database = BookDataBase(self.file)
        book = Book("What", "Steven Law", 2000, "Thriller", 0.2, 3)
        book1 = Book("What", "Steven Maw", 2000, "Thriller", 0.2, 20)
        book2 = Book("Go", "Steven Law", 2000, "Thriller", 0.2, 20)
        booklist = [book, book1, book2]
        recordlist = [book.special_record() for book in booklist]
        with open(self.file, 'w') as file:
            file.write("What+Steven Law+2000+Thriller+0.2+3\n")
            file.write("What+Steven Maw+2000+Thriller+0.2+20\n")
            file.write("Go+Steven Law+2000+Thriller+0.2+20\n")
        database.remove_record(book2)
        del recordlist[2]
        with open(self.file, 'r') as file:
            records_after_removal = file.readlines()
        self.assertEqual(recordlist, records_after_removal)
        database.remove_record(book)
        del recordlist[0]
        with open(self.file, 'r') as file:
            records_after_removal = file.readlines()
        self.assertEqual(recordlist, records_after_removal)
        os.remove(os.path.realpath(self.file))

    def test_remove_missing_record(self):
        database = BookDataBase(self.file)
        book = Book("What", "Steven Law", 2000, "Thriller", 0.2, 3)
        with open(self.file, 'w') as file:
            file.write("What+Steven Maw+2000+Thriller+0.2+20\n")
            file.write("Go+Steven Law+2000+Thriller+0.2+20\n")
        with self.assertRaises(MissingBookError):
            database.remove_record(book)

if __name__ == '__main__':
    unittest.main()
