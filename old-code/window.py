import sys
from PyQt5 import uic, QtWidgets
import main_program
from download import download_functions
import os


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi('main_gui.ui', self)
        self.dwn_btn.clicked.connect(self.dwn_btn_func)
        self.con_btn.clicked.connect(self.con_btn_func)
        self.exit_btn.clicked.connect(self.exit_btn_func)
        self.show()

    def dwn_btn_func(self):
        if not os.path.exists('./adb'):
            download_functions().download_files()

    def con_btn_func(self):
        if os.path.exists('./adb'):
            self.con_output.setPlainText(str('Starting adb server...'))
            text = main_program.adb_connection().device_show_info()
            self.con_output.setPlainText(str(text))

    def exit_btn_func(self):
        main_program.exit()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
