import sys
from PyQt5 import uic, QtWidgets
import main_program

class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        uic.loadUi('main_gui.ui', self)
        self.dwn_btn.clicked.connect(self.dwn_btn_func)
        self.con_btn.clicked.connect(self.con_btn_func)
        self.exit_btn.clicked.connect(self.exit_btn_func)
        self.show()

    def dwn_btn_func(self):
        main_program.adb_download()

    def con_btn_func(self):
        text = main_program.adb_connection().device_info()
        print(text)
        self.con_output.setPlainText(str(text))

    def exit_btn_func(self):
        main_program.exit()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    sys.exit(app.exec_())