from book import Book
class BookDataBase:

    def __init__(self, _file):
        self.file = _file
        self.database = list()

    def output_information(self, book):
        f = open(self.file, 'a')
        f.write(book.special_record())
        f.close()

    def access_information(self):
        f = open(self.file, 'r')
        booklist = list()
        for line in f.readlines():
            self.database.append(line)
            booklist.append(Book(*line.split('+')))
        f.close()
        return booklist

    def write_over_line(self, book):
        f = open(self.file, 'r+')
        books = list()
        for line in f.readlines():
            book1 = Book(*line.split('+'))
            print(book1)
            if book != book1:
                books.append(line)
            else:
                book.increase_number_of_copies(book1.number_of_copies)
                books.append(book.special_record())
                break
        f.seek(0)
        for line in books:
            f.write(line)
        f.close()


book = Book("What", "Steven Law", 2000, "Thriller", 0.2, 3)
book1 = Book("What", "Steven Law", 2000, "Thriller", 0.2, 20)
e = BookDataBase("database.txt")
e.output_information(book)
e.write_over_line(book1)
e.access_information()
