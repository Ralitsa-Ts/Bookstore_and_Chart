from book import Book
class BookDataBase:

    def __init__(self, _file):
        self.file = _file
        self.database = list()

    def output_information(self, book):
        f = open(self.file, 'a')
        #f.write(book.special_record())
        f.close()

    def access_information(self):
        f = open(self.file, 'r')
        booklist = list()
        lines = f.readlines()
        if lines != []:
            for line in lines:
                self.database.append(line)
                booklist.append(Book(*line.split('+')))
        f.close()
        return booklist

    def write_over_line(self, book):
        try:
            f = open(self.file, 'r+')
            books = list()
            lines = f.readlines()
            if lines != []:
                for line in lines:
                    book1 = Book(*line.rstrip('\n').split('+'))
                    if book != book1:
                        books.append(book.special_record().rstrip('\n'))
                    else:
                        book.increase_number_of_copies(book1.number_of_copies)
                        books.append(book.special_record().rstrip('\n'))
                        break
                f.seek(0)
                for line in books:
                    f.write(line)
            else:
                f.write(book.special_record().rstrip('\n'))
            f.close()
        except FileNotFoundError:
            f = open(self.file, 'w')
            f.write(book.special_record().rstrip('\n'))
            f.close()


book = Book("What", "Steven Law", 2000, "Thriller", 0.2, 3)
book1 = Book("What", "Steven Law", 2000, "Thriller", 0.2, 20)
book2 = Book("Go", "Steven Law", 2000, "Thriller", 0.2, 20)
print(book.special_record().rstrip('\n'))
e = BookDataBase("database.txt")
e.output_information(book)
e.write_over_line(book1)
e.write_over_line(book2)
e.access_information()