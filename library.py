from book_database import Book, BookDataBase


class Library:
    def __init__(self, storage, genres):
        self.storage = storage
        self.genres = genres
        self.database = BookDataBase(self.storage)
        self.books = self.database.booklist()
        self.number_of_books = len(self.books)
        Library.create_genre_dict(self.books, self.genres)

    def add_book(self, book):
        self.database(add_record)
        self.books.append(book)
        self.number_of_books += 1

    def remove_book(self, book):
        if book in self.books:
            self.database(remove_record(book))
            self.books.remove(book)
            self.number_of_books -= 1

    def book_information_by_title(self, title):
        return [book for book in self.books if book.title() == title]

    def book_information_by_author(self, author):
        return [book for book in self.books if book.author() == author]

    def number_of_different_books(self):
        return self.number_of_books

    def number_of_books_by_genres(self):
        return {genre: len(books) for genre, books in genre_dict.items()}

    @staticmethod
    def create_genre_dict(books, genres):
        self.genre_dict = dict()
        for genre in genres:
            books_by_genre = [book for book in books if book.genre == genre]
            sorting = lambda x: x.title
            genre_dict[genre] = sorted(book_by_genre, key=sorting)