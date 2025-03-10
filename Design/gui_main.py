import sys
from PyQt5 import QtWidgets
import gui_ver1 as ui  # Import the generated UI file
from Dark import *
from Light import *


class MyWindow(QtWidgets.QMainWindow, ui.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Setup the UI elements

        # Connect the Dark Mode / Light Mode toggle
        self.radioButton.clicked.connect(lambda: self.ChangeStylesheet(self))


    def on_button_click(self):
        print("Connect Clicked!")  # Example action when button is clicked


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
