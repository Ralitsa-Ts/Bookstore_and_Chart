"""
    This module's main purpose is to modify a file that contains
    records of books
"""

from book import Book
import os


class MissingBook(Exception):
    pass


class BookDataBase:
    """
        This class mainly adds a record of a book to file and removes a
        record.
    """

    def __init__(self, _file):
        self.file = _file
        if not os.path.exists(self.file):
            f = open(self.file, 'a')
            f.close()

    def booklist(self):
        """
            Returns a list of the books that are recorded in the file.
        """
        with open(self.file, 'r') as file:
            return [Book.book_by_record(book) for book in file.readlines()]

    def add_record(self, book):
        """
            Adds a new record of a book to the file.If there is a book that
            has the same title,author and year of publication then the book
            already exist and we only change the number of copies of the
            recorded book.Otherwise, we add the new book.
        """
        with open(self.file, 'r') as file:
            data = file.readlines()
        try:
            _file = self.file
            enum = enumerate(data)
            I = next(i for i, v in enum if Book.book_by_record(v) == book)
            os.rename(os.path.realpath(_file), os.path.realpath(_file)+".bak")
            copies = int(data[I].rstrip('\n').split('+')[-1])
            book_update = book.special_record().rstrip('\n').split('+')
            book_update[-1] = str(int(book_update[-1]) + copies)
            data[I] = '+'.join(book_update) + '\n'
            with open(_file, 'w') as file:
                file.writelines(data)
            os.remove(os.path.realpath(self.file)+".bak")
        except StopIteration:
            data.append(book.special_record())
            with open(self.file, 'a') as file:
                file.write(book.special_record())

    def remove_record(self, book):
        """
            Removes a record of a book that represents the given book.The
            record represents the given book if the title,author and year
            of publication match.
        """
        with open(self.file, 'r') as file:
            books_record = file.readlines()
        books = self.booklist()
        if book in books:
            _file = self.file
            os.rename(os.path.realpath(_file), os.path.realpath(_file)+".bak")
            with open(self.file, 'w') as file:
                counter = 0
                for _book in books_record:
                    if book != books[counter]:
                        file.write(_book)
                    counter += 1
            os.remove(os.path.realpath(self.file)+".bak")
        else:
            raise MissingBook("No such book")
