import sys
import os
sys.path.append("model")
from library import Library, Book
from PyQt4 import QtGui, QtCore
from validations import Validations


class RemoveBook(QtGui.QWidget):
    def __init__(self):
        super(RemoveBook, self).__init__()
        self.genres = Library.genres
        self.set_image_paths()
        self.InitUI()

    def set_image_paths(self):
        self.author = os.path.normpath("images/author.jpg")
        self.book_remove = os.path.normpath("images/book-remove.jpg")
        self.genre = os.path.normpath("images/genres.jpg")
        self.title = os.path.normpath("images/title.jpg")
        self.year = os.path.normpath("images/year.jpg")

    def InitUI(self):
        self.set_input_form()
        self.set_icons()
        self.prepare_remove_image()
        self.prepare_statusbar()
        self.fill_in_grid()

    def fill_in_grid(self):
        """
            Fill the gridLayout with all the widgets.
        """
        grid = QtGui.QGridLayout()
        grid.addLayout(self.input_form, 0, 0)
        grid.addLayout(self.icon_form, 0, 1)
        grid.addWidget(self.image, 0, 2)
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

    def prepare_remove_image(self):
        """
            Prepare the image of the book's removal so that it can be added.
        """
        self.image = QtGui.QLabel()
        self.image.setPixmap(QtGui.QPixmap(self.book_remove))
        self.image.setFixedWidth(200)
        self.image.setFixedHeight(200)

    def set_icons(self):
        """
            Set the small icons.
        """
        title_image = QtGui.QLabel()
        author_image = QtGui.QLabel()
        year_image = QtGui.QLabel()
        genre_image = QtGui.QLabel()

        images = (title_image, author_image, year_image, genre_image)
        images_tooltips = ("Use letters only!", "Use letters only!",
                           "Use numbers only!",
                           "Choose from the given options!")
        pixmaps = (self.title, self.author, self.year, self.genre)

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

    def set_input_form(self):
        """
            Set the form where the user will input information about the book.
        """
        self.titleEdit = QtGui.QLineEdit()
        self.authorEdit = QtGui.QLineEdit()
        self.yearEdit = QtGui.QLineEdit()
        self.genre_options = QtGui.QComboBox()
        self.genre_options.addItems(self.genres)

        edits = [self.titleEdit, self.authorEdit, self.yearEdit]
        texts = [" a title", " the author's name", " year of publication"]

        for edit, text in zip(edits, texts):
            edit.setPlaceholderText("click to add" + text)

        Remove = QtGui.QPushButton("Remove")
        Remove.clicked.connect(self.removeBook)
        self.input_form = QtGui.QFormLayout()
        self.input_form.addRow("Title*:", self.titleEdit)
        self.input_form.addRow("Author*:", self.authorEdit)
        self.input_form.addRow("Published in*:", self.yearEdit)
        self.input_form.addRow("Genre:", self.genre_options)
        self.input_form.addRow(" ", Remove)

    def removeBook(self):
        """
            Use the entered information if it is valid in order to remove the
            book after the Add button is pushed.
        """
        data = [self.titleEdit.text(), self.authorEdit.text(),
                self.yearEdit.text(), self.genre_options.currentText()]

        invalid_data = Validations.check_all(*data)
        if invalid_data == []:
            book = Book(self.titleEdit.text(), self.authorEdit.text(),
                        self.yearEdit.text(),
                        self.genre_options.currentText(), 0, 0)
            Library.remove_book(book)
            self.label.setText('You removed the book successfully!')
        else:
            message = "Unsuccessful removal!Invalid:\n"
            message += '\n'.join(invalid_data)
            self.label.setText(message)
        for edit in (self.titleEdit, self.authorEdit, self.yearEdit):
            edit.clear()
