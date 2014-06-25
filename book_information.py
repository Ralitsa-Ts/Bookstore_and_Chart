import sys
import os
sys.path.append("model")

from library import Library, Book
from PyQt4 import QtGui, QtCore
from functools import partial


class BookInformation(QtGui.QWidget):
    def __init__(self):
        super(BookInformation, self).__init__()
        self.InitUI()

    def InitUI(self):
        self.table = QtGui.QTableWidget()
        self.prepare_the_search()
        self.prepare_the_folder_image()
        self.fill_in_grid()

    def fill_in_grid(self):
        """
            Fill the gridLayout with all the widgets.
        """
        self.grid = QtGui.QGridLayout()
        self.grid.addLayout(self.search, 0, 0)
        self.grid.addWidget(self.folder_image, 2, 0)
        self.grid.setSpacing(10)
        self.grid.setColumnStretch(0, 6)
        self.grid.setRowStretch(1, 1)
        self.grid.setRowStretch(2, 2)

        vBoxlayout = QtGui.QVBoxLayout()
        vBoxlayout.addLayout(self.grid)
        self.setLayout(vBoxlayout)

    def prepare_the_folder_image(self):
        """
            Prepares the folder image so that it can be later added.
        """
        self.folder_image = QtGui.QLabel()
        self.folder_image.setPixmap(QtGui.QPixmap(
                                    os.path.normpath("images/folder.jpg")))
        self.folder_image.setFixedWidth(200)
        self.folder_image.setFixedHeight(200)

    def prepare_the_search(self):
        """
            Prepares the search form.
        """
        self.searchEdit = QtGui.QLineEdit()
        self.searchEdit.setPlaceholderText("click to search")
        self.Search = QtGui.QPushButton("Search")
        self.Search.clicked.connect(self.update_table)

        self.author = QtGui.QRadioButton("by author")
        self.title = QtGui.QRadioButton("by title")
        self.both = QtGui.QRadioButton("by both")
        self.both.setChecked(True)

        box = QtGui.QHBoxLayout()
        box.addWidget(self.author)
        box.addWidget(self.title)
        box.addWidget(self.both)

        self.search = QtGui.QGridLayout()
        self.search.addWidget(self.searchEdit, 0, 0)
        self.search.addWidget(self.Search, 0, 2)
        self.search.addLayout(box, 1, 2)
        self.search.setColumnStretch(0, 3)
        self.search.setColumnStretch(3, 1)

    def generate_book_by_row(self, row):
        """
            Creates a book, which is in a certain row using the
            information from the table cells.
        """
        record = ""
        for i in range(6):
            data = self.table.item(row, i).text()
            record += ("+" + data)
        return Book.book_by_record(record[1:])

    def get_a_copy(self, row):
        """
            Take a copy of a certain book.
        """
        if int(self.table.item(row, 5).text()) > 0:
            book = Library.take_book(self.generate_book_by_row(row))
            item = QtGui.QTableWidgetItem(str(book.number_of_copies))
            self.table.setItem(row, 5, item)

    def return_a_copy(self, row):
        """
            Return a copy of a certain book.
        """
        book = Library.return_book(self.generate_book_by_row(row))
        item = QtGui.QTableWidgetItem(str(book.number_of_copies))
        self.table.setItem(row, 5, item)

    def like_a_book(self, row):
        """
            Like a book-increases it's rating.
        """
        book = Library.like_book(self.generate_book_by_row(row))
        value = "%.2f" % book.rating
        item = QtGui.QTableWidgetItem(str(value))
        self.table.setItem(row, 4, item)

    def dislike_a_book(self, row):
        """
            Dislike a book-decreases it's rating.
        """
        book = Library.dislike_book(self.generate_book_by_row(row))
        value = "%.2f" % book.rating
        item = QtGui.QTableWidgetItem(str(value))
        self.table.setItem(row, 4, item)

    def update_table(self):
        """
            Update the table after clicking the Search button.
        """
        self.table.setRowCount(0)
        self.table.setColumnCount(0)
        search = self.searchEdit.text()
        if self.author.isChecked():
            results = Library.book_information_by_author(search)
        elif self.title.isChecked():
            results = Library.book_information_by_title(search)
        else:
            results = Library.book_information_by_title_author(search)
        self.table = QtGui.QTableWidget(len(results), 10, self)
        headers = ("Title", "Author's name", "Published in", "Genre",
                   "Rating", "Copies", "Get", "Return", "Like", " Dislike")
        self.table.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.table.setHorizontalHeaderLabels(headers)
        self.table.resizeColumnsToContents()
        self.table.resizeRowsToContents()

        widths = [150, 150, 90, 80, 70, 60, 50, 60, 50, 70]
        for col, width in zip(range(9), widths):
            self.table.setColumnWidth(col, width)

        self.table.horizontalHeader().setStretchLastSection(True)
        for row in range(len(results)):
            book = results[row]
            col = 0
            for column in (book.title, book.author, book.year, book.genre,
                           book.rating, book.number_of_copies):
                item = QtGui.QTableWidgetItem(str(column))
                self.table.setItem(row, col, item)
                col += 1

        for row in range(len(results)):
            get_btn = QtGui.QPushButton("Get")
            get_btn.setMinimumSize(50, 30)
            get_btn.clicked.connect(partial(self.get_a_copy, row))
            self.table.setCellWidget(row, 6, get_btn)
            return_btn = QtGui.QPushButton("Return")
            return_btn.setMinimumSize(50, 30)
            return_btn.clicked.connect(partial(self.return_a_copy, row))
            self.table.setCellWidget(row, 7, return_btn)

            like_btn = QtGui.QPushButton("Like")
            like_btn.setMinimumSize(50, 30)
            like_btn.clicked.connect(partial(self.like_a_book, row))
            self.table.setCellWidget(row, 8, like_btn)
            dislike_btn = QtGui.QPushButton("Dislike")
            dislike_btn.setMinimumSize(50, 30)
            dislike_btn.clicked.connect(partial(self.dislike_a_book, row))
            self.table.setCellWidget(row, 9, dislike_btn)

        self.grid.addWidget(self.table, 1, 0)
