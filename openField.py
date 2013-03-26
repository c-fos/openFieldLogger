'''
    Copyright 2013 ilya malakhin
    OpenFieldLogger. The program to logging the animal behavior in the open field test.
    Copyright (C) 09.02.2013  Ilya Malakhin (pilat1988@gmail.com)

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

import sys
from PyQt4 import QtCore, QtGui
from numpy import zeros, bincount, nonzero, array, int8
from oFieldUi import Ui_MainWindow
from about import Ui_Dialog
import datetime


class myKeyFilter(QtCore.QObject):

    def eventFilter(self,  obj,  event):
        if event.type() == QtCore.QEvent.KeyPress:
            print(event.key())
            if event.key() == 68 or event.key() == 1042:  # D key en/ru
                self.emit(QtCore.SIGNAL("D_pressed"))
                print("d key pressed")
                return True
            if event.key() == 70 or event.key() == 1040:  # F key
                self.emit(QtCore.SIGNAL("F_pressed"))
                print("f key pressed")
                return True
            if event.key() == 74 or event.key() == 1054:  # event.key() == QtCore.Qt.Key_J:
                self.emit(QtCore.SIGNAL("J_pressed"))
                print("j key pressed")
                return True
            if event.key() == 75 or event.key() == 1051:  # event.key() == QtCore.Qt.Key_K:
                self.emit(QtCore.SIGNAL("K_pressed"))
                print("k key pressed")
                return True
            if event.key() == 76 or event.key() == 1044:  # event.key() == QtCore.Qt.Key_L:
                self.emit(QtCore.SIGNAL("L_pressed"))
                print("l key pressed")
                return True
        return False


class AboutD(QtGui.QDialog):
    def __init_(self):
        super(AboutD, self).__init__()
        self.dialog = Ui_Dialog()
        self.dialog.setupUi(self)


class MyForm(QtGui.QMainWindow):
    def __init__(self, parent=None):

        self.expTime = 180
        self.cur_timer = self.expTime * 4
        self.zeroTime = self.cur_timer
        self.dataArray = zeros(self.cur_timer, dtype=int8)
        self.lastPose = 0
        self.color_names = ["Normal", "Yellow"]
        self.color_idx = 1

        now = datetime.datetime.now()
        self.dateTime = now.strftime("%Y-%m-%d_%H:%M")

        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.b_pose_1.text()
        self.poses = ["default", self.ui.b_pose_1.text(), self.ui.b_pose_2.text(),
                      self.ui.b_pose_3.text(), self.ui.b_pose_4.text(), self.ui.b_pose_5.text()]

        self.view = self.ui.graphicsView
        self.scene = QtGui.QGraphicsScene()

        self.filter = myKeyFilter()
        self.ui.centralwidget.installEventFilter(self.filter)

        QtCore.QObject.connect(self.ui.b_pose_1, QtCore.SIGNAL("clicked()"),
                               self.test)
        QtCore.QObject.connect(self.filter, QtCore.SIGNAL("D_pressed"),
                               self.test)
        QtCore.QObject.connect(self.filter, QtCore.SIGNAL("F_pressed"),
                               self.test2)
        QtCore.QObject.connect(self.filter, QtCore.SIGNAL("J_pressed"),
                               self.test3)
        QtCore.QObject.connect(self.filter, QtCore.SIGNAL("K_pressed"),
                               self.test4)
        QtCore.QObject.connect(self.filter, QtCore.SIGNAL("L_pressed"),
                               self.test5)
        QtCore.QObject.connect(self.ui.b_pose_2, QtCore.SIGNAL("clicked()"),
                               self.test2)
        QtCore.QObject.connect(self.ui.b_pose_3, QtCore.SIGNAL("clicked()"),
                               self.test3)
        QtCore.QObject.connect(self.ui.b_pose_4, QtCore.SIGNAL("clicked()"),
                               self.test4)
        QtCore.QObject.connect(self.ui.b_pose_5, QtCore.SIGNAL("clicked()"),
                               self.test5)
        QtCore.QObject.connect(self.ui.b_restart, QtCore.SIGNAL("clicked()"),
                               self.restart_timer)
        QtCore.QObject.connect(self.ui.action_2, QtCore.SIGNAL("activated()"),
                               self.showAbout)
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.showTimer)
        self.timer.start(250)

    def showAbout(self):
        #print("show about")
        self.aboutD = QtGui.QDialog()
        self.aboutD.ui = Ui_Dialog()
        self.aboutD.ui.setupUi(self.aboutD)
        self.aboutD.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.aboutD.exec_()

    def plotImg(self, img):
        self.scene.addPixmap(QtGui.QPixmap(img))
        self.view.setScene(self.scene)
        self.view.show()

    def showTimer(self):
        text = "%d:%02d" % (self.cur_timer / 240, (self.cur_timer / 4 % 60))
        self.ui.lcd_time.display(text)

        if (self.cur_timer == 0):
            self.color_idx = 3 - self.color_idx
            self.setStyleSheet("QWidget { background-color: YELLOW }")
            self.show()
            self.timer.stop()
            print((self.dataArray))
            y = bincount(array(self.dataArray))
            ii = nonzero(y)[0]
            self.setStyleSheet("QWidget { background-color: NORMAL }")
            self.c = open("./Results/{0}.csv".format(self.dateTime), "wb")
            self.c.write("{0} \n".format(self.ui.lineEdit.text()).encode('utf-8'))
            self.c.write((str(list(self.dataArray)) + "\n").encode('utf-8'))
            self.c.write("The behavior type name, Duration \n".encode('utf-8'))
            for i in ii:
                print(("time in the %s pose: %s seconds \n" % (self.poses[i], y[i] / 4.0)))
                self.c.write("{0}, {1} \n".format(self.poses[i], y[i] / 4.0).encode('utf-8'))
            self.c.close()
        else:
            self.dataArray[self.zeroTime - self.cur_timer] = self.lastPose
            self.cur_timer -= 1

    def display_image(self, img):
        self.scene.clear()
        w, h = img.size
        self.imgQ = QtGui.QImage(img)  # we need to hold reference to imgQ, or it will crash
        pixMap = QtGui.QPixmap.fromImage(self.imgQ)
        self.scene.addPixmap(pixMap)
        self.view.fitInView(QtCore.QRectF(0, 0, w, h), QtCore.Qt.KeepAspectRatio)
        self.scene.update()

    def test(self):
        self.lastPose = 1
        self.plotImg("img/first_pose.png")

    def test2(self):
        self.lastPose = 2
        self.plotImg("img/second_pose.png")

    def test3(self):
        self.lastPose = 3
        self.plotImg("img/third_pose.png")

    def test4(self):
        self.lastPose = 4
        self.plotImg("img/fourth_pose.png")

    def test5(self):
        self.lastPose = 5
        self.plotImg("img/fifth_pose.png")

    def restart_timer(self):
        self.cur_timer = self.expTime * 4
        self.zeroTime = self.cur_timer
        self.dataArray = zeros(self.cur_timer, dtype=int8)
        self.lastPose = 0
        self.timer.start(250)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())
