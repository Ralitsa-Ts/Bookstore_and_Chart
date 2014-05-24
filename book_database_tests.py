"""
    This module ensures that the important functions of class BookDataBase
    from the module book_database work as expected.
"""

from book_database import BookDataBase, Book
import unittest
import os
FILE = "test.txt"

class BookDataBaseTest(unittest.TestCase):
    def test_booklist(self):
        database = BookDataBase(FILE)
        book = Book("What", "Steven Law", 2000, "Thriller", 0.2, 3)
        book1 = Book("What", "Steven Maw", 2000, "Triller", 0.2, 20)
        book2 = Book("Go", "Steven Law", 2000, "Thriller", 0.2, 20)
        booklist = [book, book1, book2]
        with open(FILE, 'w') as file:
            file.write("What+Steven Law+2000+Thriller+0.2+3\n")
            file.write("What+Steven Maw+2000+Thriller+0.2+20\n")
            file.write("Go+Steven Law+2000+Thriller+0.2+20\n")
        self.assertEqual(booklist, database.booklist())
        os.remove(os.path.realpath(FILE))

    def test_add_record(self):
        pass



if __name__ == '__main__':
    unittest.main()


