import sys
import os
sys.path.append("model")
from library import Library, Book
from PyQt4 import QtGui, QtCore
from functools import partial
FOLDER = os.path.normpath("images/folder.jpg")


class BookInformation(QtGui.QWidget):
    def __init__(self):
        super(BookInformation, self).__init__()
        self.InitUI()

    def InitUI(self):
        self.searchEdit = QtGui.QLineEdit()
        self.searchEdit.setPlaceholderText("click to search")
        Search = QtGui.QPushButton("Search")

        self.author = QtGui.QRadioButton("by author")
        self.title = QtGui.QRadioButton("by title")
        self.both = QtGui.QRadioButton("by both")
        self.both.setChecked(True)

        box = QtGui.QHBoxLayout()
        box.addWidget(self.author)
        box.addWidget(self.title)
        box.addWidget(self.both)

        manage = QtGui.QGridLayout()
        manage.addWidget(self.searchEdit, 0, 0)
        manage.addWidget(Search, 0, 2)
        manage.addLayout(box, 1, 2)
        manage.setColumnStretch(0, 3)
        manage.setColumnStretch(3, 1)

        image = QtGui.QLabel()
        image.setPixmap(QtGui.QPixmap(FOLDER))
        image.setFixedWidth(200)
        image.setFixedHeight(200)

        self.grid = QtGui.QGridLayout()
        self.grid.addLayout(manage, 0, 0)
        self.grid.addWidget(image, 2, 0)
        self.grid.setSpacing(10)
        self.grid.setColumnStretch(0, 6)
        self.grid.setRowStretch(1, 1)
        self.grid.setRowStretch(2, 2)
        self.table = QtGui.QTableWidget(0, 0)
        Search.clicked.connect(self.update_table)

        vBoxlayout = QtGui.QVBoxLayout()
        vBoxlayout.addLayout(self.grid)
        self.setLayout(vBoxlayout)

    def generate_book_by_row(self, row):
        record = ""
        for i in range(5):
            data = self.table.item(row, i).text()
            record += ("+" + data)
        print(record[1:])

    def get_a_copy(self, row):
        value = int(self.table.item(row, 4).text()) - 1
        if value >= 0:
            item = QtGui.QTableWidgetItem(str(value))
            self.table.setItem(row, 4, item)

    def return_a_copy(self, row):
        self.generate_book_by_row(row)
        value = int(self.table.item(row, 4).text()) + 1
        item = QtGui.QTableWidgetItem(str(value))
        self.table.setItem(row, 4, item)

    def like_a_book(self, row):
        #Library.like_book()
        value = "%.2f" % (float(self.table.item(row, 3).text()) + 0.1)
        item = QtGui.QTableWidgetItem(str(value))
        self.table.setItem(row, 3, item)

    def dislike_a_book(self, row):
        #Library.dislike_book()
        value = "%.2f" % (float(self.table.item(row, 3).text()) - 0.1)
        item = QtGui.QTableWidgetItem(str(value))
        self.table.setItem(row, 3, item)

    def update_table(self):
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
        headers = ("Title", "Author's name", "Published in", "Rating",
                   "Copies", "Genre", "Get", "Return", "Like"," Dislike")
        self.table.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.table.setHorizontalHeaderLabels(headers)
        self.table.resizeColumnsToContents()
        self.table.resizeRowsToContents()

        widths = [140, 140, 90, 60, 70, 80, 50, 60, 50, 60]
        for col, width in zip(range(9), widths):
            self.table.setColumnWidth(col, width)

        self.table.horizontalHeader().setStretchLastSection(True)
        for row in range(len(results)):
            book = results[row]
            col = 0
            for column in (book.title, book.author, book.year, book.rating,
                           book.number_of_copies, book.genre):
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
