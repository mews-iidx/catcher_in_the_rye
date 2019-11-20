from uifiles.main import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from modules import core
import sys

import random

class Main(Ui_MainWindow):
    def setup(self):
        self.d = core.csv2dict("data/test_data.csv")
        self.startButton.clicked.connect(self.button_shuffle)
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.shuffle)
        self.buttonL.clicked.connect(self.button_L)
        self.buttonR.clicked.connect(self.button_R)



        # self.textline_timer = QtCore.QTimer()
        # self.timer.timeout.connect(self.set_textline)

        self.vsButton.clicked.connect(self.button_vs)
        self.nextButton.clicked.connect(self.button_next)

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
        self.labelH.mousePressEvent = self.labelH_clicked
        self.labelI.mousePressEvent = self.labelI_clicked
        self.labelJ.mousePressEvent = self.labelJ_clicked

    def label_reset(self):
        if self.labelA_f : self.labelA_clicked("hoge")
        if self.labelB_f : self.labelB_clicked("hoge")
        if self.labelC_f : self.labelC_clicked("hoge")
        if self.labelD_f : self.labelD_clicked("hoge")
        if self.labelE_f : self.labelE_clicked("hoge")
        if self.labelF_f : self.labelF_clicked("hoge")
        if self.labelG_f : self.labelG_clicked("hoge")
        if self.labelH_f : self.labelH_clicked("hoge")
        if self.labelI_f : self.labelI_clicked("hoge")
        if self.labelJ_f : self.labelJ_clicked("hoge")

    def check_win(self,  old,  text):
        if old == self.max_card_num:
            QtWidgets.QMessageBox.information(None,"Info", "WIN {}".format(text))
            self.back()

    def button_L(self):
        old = int(self.pointL.text())
        old += 1
        self.pointL.setText(str(old))
        self.check_win(old, self.labelL.text())

    def back(self):
        self.tabWidget.setCurrentIndex(1)
        self.pointL.setText(str(0))
        self.pointR.setText(str(0))

    def button_R(self):
        old = int(self.pointR.text())
        old += 1
        self.pointR.setText(str(old))
        self.check_win(old, self.labelR.text())

    def shuffle_init(self):
        pass

    def submit_team(self):
        clone_d = self.d.copy()
        l = []
        for a in clone_d:
            l.append(a)
        random.shuffle(l)
        selected = self.selected_teams()
        enable_members = self.teams[selected[0]] + self.teams[selected[1]]
        for m in enable_members:
            del clone_d[m]

        self.random_names = l
        print(clone_d)

    def button_next(self):
        import time
        p = self.random_names.pop(0)
        s = '\n'.join(self.d[p])
        print(self.d)
        del self.d[p]
        #TODO TIMER
        # all_text = ''
        # for ss in s:
        #     all_text += ss
        #     self.textEdit.setText(all_text)
        #     time.sleep(0.4)


        self.textEdit.setText(s)


    def selected_teams(self):
        selected = []
        if self.labelA_f:
            selected.append("A")
        if self.labelB_f:
            selected.append("B")
        if self.labelC_f:
            selected.append("C")
        if self.labelD_f:
            selected.append("D")
        if self.labelE_f:
            selected.append("E")
        if self.labelF_f:
            selected.append("F")
        if self.labelG_f:
            selected.append("G")
        if self.labelH_f:
            selected.append("H")
        if self.labelI_f:
            selected.append("I")
        if self.labelJ_f:
            selected.append("J")

        if len(selected) == 2:
            return selected
        else:
            ret = QtWidgets.QMessageBox.warning(None, "警告", "2チームだけ選択してください！！" )

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

    def button_vs(self):
        selected = self.selected_teams()
        self.submit_team()

        if selected:
            self.tabWidget.setCurrentIndex(0)
            self.labelL.setText(selected[0])
            self.labelR.setText(selected[1])

        self.pointL.setText(str(0))
        self.pointR.setText(str(0))

        self.max_card_num = int(self.spinBox.value())
        self.label_reset()

    def button_shuffle(self):

        if not self.is_start:
            self.is_start = True
            self.startButton.setText("STOP")
            self.timer.start(300)
        else:
            self.is_start = False
            self.startButton.setText("START")
            self.timer.stop()
            self.shuffle_init()

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
        self.teams = teams

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Main()
    ui.setupUi(MainWindow)
    ui.setup()

    MainWindow.show()
    sys.exit(app.exec_())
