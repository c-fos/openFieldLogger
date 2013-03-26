# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'about.ui'
#
# Created: Thu Feb 28 12:22:13 2013
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(490, 260)
        Dialog.setMinimumSize(QtCore.QSize(490, 260))
        Dialog.setMaximumSize(QtCore.QSize(490, 260))
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(10, 230, 471, 24))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.textBrowser = QtGui.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(0, 0, 490, 220))
        self.textBrowser.setMinimumSize(QtCore.QSize(490, 220))
        self.textBrowser.setMaximumSize(QtCore.QSize(490, 220))
        self.textBrowser.setBaseSize(QtCore.QSize(490, 220))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(230, 230, 230))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(230, 230, 230))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 208, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.textBrowser.setPalette(palette)
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.pushButton.setText(_translate("Dialog", "Закрыть", None))
        self.textBrowser.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600;\">Open field logger</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Версия: <span style=\" font-weight:600;\">0.1</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Автор: <span style=\" font-weight:600;\">Илья Малахин</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Адрес для связи: <span style=\" font-weight:600; font-style:italic;\">pilat1988@gmail.com</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Данная программа распространяется под лицензией <span style=\" font-weight:600;\">GPL</span>-v3.</p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Условия лицензии: <a href=\"http://www.gnu.org/licenses/\"><span style=\" text-decoration: underline; color:#0000ff;\">http://www.gnu.org/licenses/</span></a></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Исходный код: <a href=\"https://github.com/c-fos/openFieldLogger.git\"><span style=\" text-decoration: underline; color:#0000ff;\">http://github.com/c-fos/openFieldLogger.git</span></a></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://github.com/c-fos/openFieldLogger.git\"><span style=\" text-decoration: underline; color:#000000;\">Руководство пользователя: </span></a><a href=\"http://github.com/c-fos/openFieldLogger/wiki\"><span style=\" text-decoration: underline; color:#0000ff;\">http://github.com/c-fos/openFieldLogger/wiki</span></a></p></body></html>", None))

