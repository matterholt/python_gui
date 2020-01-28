import sys
from PyQt5.QtWidgets import (QWidget, QToolTip,
                             QPushButton, QApplication,
                             QDesktopWidget, QMessageBox)
from PyQt5.QtGui import QFont


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.height = 500
        self.width = 250

        self.initUI()

    def initUI(self):

        QToolTip.setFont(QFont('SansSerif', 10))

        self.setToolTip('This is a <b> QWidget </b> widget')

        btn = QPushButton('Button', self)
        btn.setToolTip('this is a <b>QPushButton</b> widget')
        btn.resize(btn.sizeHint())
        btn.move(50, 50)

        qbtn = QPushButton('Quit', self)
        # how to confirm quit when on button??
        qbtn.clicked.connect(QApplication.instance().quit)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(50, 70)

        # self.setGeometry(200, 300, self.height, self.width)
        self.setWindowTitle('ToolTips')
        self.show()

    def center(self):

        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        # self.move(qr.topLeft())

    def closeEvent(self, event):

        reply = QMessageBox.question(self, 'Message',
                                     "Are you sure to quit?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
