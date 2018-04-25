# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'room1.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Room1(object):
    def setupUi(self, Room1):
        Room1.setObjectName("Room1")
        Room1.resize(800, 480)
        self.groensld = QtWidgets.QSlider(Room1)
        self.groensld.setGeometry(QtCore.QRect(160, 190, 201, 71))
        self.groensld.setStyleSheet("QSlider::groove:horizontal {\n"
"    border: 1px solid;\n"
"    height: 10px;\n"
"    margin: 0px;\n"
"    }\n"
"QSlider::handle:horizontal {\n"
"    background-color: black;\n"
"    border: 1px solid;\n"
"    height: 40px;\n"
"    width: 40px;\n"
"    margin: -15px 0px;\n"
"    }")
        self.groensld.setSliderPosition(75)
        self.groensld.setOrientation(QtCore.Qt.Horizontal)
        self.groensld.setObjectName("groensld")
        self.rolluik = QtWidgets.QLabel(Room1)
        self.rolluik.setGeometry(QtCore.QRect(370, 210, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.rolluik.setFont(font)
        self.rolluik.setObjectName("rolluik")
        self.groen = QtWidgets.QPushButton(Room1)
        self.groen.setGeometry(QtCore.QRect(10, 190, 131, 71))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.groen.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.groen.setFont(font)
        self.groen.setObjectName("groen")
        self.stand = QtWidgets.QLabel(Room1)
        self.stand.setGeometry(QtCore.QRect(580, 110, 201, 51))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.stand.setFont(font)
        self.stand.setObjectName("stand")
        self.beneden = QtWidgets.QFrame(Room1)
        self.beneden.setGeometry(QtCore.QRect(620, 270, 111, 41))
        self.beneden.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.beneden.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.beneden.setFrameShadow(QtWidgets.QFrame.Raised)
        self.beneden.setObjectName("beneden")
        self.blauw = QtWidgets.QPushButton(Room1)
        self.blauw.setGeometry(QtCore.QRect(10, 280, 131, 71))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(85, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.blauw.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.blauw.setFont(font)
        self.blauw.setObjectName("blauw")
        self.boven = QtWidgets.QFrame(Room1)
        self.boven.setGeometry(QtCore.QRect(620, 170, 111, 41))
        self.boven.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.boven.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.boven.setFrameShadow(QtWidgets.QFrame.Raised)
        self.boven.setObjectName("boven")
        self.status = QtWidgets.QFrame(Room1)
        self.status.setGeometry(QtCore.QRect(160, 370, 111, 41))
        self.status.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.status.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.status.setFrameShadow(QtWidgets.QFrame.Raised)
        self.status.setObjectName("status")
        self.mid = QtWidgets.QFrame(Room1)
        self.mid.setGeometry(QtCore.QRect(620, 220, 111, 41))
        self.mid.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.mid.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mid.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mid.setObjectName("mid")
        self.rood = QtWidgets.QPushButton(Room1)
        self.rood.setEnabled(True)
        self.rood.setGeometry(QtCore.QRect(10, 100, 131, 71))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.rood.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.rood.setFont(font)
        self.rood.setObjectName("rood")
        self.home = QtWidgets.QPushButton(Room1)
        self.home.setGeometry(QtCore.QRect(0, 0, 141, 61))
        self.home.setObjectName("home")
        self.down = QtWidgets.QPushButton(Room1)
        self.down.setGeometry(QtCore.QRect(500, 240, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.down.setFont(font)
        self.down.setObjectName("down")
        self.roodsld = QtWidgets.QSlider(Room1)
        self.roodsld.setGeometry(QtCore.QRect(160, 100, 201, 71))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.roodsld.sizePolicy().hasHeightForWidth())
        self.roodsld.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(36)
        self.roodsld.setFont(font)
        self.roodsld.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.roodsld.setMouseTracking(False)
        self.roodsld.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.roodsld.setAutoFillBackground(False)
        self.roodsld.setStyleSheet("QSlider::groove:horizontal {\n"
"    border: 1px solid;\n"
"    height: 10px;\n"
"    margin: 0px;\n"
"    }\n"
"QSlider::handle:horizontal {\n"
"    background-color: black;\n"
"    border: 1px solid;\n"
"    height: 40px;\n"
"    width: 40px;\n"
"    margin: -15px 0px;\n"
"    }")
        self.roodsld.setSingleStep(5)
        self.roodsld.setSliderPosition(75)
        self.roodsld.setOrientation(QtCore.Qt.Horizontal)
        self.roodsld.setInvertedAppearance(False)
        self.roodsld.setInvertedControls(False)
        self.roodsld.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.roodsld.setTickInterval(0)
        self.roodsld.setObjectName("roodsld")
        self.blauwsld = QtWidgets.QSlider(Room1)
        self.blauwsld.setGeometry(QtCore.QRect(160, 280, 201, 71))
        self.blauwsld.setStyleSheet("QSlider::groove:horizontal {\n"
"    border: 1px solid;\n"
"    height: 10px;\n"
"    margin: 0px;\n"
"    }\n"
"QSlider::handle:horizontal {\n"
"    background-color: black;\n"
"    border: 1px solid;\n"
"    height: 40px;\n"
"    width: 40px;\n"
"    margin: -15px 0px;\n"
"    }")
        self.blauwsld.setSliderPosition(75)
        self.blauwsld.setOrientation(QtCore.Qt.Horizontal)
        self.blauwsld.setObjectName("blauwsld")
        self.up = QtWidgets.QPushButton(Room1)
        self.up.setGeometry(QtCore.QRect(500, 170, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.up.setFont(font)
        self.up.setObjectName("up")

        self.retranslateUi(Room1)
        QtCore.QMetaObject.connectSlotsByName(Room1)

    def retranslateUi(self, Room1):
        _translate = QtCore.QCoreApplication.translate
        Room1.setWindowTitle(_translate("Room1", "kamer1"))
        self.rolluik.setText(_translate("Room1", "Rolluik"))
        self.groen.setText(_translate("Room1", "Groen"))
        self.stand.setText(_translate("Room1", "stand rolluik"))
        self.blauw.setText(_translate("Room1", "Blauw"))
        self.rood.setText(_translate("Room1", "Rood"))
        self.home.setText(_translate("Room1", "Return"))
        self.down.setText(_translate("Room1", "↓"))
        self.up.setText(_translate("Room1", "↑"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Room1 = QtWidgets.QDialog()
    ui = Ui_Room1()
    ui.setupUi(Room1)
    Room1.show()
    sys.exit(app.exec_())

