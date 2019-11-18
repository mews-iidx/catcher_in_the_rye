from uifiles.start import Ui_startup
from uifiles.teams import Ui_teams
from uifiles.main import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from modules import core
import sys

class StartGUI(Ui_startup):
    def setup(self, Dialog):
        self.button_ok.clicked.connect(self.button_okClicked)

    def button_okClicked(self):
        print("Click")
        self.show_subwindow()

    def show_subwindow(self):
        self.teams_gui = TeamsGUI()
        dialog = QtWidgets.QDialog()
        # dialog.setWindowFlags(QtCore.Qt.Window)
        dialog.setWindowFlags(QtCore.Qt.WindowMaximizeButtonHint)
        self.teams_gui.setupUi(dialog)
        self.teams_gui.setup(self)
        dialog.exec_()
        print("call exec")

class TeamsGUI(Ui_teams):
    def setup(self, parent=None):
        # self.setWindowFlags(0)
        self.num = parent.spin_members.value()
        self.button_ok.clicked.connect(self.button_okClicked)

    def button_okClicked(self):
        print("clicked teamsGUI ok button. destroy")
        print(self.num)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    startup = QtWidgets.QDialog()
    ui = StartGUI()
    ui.setupUi(startup)
    ui.setup(startup)
    # startup.showFullScreen()
    startup.show()
    sys.exit(app.exec_())
