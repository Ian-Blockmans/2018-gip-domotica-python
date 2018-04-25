# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'camera.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Camera(object):
    def setupUi(self, Camera):
        Camera.setObjectName("Camera")
        Camera.resize(800, 480)
        self.graphicsView = QtWidgets.QGraphicsView(Camera)
        self.graphicsView.setGeometry(QtCore.QRect(0, 40, 801, 441))
        self.graphicsView.setObjectName("graphicsView")
        self.home = QtWidgets.QPushButton(Camera)
        self.home.setGeometry(QtCore.QRect(0, 0, 801, 41))
        self.home.setObjectName("home")

        self.retranslateUi(Camera)
        QtCore.QMetaObject.connectSlotsByName(Camera)

    def retranslateUi(self, Camera):
        _translate = QtCore.QCoreApplication.translate
        Camera.setWindowTitle(_translate("Camera", "alarm"))
        self.home.setText(_translate("Camera", "Return"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Camera = QtWidgets.QDialog()
    ui = Ui_Camera()
    ui.setupUi(Camera)
    Camera.show()
    sys.exit(app.exec_())

