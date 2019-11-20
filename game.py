from uifiles.main import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from modules import core
import sys


class Main(Ui_MainWindow):
    def setup(self):
        self.d = core.csv2dict("data/test_data.csv")
        self.startButton.clicked.connect(self.button_shuffle)
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.shuffle)

        self.is_start = False

        self.labelA_f = False
        self.labelB_f = False
        self.labelC_f = False
        self.labelD_f = False
        self.labelE_f = False
        self.labelF_f = False
        self.labelG_f = False
        self.labelH_f = False
        self.labelI_f = False
        self.labelJ_f = False

        self.labelA.mousePressEvent = self.labelA_clicked
        self.labelB.mousePressEvent = self.labelB_clicked
        self.labelC.mousePressEvent = self.labelC_clicked
        self.labelD.mousePressEvent = self.labelD_clicked
        self.labelE.mousePressEvent = self.labelE_clicked
        self.labelF.mousePressEvent = self.labelF_clicked
        self.labelG.mousePressEvent = self.labelG_clicked
        self.labelH.mousePressEvent = self.labelA_clicked
        self.labelI.mousePressEvent = self.labelA_clicked
        self.labelJ.mousePressEvent = self.labelA_clicked

    def labelA_clicked(self, e):
        self.labelA_f = self.switch_label(self.labelA, self.labelA_f)
    def labelB_clicked(self, e):
        self.labelB_f = self.switch_label(self.labelB, self.labelB_f)
    def labelC_clicked(self, e):
        self.labelC_f = self.switch_label(self.labelC, self.labelC_f)
    def labelD_clicked(self, e):
        self.labelD_f = self.switch_label(self.labelD, self.labelD_f)
    def labelE_clicked(self, e):
        self.labelE_f = self.switch_label(self.labelE, self.labelE_f)
    def labelF_clicked(self, e):
        self.labelF_f = self.switch_label(self.labelF, self.labelF_f)
    def labelG_clicked(self, e):
        self.labelG_f = self.switch_label(self.labelG, self.labelG_f)
    def labelH_clicked(self, e):
        self.labelH_f = self.switch_label(self.labelH, self.labelH_f)
    def labelI_clicked(self, e):
        self.labelI_f = self.switch_label(self.labelI, self.labelI_f)
    def labelJ_clicked(self, e):
        self.labelJ_f = self.switch_label(self.labelJ, self.labelJ_f)

    def switch_label(self, label, flag):
        if not flag:
            label.setStyleSheet("background-color:red")
            return True
        else:
            label.setStyleSheet("")
            return False


    def button_shuffle(self):

        if not self.is_start:
            self.is_start = True
            self.startButton.setText("STOP")
            self.timer.start(300)
        else:
            self.is_start = False
            self.startButton.setText("START")
            self.timer.stop()

    def shuffle(self):
        members = list(self.d.keys())
        member_num = int(self.shuffle_num.text())
        teams = core.get_teams(members, member_num)
        team_map = [chr(i) for i in range(65, 65 + 26)]

        team_objects = [self.teamA_list, self.teamB_list, self.teamC_list, self.teamD_list, self.teamE_list,
                        self.teamF_list, self.teamG_list, self.teamH_list, self.teamI_list, self.teamJ_list]

        for key in teams:
            team_objects[team_map.index(key)].clear()
            for t in teams[key]:
                print(key, t)
                team_objects[team_map.index(key)].addItem(t)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Main()
    ui.setupUi(MainWindow)
    ui.setup()

    MainWindow.show()
    sys.exit(app.exec_())
