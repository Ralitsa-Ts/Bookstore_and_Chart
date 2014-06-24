import sys
import os
sys.path.append("model")
from library import Library, Book
from PyQt4 import QtGui, QtCore
from add_book import AddBook
from remove_book import RemoveBook
from book_information import BookInformation
from chart import Chart

  
class Main(QtGui.QWidget):
    def __init__(self):
        super(Main, self).__init__()
        self.InitUI()

    def InitUI(self):
        Library()
        tab_widget = Tabs()
        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(tab_widget)
        self.setLayout(vbox)


class About(QtGui.QDialog):
    """
        Sets the About window
    """
    def __init__(self, parent):
        super(About, self).__init__(parent)
        self.resize(300, 300)
        self.setMinimumSize(300, 300)
        self.setMaximumSize(500, 500)
        self.setWindowTitle("About")
        self.setWindowIcon(QtGui.QIcon(os.path.normpath("images/about.png")))


class Interface(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(Interface, self).__init__(parent)
        self.about = os.path.normpath("images/about.png")
        self.book = os.path.normpath("images/book.png")
        self.background1 = os.path.normpath("images/background1.jpg")
        self.background2 = os.path.normpath("images/background2.jpg")
        self.exit = os.path.normpath("images/exit.png")
        self.styles = os.path.normpath("images/style.png")
        self.InitUI()

    def InitUI(self):
        self.resize(950, 800)
        self.setMinimumSize(950, 800)
        self.setMaximumSize(1000, 950)
        self.setWindowTitle('BookStore and Chart')
        self.setWindowIcon(QtGui.QIcon(self.book))
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
        self.exitAction = QtGui.QAction(QtGui.QIcon(self.exit), '&Exit', self)
        self.aboutAction = QtGui.QAction(QtGui.QIcon(self.about), '&About',
                                         self)
        self.styleAction = QtGui.QAction(QtGui.QIcon(self.styles), '&Style',
                                         self)

        actions = [self.exitAction, self.aboutAction, self.styleAction]
        shortcuts = ['Ctrl+Q', 'Ctrl+A', 'Ctrl+S']
        tips = ['Exit application', 'About application', 'Change style']
        connections = [QtGui.qApp.quit, self.about_app, self.change_style]
        self.create_actions(actions, shortcuts, tips, connections)

    def create_actions(self, actions, shortcuts, tips, connections):
        for action, shortcut, tip, connection in zip(actions, shortcuts,
                                                     tips, connections):
            action.setShortcut(shortcut)
            action.setStatusTip(tip)
            action.triggered.connect(connection)
        self.statusBar()
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&Actions')
        self.toolbar = self.addToolBar('Exit')
        self.toolbar.setIconSize(QtCore.QSize(48, 48))
        for action in actions:
            fileMenu.addAction(action)
            self.toolbar.addAction(action)

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

    def about_app(self):
        self.inf = About(self)
        self.inf.show()

    def style_sheet1(self):
        with open(os.path.normpath("styles/style_sheet1.txt"), "r") as style:
            self.setStyleSheet(style.read())
        self.palette.setBrush(QtGui.QPalette.Background,
                              QtGui.QBrush(QtGui.QPixmap(self.background2)))
        self.setPalette(self.palette)

    def style_sheet2(self):
        with open(os.path.normpath("styles/style_sheet2.txt"), "r") as style:
            self.setStyleSheet(style.read())
        self.palette.setBrush(QtGui.QPalette.Background,
                              QtGui.QBrush(QtGui.QPixmap(self.background1)))
        self.setPalette(self.palette)

    def change_style(self):
        if self.style is True:
            self.style_sheet1()
            self.style = False
        else:
            self.style_sheet2()
            self.style = True


class Tabs(QtGui.QWidget):
    def __init__(self):
        super(Tabs, self).__init__()
        self.InitUI()

    def InitUI(self):
        tab_widget = QtGui.QTabWidget()
        add_book = AddBook()
        remove_book = RemoveBook()
        information = BookInformation()
        charts = Chart()

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
