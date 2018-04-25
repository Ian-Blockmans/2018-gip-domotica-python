# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'camera.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import PyQt5.QtWebKitWidgets as Qweb
from PyQt5.QtWebKit import QWebSettings

class Ui_Camera(object):
    def setupUi(self, Camera):
        Camera.setObjectName("Camera")
        Camera.resize(800, 480)
        self.web = Qweb.QWebView(Camera)
        settings = QWebSettings.globalSettings()
        settings.setAttribute(QWebSettings.PluginsEnabled, True)
        settings.setAttribute(QWebSettings.AutoLoadImages, True)
        self.web.load(QtCore.QUrl("http://192.168.1.215/TinyIB/"))
        self.web.setGeometry(QtCore.QRect(0, 40, 801, 441))
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

