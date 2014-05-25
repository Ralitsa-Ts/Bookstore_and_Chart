from book_database import Book, BookDataBase


class Library:

    def __init__(self, storage, genres):
        self.storage = storage
        self.genres = genres
        self.database = BookDataBase(self.storage)
        self._books = self.database.booklist()
        self.number_of_books = len(self._books)
        self.create_genre_dict()

    @property
    def books(self):
        return self._books

    def add_book(self, book):
        self.database.add_record(book)
        if book in self._books:
            index = self._books.index(book)
            new_copies = book.number_of_copies
            self._books[index].increase_number_of_copies(new_copies)
        else:
            self._books.append(book)
            self.number_of_books += 1
            self.genre_dict[book.genre].append(book)

    def remove_book(self, book):
        if book in self._books:
            self.database.remove_record(book)
            self._books.remove(book)
            self.number_of_books -= 1
            self.genre_dict[book.genre].remove(book)

    def book_information_by_title(self, title):
        return [book for book in self._books if book.title == title]

    def book_information_by_author(self, author):
        return [book for book in self._books if book.author == author]

    def number_of_different_books(self):
        return self.number_of_books

    def number_of_books_by_genres(self):
        return {genre: len(books) for genre, books in self.genre_dict.items()}

    def create_genre_dict(self):
        self.genre_dict = dict()
        books = self._books
        for genre in self.genres:
            books_by_genre = [book for book in books if book.genre == genre]
            sorting = lambda x: x.title
            self.genre_dict[genre] = sorted(books_by_genre, key=sorting)
