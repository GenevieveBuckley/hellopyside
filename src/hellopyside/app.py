"""
My first application
"""
import sys
from PySide2 import QtWidgets


class hellopyside(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('hellopyside')
        self.show()

def main():
    app = QtWidgets.QApplication(sys.argv)
    main_window = hellopyside()
    sys.exit(app.exec_())
