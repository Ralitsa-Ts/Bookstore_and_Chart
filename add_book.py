import sys
import os
sys.path.append("model")

from library import Library, Book
from PyQt4 import QtGui, QtCore
from validations import Validations


class AddBook(QtGui.QWidget):
    def __init__(self):
        super(AddBook, self).__init__()
        self.image_dir = "images/"
        self.genres = Library.genres
        self.InitUI()

    def InitUI(self):
        self.set_input_form()
        self.set_icons()
        self.prepare_book_image()
        self.prepare_statusbar()
        self.fill_in_grid()

    def fill_in_grid(self):
        """
            Fill the gridLayout with all the widgets.
        """
        grid = QtGui.QGridLayout()
        grid.addLayout(self.input_form, 0, 0)
        grid.addLayout(self.icon_form, 0, 1)
        grid.addWidget(self.book_image, 0, 2)
        grid.addWidget(self.window, 1, 0)
        grid.setSpacing(10)
        grid.setColumnStretch(0, 5)
        grid.setColumnStretch(1, 2)
        grid.setRowStretch(1, 1)
        vBoxlayout = QtGui.QVBoxLayout()
        vBoxlayout.addLayout(grid)
        self.setLayout(vBoxlayout)

    def prepare_statusbar(self):
        """
            Prepare the statusBar, which will show whether the addition
            of a book is successful or not.
        """
        self.window = QtGui.QMainWindow()
        self.statusBar = QtGui.QStatusBar()
        self.label = QtGui.QLabel()
        self.statusBar.addWidget(self.label)
        self.window.setStatusBar(self.statusBar)

    def prepare_book_image(self):
        """
            Prepare the image of the book so that it can be added.
        """
        self.book_image = QtGui.QLabel()
        self.book_image.setPixmap(QtGui.QPixmap
                                 (os.path.normpath("images/books.png")))
        self.book_image.setFixedWidth(200)
        self.book_image.setFixedHeight(200)

    def set_input_form(self):
        """
            Set the form where the user will input information about the book.
        """
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
        self.input_form = QtGui.QFormLayout()
        texts = ("Title*:", "Author*:", "Published in*:", "Genre*:",
                 "Rating:", "Copies:", " ")
        for text, gadget in zip(texts, self.gadgets):
            self.input_form.addRow(text, gadget)
        self.gadgets.remove(Add)

    def set_icons(self):
        """
            Set the small icons.
        """
        title_image = QtGui.QLabel()
        author_image = QtGui.QLabel()
        year_image = QtGui.QLabel()
        genre_image = QtGui.QLabel()
        rating_image = QtGui.QLabel()
        copies_image = QtGui.QLabel()

        images = (title_image, author_image, year_image,
                  genre_image, rating_image, copies_image)
        images_tooltips = ("Use letters only!", "Use letters only!",
                           "Use numbers only!",
                           "Choose from the given options!",
                           "Enter a rating from 0 to 5!", "Enter a number!")
        pixmaps = ["title.jpg", "author.jpg", "year.jpg", "genres.jpg",
                   "rating.png", "copies.jpg"]

        for count in range(len(pixmaps)):
            pixmaps[count] = os.path.normpath(self.image_dir + pixmaps[count])

        images_width = 25
        images_height = 24

        for image, tooltip, pixmap in zip(images, images_tooltips, pixmaps):
            image.setFixedWidth(images_width)
            image.setFixedHeight(images_height)
            image.setToolTip(tooltip)
            image.setPixmap(QtGui.QPixmap(pixmap))

        self.icon_form = QtGui.QFormLayout()
        for image in images:
            self.icon_form.addRow("", image)

    def addBook(self):
        """
            Use the entered information if it is valid in order to add the
            book after the Add button is pushed.
        """
        data = [self.titleEdit.text(), self.authorEdit.text(),
                self.yearEdit.text(), self.genre_options.currentText(),
                self.ratingEdit.text(), self.copiesEdit.text()]
        invalid_data = Validations.check_all(*data)
        if invalid_data == []:
            new_book = Book(*data)
            Library.add_book(new_book)
            self.label.setText('You added the book successfully!')
        else:
            message = "Unsuccessful addition!Invalid:\n"
            message += '\n'.join(invalid_data)
            self.label.setText(message)
        for gadget in self.gadgets:
            if gadget != self.genre_options:
                gadget.clear()
