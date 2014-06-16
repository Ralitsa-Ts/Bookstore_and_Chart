import sys
import os
sys.path.append("model")
from library import Library, Book
from PyQt4 import QtGui, QtCore
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
        self.table = QtGui.QTableWidget(len(results), 9, self)
        headers = ("Title", "Author's name", "Published in", "Rating",
                   "Copies", "Genre", "Get", "Return", "Vote")
        self.table.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.table.setHorizontalHeaderLabels(headers)
        self.table.resizeColumnsToContents()
        self.table.resizeRowsToContents()

        widths = [160, 150, 90, 60, 70, 90, 60]
        for col, width in zip(range(7), widths):
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
            btn = QtGui.QPushButton("Get")
            btn.setMinimumSize(50, 30)
            btn2 = QtGui.QPushButton("Return")
            btn2.setMinimumSize(50, 30)
            self.table.setCellWidget(row, 6, btn)
            self.table.setCellWidget(row, 7, btn2)

        self.grid.addWidget(self.table, 1, 0)
