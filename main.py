# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Main(object):
    def setupUi(self, Main):
        Main.setObjectName("Main")
        Main.resize(800, 480)
        self.kamer2 = QtWidgets.QPushButton(Main)
        self.kamer2.setGeometry(QtCore.QRect(270, 40, 261, 351))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.kamer2.setFont(font)
        self.kamer2.setObjectName("kamer2")
        self.quit = QtWidgets.QPushButton(Main)
        self.quit.setGeometry(QtCore.QRect(0, 0, 801, 41))
        self.quit.setObjectName("quit")
        self.kamer3 = QtWidgets.QPushButton(Main)
        self.kamer3.setGeometry(QtCore.QRect(540, 40, 261, 351))
        self.kamer3.setObjectName("kamer3")
        self.kamer1 = QtWidgets.QPushButton(Main)
        self.kamer1.setGeometry(QtCore.QRect(0, 40, 261, 351))
        self.kamer1.setObjectName("kamer1")
        self.camera = QtWidgets.QPushButton(Main)
        self.camera.setGeometry(QtCore.QRect(0, 430, 801, 41))
        self.camera.setObjectName("camera")
        self.alarm = QtWidgets.QPushButton(Main)
        self.alarm.setGeometry(QtCore.QRect(0, 390, 801, 41))
        self.alarm.setObjectName("alarm")

        self.retranslateUi(Main)
        QtCore.QMetaObject.connectSlotsByName(Main)

    def retranslateUi(self, Main):
        _translate = QtCore.QCoreApplication.translate
        Main.setWindowTitle(_translate("Main", "huis"))
        self.kamer2.setText(_translate("Main", "kamer 2"))
        self.quit.setText(_translate("Main", "Quit"))
        self.kamer3.setText(_translate("Main", "kamer 3"))
        self.kamer1.setText(_translate("Main", "kamer 1"))
        self.camera.setText(_translate("Main", "Camera"))
        self.alarm.setText(_translate("Main", "Alarm"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Main = QtWidgets.QDialog()
    ui = Ui_Main()
    ui.setupUi(Main)
    Main.show()
    sys.exit(app.exec_())

