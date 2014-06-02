import sys
import os
sys.path.append("model")
from library import Library, Book
from PyQt4 import QtGui, QtCore

ABOUT = os.path.normpath("images/about.png")
AUTHOR = os.path.normpath("images/author.jpg")
BOOK = os.path.normpath("images/book.png")
BACKGROUND1 = os.path.normpath("images/background1.jpg")
BACKGROUND2 = os.path.normpath("images/background2.jpg")
BOOK_REMOVE = os.path.normpath("images/book-remove.jpg")
BOOKS = os.path.normpath("images/books.png")
COPIES = os.path.normpath("images/copies.jpg")
EXIT = os.path.normpath("images/exit.png")
GENRES = os.path.normpath("images/genres.jpg")
RATING = os.path.normpath("images/rating.png")
STYLE = os.path.normpath("images/style.png")
TITLE = os.path.normpath("images/title.jpg")
FOLDER = os.path.normpath("images/folder.jpg")
YEAR = os.path.normpath("images/year.jpg")

STYLE_SHEET1 = os.path.normpath("styles/style_sheet1.txt")
STYLE_SHEET2 = os.path.normpath("styles/style_sheet2.txt")
POSSIBLE_GENRES = ["Fantasy", "Crime", "Thriller", "Romance", "Other"]

DATABASE = "model/database.txt"
LIBRARY = Library(DATABASE, POSSIBLE_GENRES)


class Main(QtGui.QWidget):
    def __init__(self):
        super(Main, self).__init__()
        self.InitUI()

    def InitUI(self):
        tab_widget = Tabs()
        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(tab_widget)
        self.setLayout(vbox)


class About(QtGui.QDialog):
    def __init__(self, parent):
        super(About, self).__init__(parent)
        self.resize(300, 300)
        self.setMinimumSize(300, 300)
        self.setMaximumSize(500, 500)
        self.setWindowTitle("About")
        self.setWindowIcon(QtGui.QIcon(ABOUT))


