from uifiles.main import Ui_MainWindow
from uifiles.winner import Ui_cong_dialog
from uifiles.control import Ui_Control
from PyQt5 import QtCore, QtGui, QtWidgets
from modules import core
import sys

import random

class Winner(Ui_cong_dialog):
    def setup(self, dialog):
        self.dialog = dialog
        self.button_ok.clicked.connect(self.dialog.close)
        # self.button_ok.clicked.connect(self.okClicked)
        pass
    # def okClicked
    def show(self, text):
        self.team_name.setText(text)
        self.dialog.showFullScreen()
        self.dialog.exec_()
        pass

class Control(Ui_Control):
    def setup(self, dialog, mainwindow):
        self.main = mainwindow
        self.dialog = dialog
        self.pushButton.clicked.connect(self.pushbutton)

        self.startButton.clicked.connect(self.main.button_shuffle)
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

        self.teamA_list = self.main.teamA_list









        self.buttonL.clicked.connect(self.main.button_L)
        self.buttonR.clicked.connect(self.main.button_R)
        self.vsButton.clicked.connect(self.main.button_vs)
        self.nextButton.clicked.connect(self.main.button_next)
        # self.button_ok.clicked.connect(self.okClicked)

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

    def labelA_clicked(self, e):
        self.labelA_f = self.switch_label(self.labelA, self.labelA_f)
        self.main.labelA_f = self.switch_label(self.main.labelA, self.main.labelA_f)
    def labelB_clicked(self, e):
        self.labelB_f = self.switch_label(self.labelB, self.labelB_f)
        self.main.labelB_f = self.switch_label(self.main.labelB, self.main.labelB_f)
    def labelC_clicked(self, e):
        self.labelC_f = self.switch_label(self.labelC, self.labelC_f)
        self.main.labelC_f = self.switch_label(self.main.labelC, self.main.labelC_f)
    def labelD_clicked(self, e):
        self.labelD_f = self.switch_label(self.labelD, self.labelD_f)
        self.main.labelD_f = self.switch_label(self.main.labelD, self.main.labelD_f)
    def labelE_clicked(self, e):
        self.labelE_f = self.switch_label(self.labelE, self.labelE_f)
        self.main.labelE_f = self.switch_label(self.main.labelE, self.main.labelE_f)
    def labelF_clicked(self, e):
        self.labelF_f = self.switch_label(self.labelF, self.labelF_f)
        self.main.labelF_f = self.switch_label(self.main.labelF, self.main.labelF_f)
    def labelG_clicked(self, e):
        self.labelG_f = self.switch_label(self.labelG, self.labelG_f)
        self.main.labelG_f = self.switch_label(self.main.labelG, self.main.labelG_f)
    def labelH_clicked(self, e):
        self.labelH_f = self.switch_label(self.labelH, self.labelH_f)
        self.main.labelH_f = self.switch_label(self.main.labelH, self.main.labelH_f)
    def labelI_clicked(self, e):
        self.labelI_f = self.switch_label(self.labelI, self.labelI_f)
        self.main.labelI_f = self.switch_label(self.main.labelI, self.main.labelI_f)
    def labelJ_clicked(self, e):
        self.labelJ_f = self.switch_label(self.labelJ, self.labelJ_f)
        self.main.labelJ_f = self.switch_label(self.main.labelJ, self.main.labelJ_f)
    def switch_label(self, label, flag):
        if not flag:
            label.setStyleSheet("background-color:red")
            return True
        else:
            label.setStyleSheet("")
            return False







    def pushbutton(self):
        self.main.labelA.setText("AAAAAAAA")


    def show(self):
        self.dialog.show()
        # self.dialog.exec_()


