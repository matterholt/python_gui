import sys
from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':
    # list of parameter of arguments from a comand line
    app = QApplication(sys.argv)

    w = QWidget()
    w.setGeometry(100, 100, 700, 250)
    #w.resize(550, 150)
    #w.move(300, 300)
    w.setWindowTitle('Simple')
    w.show()

    sys.exit(app.exec_())
