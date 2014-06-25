"""
    This module contains a class named Book,which provides
    storing and manipulating some basic information about a book.
"""


class Book:
    """
        This class provides us with the opportunity to create objects
        that represent different books.
    """
    def __init__(self, title, author, year, genre, rating, copies):
        """
            Setting the basic information about the book.
            Keyword arguments:
            * title - The title of the book
            * author - The author's name
            * rating - The rating of the book
            * year - Year ot publication
            * genre - Genre
            * copies - Number of copies that are available
        """
        self._title = title
        self._author = author
        self._year = int(year)
        self._genre = genre
        if rating == "":
            self._rating = 0
        else:
            self._rating = float("%.2f" % float(rating))
        if copies == "":
            self._number_of_copies = 1
        else:
            self._number_of_copies = int(copies)

    def __str__(self):
        """
            Get full information about the book.
        """
        return ("<Book Information>\nTitle:{}\n".format(self.title) +
                "Author:{}\nPublished in:{}\n".format(self.author, self.year) +
                "Genre:{}\nRating:{}\n".format(self.genre, self.rating) +
                "Number of copies:{}\n".format(self.number_of_copies))

    def __repr__(self):
        """
            Representation of a book.
        """
        return ("<Book " + self._title + " by " + self._author + " published"
                " in " + str(self._year) + ";genre:" + self._genre + ">")

    def __eq__(self, other):
        """
            Check if two books are the same by comparing their title,
            author and year of publication
        """
        if not isinstance(other, self.__class__):
            return False
        elif self._title == other._title and self._author == other._author:
            return True and self._year == other._year
        else:
            return False and self._year == other._year

    def __ne__(self, other):
        """
            Check if two books are not the same by comparing their title,
            author and year of publication
        """
        return not self.__eq__(other)

    @property
    def rating(self):
        """
            This function will return the value of the rating if it is between
            0 and 5.In case it is less than 0 or greater than 5 the function
            will return corespondingly 0 or 5
        """
        if self._rating >= 0 and self._rating <= 5:
            return self._rating
        elif self._rating < 0:
            return 0
        else:
            return 5

    @property
    def title(self):
        """
            Returns the book's title
        """
        return self._title

    @property
    def author(self):
        """
            Returns the book's author
        """
        return self._author

    @property
    def year(self):
        """
            Returns the book's year of publication
        """
        return self._year

    @property
    def genre(self):
        """
            Returns the book's genre
        """
        return self._genre

    @property
    def number_of_copies(self):
        """
            Returns the number of the book's copies that are available
        """
        return self._number_of_copies

    def decrease_number_of_copies(self, taken_copies):
        """
            Decrease the number of the available copies with a certain number.
            If the numer of copies is less than the number we take all
            available copies.
        """
        self._number_of_copies -= taken_copies
        if self._number_of_copies < 0:
            self._number_of_copies = 0

    def increase_number_of_copies(self, added_copies):
        """
            Increase the number of the available copies with a certain number.
        """
        self._number_of_copies += added_copies

    def decrease_rating(self):
        """
            Decrease the rating of the book with 0.1.
        """
        self._rating -= 0.1

    def increase_rating(self):
        """
            Increase the rating of the book with 0.1.
        """
        self._rating += 0.1

    def special_record(self):
        """
            Returns a special representation of the book's information
            that may be used as output to a file.The components of the
            book's information are splitted with '+'
        """
        return "{}+{}+{}+{}+{}+{}".format(self.title, self.author, self.year,
                                          self.genre, self.rating,
                                          self.number_of_copies) + "\n"

    @staticmethod
    def book_by_record(record):
        """
            Returns a book that was created after using the special record.
        """
        return Book(*record.rstrip('\n').split('+'))