class Main(Ui_MainWindow):


    def setup(self):


        self.d = core.csv2dict("data/test_data.csv")
        self.startButton.clicked.connect(self.button_shuffle)
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.shuffle)
        self.buttonL.clicked.connect(self.button_L)
        self.buttonR.clicked.connect(self.button_R)
        self.vsButton.clicked.connect(self.button_vs)
        self.nextButton.clicked.connect(self.button_next)

        self.textline_timer = QtCore.QTimer()
        self.textline_timer.timeout.connect(self.set_textline)


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
            # QtWidgets.QMessageBox.information(None,"Info", "WIN {}".format(text))
            dialog = QtWidgets.QDialog()
            cong_dialog = Winner()
            cong_dialog.setupUi(dialog)
            cong_dialog.setup(dialog)
            cong_dialog.show("Team " + text + "!!!")
            self.vsButton.setEnabled(True)
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

        self.d.update(self.tmp_members)
        self.random_names += list(self.tmp_members.keys())
        random.shuffle(self.random_names)

        #debug
        # print("残りめんば　{}人".format(len(self.random_names)))
        # print("------------------------------------------------ ")
        # for a in self.random_names:
        #     print(a)
        # print("------------------------------------------------ ")
        # print("")


    def button_R(self):
        old = int(self.pointR.text())
        old += 1
        self.pointR.setText(str(old))
        self.check_win(old, self.labelR.text())

    def shuffle_init(self):
        clone_d = self.d.copy()
        l = []
        for a in clone_d:
            l.append(a)
        random.shuffle(l)
        self.random_names = l

    def submit_team(self):
        self.tmp_members = {}
        selected = self.selected_teams()
        #参加者たちを一時的に退避
        enable_members = self.teams[selected[0]] + self.teams[selected[1]]
        for m in enable_members:
            ret = self.d.get(m)
            if ret:
                self.tmp_members[m] = self.d[m]
                del self.d[m]
                del self.random_names[self.random_names.index(m)]
                #TODO add end process. tmp_members back to self.d


    def button_next(self):

        p = self.random_names.pop(0)
        print("答え: " + p)
        textlines_text = '\n'.join(self.d[p])
        self.text_iter = iter(textlines_text)
        self.iter_all = ""

        del self.d[p]

        timeout_time = (self.max_sec.value() * 1000) / len(textlines_text)
        self.textline_timer.start(timeout_time)


    def set_textline(self):
        try:
            self.iter_all += self.text_iter.__next__()
            self.textEdit.setText(self.iter_all)
        except StopIteration as e:
            self.textline_timer.stop()


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
            return False

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
        self.max_card_num = int(self.spinBox.value())
        selected = self.selected_teams()
        if not selected:
            return

        if selected:
            self.tabWidget.setCurrentIndex(0)
            self.labelL.setText(selected[0])
            self.labelR.setText(selected[1])

        self.pointL.setText(str(0))
        self.pointR.setText(str(0))

        self.submit_team()
        self.label_reset()
        self.vsButton.setDisabled(True)

    def button_shuffle(self):

        if not self.is_start:
            self.is_start = True
            self.startButton.setText("STOP")
            self.timer.start(self.shuffle_speed.value())
        else:
            self.is_start = False
            # self.startButton.setText("START")
            self.startButton.setDisabled(True)
            self.timer.stop()
            self.shuffle_init()

    def shuffle(self):
        members = list(self.d.keys())
        member_num = int(self.shuffle_num.text())
        teams = core.get_teams(members, member_num)
        team_map = [chr(i) for i in range(65, 65 + 26)]

        team_objects = [self.teamA_list, self.teamB_list, self.teamC_list, self.teamD_list, self.teamE_list,
                        self.teamF_list, self.teamG_list, self.teamH_list, self.teamI_list, self.teamJ_list]

        #?
        self.team_objects = team_objects
        for key in teams:
            team_objects[team_map.index(key)].clear()
            for t in teams[key]:
                # print(key, t)
                team_objects[team_map.index(key)].addItem(t)
        self.teams = teams

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Main()
    ui.setupUi(MainWindow)
    ui.setup()

    # sub_dialog = QtWidgets.QDialog()
    # control = Control()
    # control.setupUi(sub_dialog)
    # control.setup(sub_dialog, ui)
    # control.show()

    MainWindow.show()
    #MainWindow.showFullScreen()
    sys.exit(app.exec_())
