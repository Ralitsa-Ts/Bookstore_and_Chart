import sys
import os
sys.path.append("model")
from library import Library, Book
from PyQt4 import QtGui, QtCore

AUTHOR = os.path.normpath("images/author.jpg")
BOOK_REMOVE = os.path.normpath("images/book-remove.jpg")
GENRES = os.path.normpath("images/genres.jpg")
TITLE = os.path.normpath("images/title.jpg")
YEAR = os.path.normpath("images/year.jpg")

DATABASE = "model/database.txt"
POSSIBLE_GENRES = ["Fantasy", "Crime", "Thriller", "Romance", "Other"]
Library = Library(DATABASE, POSSIBLE_GENRES)

class RemoveBook(QtGui.QWidget):
    def __init__(self):
        super(RemoveBook, self).__init__()
        self.genres = POSSIBLE_GENRES
        self.InitUI()


    def InitUI(self):
        self.titleEdit = QtGui.QLineEdit()
        self.authorEdit = QtGui.QLineEdit()
        self.yearEdit = QtGui.QLineEdit()
        self.genre_options = QtGui.QComboBox()
        self.genre_options.addItems(self.genres)

        self.titleEdit.setPlaceholderText("click to add a title")
        self.authorEdit.setPlaceholderText("click to add the author's name")
        self.yearEdit.setPlaceholderText("click to add year of publication")

        Remove = QtGui.QPushButton("Remove")
        Remove.clicked.connect(self.removeBook)
        form = QtGui.QFormLayout()
        form.addRow("Title*:", self.titleEdit)
        form.addRow("Author*:", self.authorEdit)
        form.addRow("Published in:", self.yearEdit)
        form.addRow("Genre:", self.genre_options)
        form.addRow(" ", Remove)


        self.title_image = QtGui.QLabel()
        self.author_image = QtGui.QLabel()
        self.year_image = QtGui.QLabel()
        self.genre_image = QtGui.QLabel()

        images = (self.title_image, self.author_image, self.year_image,
                  self.genre_image)
        images_tooltips = ("Use letters only!", "Use letters only!",
                           "Use numbers only!",
                           "Choose from the given options!")
        pixmaps = (TITLE, AUTHOR, YEAR, GENRES)

        images_width = 25
        images_height = 24

        for image, tooltip, pixmap in zip(images, images_tooltips, pixmaps):
            image.setFixedWidth(images_width)
            image.setFixedHeight(images_height)
            image.setToolTip(tooltip)
            image.setPixmap(QtGui.QPixmap(pixmap))

        form1 = QtGui.QFormLayout()
        for image in images:
            form1.addRow("", image)

        image = QtGui.QLabel()
        image.setPixmap(QtGui.QPixmap(BOOK_REMOVE))
        image.setFixedWidth(200)
        image.setFixedHeight(200)
        grid = QtGui.QGridLayout()
        grid.addLayout(form, 0, 0)
        grid.addLayout(form1, 0, 1)
        grid.addWidget(image, 0, 2)
        grid.setSpacing(10)
        grid.setColumnStretch(0, 5)
        grid.setColumnStretch(1, 2)
        grid.setRowStretch(1, 1)

        vBoxlayout = QtGui.QVBoxLayout()
        vBoxlayout.addLayout(grid)
        self.setLayout(vBoxlayout)

    def removeBook(self):
        book = Book(self.titleEdit.text(), self.authorEdit.text(),
                    self.yearEdit.text(),
                    self.genre_options.currentText(), 0, 0)
        Library.remove_book(book)
        for edit in (self.titleEdit, self.authorEdit, self.yearEdit):
            edit.clear()
