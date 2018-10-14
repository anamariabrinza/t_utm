import sys
import os
from PyQt4 import QtGui, QtCore


class Window(QtGui.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(50, 50, 500, 300)
        self.setWindowTitle("PyQT tuts!")
        self.setWindowIcon(QtGui.QIcon('icon.png'))
        self.home()

    def home(self):
        btn = QtGui.QPushButton("Quit", self)
        btn.clicked.connect(self.close_application)
        btn.resize(btn.minimumSizeHint())
        btn.move(0, 0)


        btn1 = QtGui.QPushButton("Start", self)
        btn1.clicked.connect(self.start_recog)
        btn1.resize(btn.minimumSizeHint())
        btn1.move(100, 0)
        self.show()

    def close_application(self):
        print("whooaaaa so custom!!!")
        sys.exit()
    def start_recog(self):
        os.system('python.exe detector.py')


def run():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())


run()