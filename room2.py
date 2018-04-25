# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'room2.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Room2(object):
    def setupUi(self, Room2):
        Room2.setObjectName("Room2")
        Room2.resize(800, 480)
        self.home = QtWidgets.QPushButton(Room2)
        self.home.setGeometry(QtCore.QRect(0, 0, 141, 61))
        self.home.setObjectName("home")
        self.aanuit = QtWidgets.QFrame(Room2)
        self.aanuit.setEnabled(True)
        self.aanuit.setGeometry(QtCore.QRect(160, 10, 111, 51))
        self.aanuit.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.aanuit.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.aanuit.setFrameShadow(QtWidgets.QFrame.Raised)
        self.aanuit.setMidLineWidth(-1)
        self.aanuit.setObjectName("aanuit")
        self.light = QtWidgets.QPushButton(Room2)
        self.light.setGeometry(QtCore.QRect(60, 90, 691, 351))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.light.setFont(font)
        self.light.setObjectName("light")

        self.retranslateUi(Room2)
        QtCore.QMetaObject.connectSlotsByName(Room2)

    def retranslateUi(self, Room2):
        _translate = QtCore.QCoreApplication.translate
        Room2.setWindowTitle(_translate("Room2", "kamer2"))
        self.home.setText(_translate("Room2", "Return"))
        self.light.setText(_translate("Room2", "kamer 2"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Room2 = QtWidgets.QDialog()
    ui = Ui_Room2()
    ui.setupUi(Room2)
    Room2.show()
    sys.exit(app.exec_())