class Interface(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(Interface, self).__init__(parent)
        self.InitUI()

    def InitUI(self):
        self.resize(900, 700)
        self.setMinimumSize(900, 700)
        self.setMaximumSize(1000, 950)
        self.setWindowTitle('BookStore and Chart')
        self.setWindowIcon(QtGui.QIcon(BOOK))
        self.center()

        self.palette = QtGui.QPalette()
        self.style = False
        self.change_style()

        self.manage_bars()
        central_widget = Main()
        self.setCentralWidget(central_widget)
        self.show()

    def center(self):
        rectangle = self.frameGeometry()
        center_point = QtGui.QDesktopWidget().availableGeometry().center()
        rectangle.moveCenter(center_point)
        self.move(rectangle.topLeft())

    def manage_bars(self):
        exitAction = QtGui.QAction(QtGui.QIcon(EXIT), '&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(QtGui.qApp.quit)

        aboutAction = QtGui.QAction(QtGui.QIcon(ABOUT), '&About', self)
        aboutAction.setShortcut('Ctrl+A')
        aboutAction.setStatusTip('About application')
        aboutAction.triggered.connect(self.about)

        styleAction = QtGui.QAction(QtGui.QIcon(STYLE), '&Style', self)
        styleAction.setShortcut('Ctrl+S')
        styleAction.setStatusTip('Change style')
        styleAction.triggered.connect(self.change_style)
        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&Actions')
        fileMenu.addAction(exitAction)
        fileMenu.addAction(styleAction)
        fileMenu.addAction(aboutAction)

        self.toolbar = self.addToolBar('Exit')
        self.toolbar.setIconSize(QtCore.QSize(48, 48))
        self.toolbar.addAction(exitAction)
        self.toolbar.addAction(styleAction)
        self.toolbar.addAction(aboutAction)

    def closeEvent(self, event):
        reply = QtGui.QMessageBox.question(self, 'Quit', "Are you sure you " +
                                           "want to quit?",
                                           QtGui.QMessageBox.Yes |
                                           QtGui.QMessageBox.No,
                                           QtGui.QMessageBox.Yes)
        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def about(self):
        self.inf = About(self)
        self.inf.show()

    def style_sheet1(self):
        with open(STYLE_SHEET1, "r") as style1:
            self.setStyleSheet(style1.read())
        self.palette.setBrush(QtGui.QPalette.Background,
                              QtGui.QBrush(QtGui.QPixmap(BACKGROUND2)))
        self.setPalette(self.palette)

    def style_sheet2(self):
        with open(STYLE_SHEET2, "r") as style2:
            self.setStyleSheet(style2.read())
        self.palette.setBrush(QtGui.QPalette.Background,
                              QtGui.QBrush(QtGui.QPixmap(BACKGROUND1)))
        self.setPalette(self.palette)

    def change_style(self):
        if self.style is True:
            self.style_sheet1()
            self.style = False
        else:
            self.style_sheet2()
            self.style = True


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
        LIBRARY.remove_book(book)
        for edit in (self.titleEdit, self.authorEdit, self.yearEdit):
            edit.clear()


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
        Search.clicked.connect(self.update_table)

        vBoxlayout = QtGui.QVBoxLayout()
        vBoxlayout.addLayout(self.grid)
        self.setLayout(vBoxlayout)

    def update_table(self):
        search = self.searchEdit.text()
        if self.author.isChecked():
            results = LIBRARY.book_information_by_author(search)
        elif self.title.isChecked():
            results = LIBRARY.book_information_by_title(search)
        else:
            pass
        table = QtGui.QTableWidget(len(results), 9, self)
        headers = ("Title", "Author's name", "Published in", "Rating",
                   "Copies", "Genre", "Get", "Return", "Vote")
        table.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        table.setHorizontalHeaderLabels(headers)
        table.resizeColumnsToContents()
        table.resizeRowsToContents()

        table.setColumnWidth(0, 160)
        table.setColumnWidth(1, 160)
        table.setColumnWidth(2, 90)
        table.setColumnWidth(3, 50)
        table.setColumnWidth(4, 50)
        table.setColumnWidth(5, 90)
        table.setColumnWidth(6, 40)
        table.setColumnWidth(6, 60)
        table.horizontalHeader().setStretchLastSection(True)
        #table.horizontalHeader().setResizeMode(QtGui.QHeaderView.Stretch)
        for row in range(len(results)):
            book = results[row]
            col = 0
            for column in (book.title, book.author, book.year, book.rating,
                           book.number_of_copies, book.genre):
                item = QtGui.QTableWidgetItem(str(column))
                table.setItem(row, col, item)
                col += 1

        for row in range(len(results)):
            btn = QtGui.QPushButton("Get")
            btn.setMinimumSize(50, 30)
            btn2 = QtGui.QPushButton("Return")
            btn2.setMinimumSize(50, 30)
            table.setCellWidget(row, 6, btn)
            table.setCellWidget(row, 7, btn2)

        self.grid.addWidget(table, 1, 0)


class Tabs(QtGui.QWidget):
    def __init__(self):
        super(Tabs, self).__init__()
        self.InitUI()

    def InitUI(self):
        tab_widget = QtGui.QTabWidget()
        add_book = AddBook()
        remove_book = RemoveBook()
        information = BookInformation()
        charts = QtGui.QWidget()

        tab_widget.resize(500, 500)
        tab_widget.addTab(add_book, "Add new book")
        tab_widget.addTab(remove_book, "Remove a book")
        tab_widget.addTab(information, "Information")
        tab_widget.addTab(charts, "Charts")

        main_layout = QtGui.QVBoxLayout()
        main_layout.addWidget(tab_widget)
        self.setLayout(main_layout)


def main():
    app = QtGui.QApplication(sys.argv)
    interface = Interface()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
