# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'oField.ui'
#
# Created: Tue Mar 26 23:39:05 2013
#      by: PyQt4 UI code generator 4.9.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(372, 237)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.graphicsView = QtGui.QGraphicsView(self.centralwidget)
        self.graphicsView.setEnabled(True)
        self.graphicsView.setMinimumSize(QtCore.QSize(80, 80))
        self.graphicsView.setMaximumSize(QtCore.QSize(80, 80))
        self.graphicsView.setBaseSize(QtCore.QSize(80, 80))
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.horizontalLayout_2.addWidget(self.graphicsView)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.lcd_time = QtGui.QLCDNumber(self.centralwidget)
        self.lcd_time.setMinimumSize(QtCore.QSize(120, 0))
        self.lcd_time.setMaximumSize(QtCore.QSize(16777215, 80))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lcd_time.setFont(font)
        self.lcd_time.setAutoFillBackground(True)
        self.lcd_time.setObjectName(_fromUtf8("lcd_time"))
        self.horizontalLayout_2.addWidget(self.lcd_time)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.b_restart = QtGui.QPushButton(self.centralwidget)
        self.b_restart.setObjectName(_fromUtf8("b_restart"))
        self.verticalLayout.addWidget(self.b_restart)
        self.b_close = QtGui.QPushButton(self.centralwidget)
        self.b_close.setObjectName(_fromUtf8("b_close"))
        self.verticalLayout.addWidget(self.b_close)
        spacerItem2 = QtGui.QSpacerItem(20, 10, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout_2.setStretch(4, 10)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.b_pose_1 = QtGui.QPushButton(self.centralwidget)
        self.b_pose_1.setMouseTracking(False)
        self.b_pose_1.setDefault(False)
        self.b_pose_1.setFlat(False)
        self.b_pose_1.setObjectName(_fromUtf8("b_pose_1"))
        self.verticalLayout_2.addWidget(self.b_pose_1)
        self.b_pose_2 = QtGui.QPushButton(self.centralwidget)
        self.b_pose_2.setObjectName(_fromUtf8("b_pose_2"))
        self.verticalLayout_2.addWidget(self.b_pose_2)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.b_pose_3 = QtGui.QPushButton(self.centralwidget)
        self.b_pose_3.setObjectName(_fromUtf8("b_pose_3"))
        self.verticalLayout_4.addWidget(self.b_pose_3)
        self.b_pose_4 = QtGui.QPushButton(self.centralwidget)
        self.b_pose_4.setObjectName(_fromUtf8("b_pose_4"))
        self.verticalLayout_4.addWidget(self.b_pose_4)
        self.b_pose_5 = QtGui.QPushButton(self.centralwidget)
        self.b_pose_5.setObjectName(_fromUtf8("b_pose_5"))
        self.verticalLayout_4.addWidget(self.b_pose_5)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.gridLayout.addLayout(self.horizontalLayout, 9, 0, 1, 1)
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.gridLayout.addWidget(self.lineEdit, 2, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 372, 20))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menu = QtGui.QMenu(self.menubar)
        self.menu.setObjectName(_fromUtf8("menu"))
        self.menu_2 = QtGui.QMenu(self.menubar)
        self.menu_2.setObjectName(_fromUtf8("menu_2"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.action = QtGui.QAction(MainWindow)
        self.action.setCheckable(False)
        self.action.setObjectName(_fromUtf8("action"))
        self.action_2 = QtGui.QAction(MainWindow)
        self.action_2.setObjectName(_fromUtf8("action_2"))
        self.action_3 = QtGui.QAction(MainWindow)
        self.action_3.setObjectName(_fromUtf8("action_3"))
        self.menu.addAction(self.action)
        self.menu_2.addAction(self.action_2)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.b_close, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.close)
        QtCore.QObject.connect(self.action, QtCore.SIGNAL(_fromUtf8("activated()")), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "OpenField Loger", None))
        self.b_restart.setText(_translate("MainWindow", "Рестарт", None))
        self.b_close.setText(_translate("MainWindow", "Выход", None))
        self.b_pose_1.setText(_translate("MainWindow", "Бег по периферии (D)", None))
        self.b_pose_2.setText(_translate("MainWindow", "Бег в центре (F)", None))
        self.b_pose_3.setText(_translate("MainWindow", "Умывание (J)", None))
        self.b_pose_4.setText(_translate("MainWindow", "Стойка (K)", None))
        self.b_pose_5.setText(_translate("MainWindow", "Замирание (L)", None))
        self.lineEdit.setText(_translate("MainWindow", "описание мыши", None))
        self.menu.setTitle(_translate("MainWindow", "Файл", None))
        self.menu_2.setTitle(_translate("MainWindow", "Справка", None))
        self.action.setText(_translate("MainWindow", "Выход", None))
        self.action_2.setText(_translate("MainWindow", "О программе", None))
        self.action_3.setText(_translate("MainWindow", "FAQ", None))

