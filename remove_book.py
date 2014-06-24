import sys
import os
sys.path.append("model")
from library import Library, Book
from PyQt4 import QtGui, QtCore
from book_validations import Validations

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
        pixmaps = (self.title, self.author, self.year, self.genre)

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
        image.setPixmap(QtGui.QPixmap(self.book_remove))
        image.setFixedWidth(200)
        image.setFixedHeight(200)

        window = QtGui.QMainWindow()
        self.statusBar = QtGui.QStatusBar()
        self.label = QtGui.QLabel()
        self.statusBar.addWidget(self.label)
        window.setStatusBar(self.statusBar)

        grid = QtGui.QGridLayout()
        grid.addLayout(form, 0, 0)
        grid.addLayout(form1, 0, 1)
        grid.addWidget(image, 0, 2)
        grid.addWidget(window, 1, 0)
        grid.setSpacing(10)
        grid.setColumnStretch(0, 5)
        grid.setColumnStretch(1, 2)
        grid.setRowStretch(1, 1)

        vBoxlayout = QtGui.QVBoxLayout()
        vBoxlayout.addLayout(grid)
        self.setLayout(vBoxlayout)

    def removeBook(self):
        data = [self.titleEdit.text(), self.authorEdit.text(),
                self.yearEdit.text(), self.genre_options.currentText()]

        invalid_data = Validations.check_all(*data)
        if invalid_data == '':
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
