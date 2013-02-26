'''
Created on 15.02.2013

@author: pilat
'''

import sys
from PyQt4 import QtCore, QtGui
from numpy import zeros,bincount,nonzero,array,int8
from oFieldUi import Ui_MainWindow


class MyForm(QtGui.QMainWindow): 
    def __init__(self, parent=None): 
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.event=self.ui.centralwidget
        
        def eventFilter(self,e):
            print(e.type())
            if e.type() == QtCore.QEvent.KeyPress and e.key() == QtCore.Qt.Key_D:
                print("event filtered")
                self.event.emit(QtCore.SIGNAL("didSomething"), "important", "information")

        self.connect(self.event, QtCore.SIGNAL("didSomething"),
                     self.update_label)
        #self.do_something()

    def update_label(self, value1, value2):
        print (value1 + " " + value2)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())        