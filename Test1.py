import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic
from PyQt5 import QtCore, QtGui, QtWidgets

mainwindow_class  = uic.loadUiType("MainWindow.ui")[0]

class MainWindow(QMainWindow, mainwindow_class):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.selector = QStackedWidget(self)


        #selector = self.QtWidgets.QStackedWidget()

        """
        self.QtStack = QtWidgets.QStackedLayout()

        self.stack1 = QtWidgets.QWidget()
        self.stack2 = QtWidgets.QWidget()
        self.stack3 = QtWidgets.QWidget()

        self.Window1UI()
        self.Window2UI()
        self.Window3UI()

        self.QtStack.addWidget(self.stack1)
        self.QtStack.addWidget(self.stack2)
        self.QtStack.addWidget(self.stack3)
        """

    def slot1(self):
        print("Hello QyQt5! slot1")
        #self.selector.setCurrentIndex(2)
        self.selector.setCurrentIndex(1)
        

    
    def slot2(self):
        print("Hello QyQt5! slot2")

    def slot3(self):
        print("Hello QyQt5! slot3")


if __name__ == "__main__":

    app = QApplication(sys.argv)
    mWindow = MainWindow()
    mWindow.show()

    app.exec_()