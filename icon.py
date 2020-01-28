import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'test two the Icon'
        self.width = 200
        self.height = 550

        self.initUI()

    def initUI(self):

        self.setGeometry(200, 200, self.height, self.width)
        self.setWindowTitle(self.title)
        self.setWindowIcon(QIcon('web.png'))

        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
