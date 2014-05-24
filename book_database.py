from book import Book
import os


class MissingBook(Exception):
    pass


class BookDataBase:

    def __init__(self, _file):
        self.file = _file
        if not os.path.exists(self.file):
            f = open(self.file, 'a')
            f.close()

    def booklist(self):
        with open(self.file, 'r') as file:
            return [Book.book_by_record(book) for book in file.readlines()]

    def writer(self, book):
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

    def remover(self, book):
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
