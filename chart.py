import sys
import matplotlib.pyplot as plt
import numpy as np
import pylab as pl
sys.path.append("model")
from library import Library
from PyQt4 import QtGui, QtCore
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as Fig
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QTAgg as Nav


class Navigation(Nav):
    toolitems = [t for t in Nav.toolitems if t[0] in ('Back',
                 'Forward', 'Pan', 'Zoom', 'Save', 'Subplots')]


class Window(QtGui.QDialog):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        self.figure = plt.figure(1, facecolor="white", figsize=(6, 5))
        self.canvas = Fig(self.figure)
        self.toolbar = Navigation(self.canvas, self, coordinates=False)
        layout = QtGui.QVBoxLayout()
        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)
        self.setLayout(layout)

    def line_chart(self):
        self.figure.clf()
        self.get_data()
        ax = self.figure.add_subplot(1, 1, 1)
        ax.hold(False)
        sorted(self.count)
        ax.plot(range(len(self.count)), self.count, '*-')
        pl.xticks(np.arange(len(self.genres)), self.genres, rotation=90)
        pl.yticks(np.arange(len(self.genres)), range(max(self.count) + 1),
                  rotation=45)
        plt.tight_layout()
        self.canvas.draw()

    def pie(self):
        self.figure.clf()
        self.get_data()
        pie_data = {k: v for k, v in self.data.items() if v != 0}
        count = list(pie_data.values())
        ax = self.figure.add_subplot(1, 1, 1)
        labels = pie_data.keys()
        ax.pie(count, labeldistance=1, autopct='%1.1f%%')
        plt.legend(labels, loc="best")
        plt.tight_layout()
        self.canvas.draw()

    def get_data(self):
        self.data = Library.number_of_books_by_genres()
        self.genres = sorted(self.data.keys())
        self.count = list(self.data[genre] for genre in self. genres)


class Chart(QtGui.QWidget):
    def __init__(self):
        super(Chart, self).__init__()
        self.InitUI()

    def InitUI(self):
        self.pie_chart = QtGui.QRadioButton("pie chart")
        self.line_chart = QtGui.QRadioButton("line chart")
        self.generate = QtGui.QPushButton('Generate')
        self.generate.clicked.connect(self.show_data)
        self.generate.setMinimumSize(80, 30)

        self.pie_chart.setChecked(True)
        box = QtGui.QVBoxLayout()
        box.addWidget(self.pie_chart)
        box.addWidget(self.line_chart)
        box.addWidget(self.generate)
        label = QtGui.QLabel("Choose your type of chart:")
        self.figure = Window()

        grid = QtGui.QGridLayout()
        grid.addWidget(label, 0, 0)
        grid.addLayout(box, 0, 1)
        grid.addWidget(self.figure, 1, 2)

        grid.setColumnStretch(0, 5)
        grid.setColumnStretch(1, 0)
        grid.setRowStretch(1, 1)

        vBoxlayout = QtGui.QVBoxLayout()
        vBoxlayout.addLayout(grid)
        self.setLayout(vBoxlayout)

    def show_data(self):
        if self.pie_chart.isChecked():
            self.figure.pie()
        else:
            self.figure.line_chart()
