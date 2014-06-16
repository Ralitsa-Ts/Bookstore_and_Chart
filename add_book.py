import sys
import os
sys.path.append("model")
from library import Library, Book
from PyQt4 import QtGui, QtCore

AUTHOR = os.path.normpath("images/author.jpg")
BOOKS = os.path.normpath("images/books.png")
COPIES = os.path.normpath("images/copies.jpg")
GENRES = os.path.normpath("images/genres.jpg")
RATING = os.path.normpath("images/rating.png")
STYLE = os.path.normpath("images/style.png")
TITLE = os.path.normpath("images/title.jpg")
YEAR = os.path.normpath("images/year.jpg")

POSSIBLE_GENRES = ["Fantasy", "Crime", "Thriller", "Romance", "Other"]
DATABASE = "model/database.txt"
LIBRARY = Library(DATABASE, POSSIBLE_GENRES)

class AddBook(QtGui.QWidget):
    def __init__(self):
        super(AddBook, self).__init__()
        self.genres = POSSIBLE_GENRES
        self.InitUI()

    def InitUI(self):
        self.titleEdit = QtGui.QLineEdit()
        self.authorEdit = QtGui.QLineEdit()
        self.yearEdit = QtGui.QLineEdit()
        self.genre_options = QtGui.QComboBox()
        self.genre_options.addItems(self.genres)
        self.ratingEdit = QtGui.QLineEdit()
        self.copiesEdit = QtGui.QLineEdit()

        self.gadgets = [self.titleEdit, self.authorEdit, self.yearEdit,
                        self.genre_options, self.ratingEdit, self.copiesEdit]

        place_holders = ("click to add a title",
                         "click to add the author's name",
                         "click to add year of publication",
                         "", "optional", "optional")

        for gadget, place_holder in zip(self.gadgets, place_holders):
            if gadget != self.genre_options:
                gadget.setPlaceholderText(place_holder)

        Add = QtGui.QPushButton("Add")
        Add.clicked.connect(self.addBook)
        self.gadgets.append(Add)
        form = QtGui.QFormLayout()
        texts = ("Title*:", "Author*:", "Published in*:", "Genre:", "Rating:",
                 "Copies:", " ")
        for text, gadget in zip(texts, self.gadgets):
            form.addRow(text, gadget)
        self.gadgets.remove(Add)
        self.title_image = QtGui.QLabel()
        self.author_image = QtGui.QLabel()
        self.year_image = QtGui.QLabel()
        self.genre_image = QtGui.QLabel()
        self.rating_image = QtGui.QLabel()
        self.copies_image = QtGui.QLabel()

        images = (self.title_image, self.author_image, self.year_image,
                  self.genre_image, self.rating_image, self.copies_image)
        images_tooltips = ("Use letters only!", "Use letters only!",
                           "Use numbers only!",
                           "Choose from the given options!",
                           "Enter a rating from 0 to 5!", "Enter a number!")
        pixmaps = (TITLE, AUTHOR, YEAR, GENRES, RATING, COPIES)

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
        image.setPixmap(QtGui.QPixmap(BOOKS))
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

    def addBook(self):
        new_book = Book(self.titleEdit.text(), self.authorEdit.text(),
                        self.yearEdit.text(),
                        self.genre_options.currentText(),
                        self.ratingEdit.text(), self.copiesEdit.text())
        LIBRARY.add_book(new_book)
        for gadget in self.gadgets:
            if gadget != self.genre_options:
                gadget.clear()