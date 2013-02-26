'''
Created on 09.02.2013

@author: pilat
'''

import sys
from PyQt4 import QtCore, QtGui
from numpy import zeros,bincount,nonzero,array,int8
from oFieldUi import Ui_MainWindow 
import csv
import datetime


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s
    
#===============================================================================
class myKeyFilter(QtCore.QObject):
    #event = QtCore.pyqtSignal()
    
    def eventFilter(self,  obj,  event):
        if event.type() == QtCore.QEvent.KeyPress:
            if event.key() == QtCore.Qt.Key_D:
                self.emit(QtCore.SIGNAL("D_pressed"))
                print("d key pressed")
                return True
            if event.key() == QtCore.Qt.Key_F:
                self.emit(QtCore.SIGNAL("F_pressed"))
                print("f key pressed")
                return True
            if event.key() == QtCore.Qt.Key_J:
                self.emit(QtCore.SIGNAL("J_pressed"))
                print("j key pressed")
                return True
            if event.key() == QtCore.Qt.Key_K:
                self.emit(QtCore.SIGNAL("K_pressed"))
                print("k key pressed")
                return True
            if event.key() == QtCore.Qt.Key_L:
                self.emit(QtCore.SIGNAL("L_pressed"))
                print("l key pressed")
                return True
        return False
#===============================================================================

        
class MyForm(QtGui.QMainWindow):
    def __init__(self, parent=None):
        
        self.expTime=5
        self.poses=["1","2","3","4","5","6"]
        self.cur_timer=self.expTime*4
        self.zeroTime=self.cur_timer
        self.dataArray=zeros(self.cur_timer,dtype=int8)
        self.lastPose=0 #
        self.color_names = [ "Normal", "Yellow" ]
        self.color_idx = 1
        
        now = datetime.datetime.now()
        self.dateTime=now.strftime("%Y-%m-%d_%H:%M")
        
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.view = self.ui.graphicsView
        self.scene = QtGui.QGraphicsScene()
        
        
        self.filter = myKeyFilter()
        self.ui.centralwidget.installEventFilter(self.filter)
        
        QtCore.QObject.connect(self.ui.b_pose_1, QtCore.SIGNAL(_fromUtf8("clicked()")),\
                self.test)
        QtCore.QObject.connect(self.filter, QtCore.SIGNAL("D_pressed"),\
                self.test)
        QtCore.QObject.connect(self.filter, QtCore.SIGNAL("F_pressed"),\
                self.test2)
        QtCore.QObject.connect(self.filter, QtCore.SIGNAL("J_pressed"),\
                self.test3)
        QtCore.QObject.connect(self.filter, QtCore.SIGNAL("K_pressed"),\
                self.test4)
        QtCore.QObject.connect(self.filter, QtCore.SIGNAL("L_pressed"),\
                self.test5)
        QtCore.QObject.connect(self.ui.b_pose_2, QtCore.SIGNAL(_fromUtf8("clicked()")),\
                self.test2)
        QtCore.QObject.connect(self.ui.b_pose_3, QtCore.SIGNAL(_fromUtf8("clicked()")),\
                self.test3)
        QtCore.QObject.connect(self.ui.b_pose_4, QtCore.SIGNAL(_fromUtf8("clicked()")),\
                self.test4)
        QtCore.QObject.connect(self.ui.b_pose_5, QtCore.SIGNAL(_fromUtf8("clicked()")),\
                self.test5)
        QtCore.QObject.connect(self.ui.b_restart, QtCore.SIGNAL(_fromUtf8("clicked()")),\
                self.restart_timer)
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.showTimer)
        self.timer.start(250)
    
    def plotImg(self,img):
        self.scene.addPixmap(QtGui.QPixmap(img))
        self.view.setScene(self.scene)
        self.view.show()
    
    def showTimer(self):
        text = "%d:%02d" % (self.cur_timer/240,(self.cur_timer/4 % 60))
        self.ui.lcd_time.display(text)
        
        if (self.cur_timer == 0):
            self.color_idx = 3 - self.color_idx
            self.setStyleSheet("QWidget { background-color: YELLOW }")
            self.show()
            self.timer.stop()
            print(self.dataArray)
            y = bincount(array(self.dataArray))
            ii = nonzero(y)[0]
            self.setStyleSheet("QWidget { background-color: NORMAL }")
            self.c = open("{0}.csv".format(self.dateTime), "wb")
            self.c.write(u"{0} \n".format(self.dataArray))
            self.c.write(u"The behavior type name, Duration \n")
            for i in ii:
                print("time in the %s pose: %s seconds \n" % (self.poses[i],y[i]/4.0))
                self.c.write("{0}, {1} \n".format(self.poses[i],y[i]/4.0))
            self.c.close()
        else:
            self.dataArray[self.zeroTime-self.cur_timer]=self.lastPose
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
        self.lastPose=1
        self.plotImg("img/first_pose.png")
    def test2(self):
        self.lastPose=2
        self.plotImg("img/second_pose.png")
    def test3(self):
        self.lastPose=3
        self.plotImg("img/third_pose.png")
    def test4(self):
        self.lastPose=4
        self.plotImg("img/fourth_pose.png")
    def test5(self):
        self.lastPose=5
        self.plotImg("img/fifth_pose.png")
        
    def restart_timer(self):
        self.cur_timer=self.expTime*4
        self.zeroTime=self.cur_timer
        self.dataArray=zeros(self.cur_timer,dtype=int8)
        self.lastPose=0 #
        self.timer.start(250)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())
