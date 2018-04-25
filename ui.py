import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
import mysql.connector as mysql
import time
import datetime
from main import Ui_Main
from room1 import Ui_Room1
from room2 import Ui_Room2
from room3 import Ui_Room3
from camera2 import Ui_Camera
from keypad import Ui_KeyPad

# connectie maken met de database
conn = mysql.connect(user='root', password='masta', database='gip')
c = conn.cursor()

# veriabele voor de tijd
unix = int(time.time())
date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))

# globale variabelen voor gebruik tussen functies
Ron = False
Gon = False
Bon = False
room3 = False
room2 = False
temp1 = 0
temp2 = 0
asked = 20
Von = False
digit = 0
code = []

# PyQt kleuren
green = QtGui.QColor(0, 255, 0)
red = QtGui.QColor(255, 0, 0)
black = QtGui.QColor(0, 0, 0)


class Main(QDialog):
    def __init__(self):
        super(Main, self).__init__()

        # setup scherm
        self.ui = Ui_Main()
        self.ui.setupUi(self)

        # conecties knoppen met functies
        self.ui.kamer1.clicked.connect(self.change_room1)
        self.ui.kamer2.clicked.connect(self.change_room2)
        self.ui.kamer3.clicked.connect(self.change_room3)
        self.ui.quit.clicked.connect(self.close_application)
        self.ui.camera.clicked.connect(self.change_camera)
        self.ui.alarm.clicked.connect(self.alarm)

        # toon scherm zonder rand
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.move(0, 0)
        self.show()

    def alarm(self):  # toon scherm alarm
        global w
        w = KeyPad()
        w.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        w.move(0, 0)
        w.show()

    def change_room1(self):  # toon scherm kamer1
        global w
        w = Room1()
        w.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        w.move(0, 0)
        w.show()

    def change_room2(self):  # toon scherm kamer2
        global w
        w = Room2()
        w.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        w.move(0, 0)
        w.show()

    def change_room3(self):  # toon scherm kamer3
        global w
        w = Room3()
        w.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        w.move(0, 0)
        w.show()

    def change_camera(self):  # toon scherm kamer1
        global w
        w = Camera()
        w.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        w.move(0, 0)
        w.show()

    def close_application(self):  # sluit programma
        print("bye")
        c.execute("UPDATE devices SET value = 1 WHERE device = 'stop'")
        conn.commit()
        c.close()
        conn.close()
        sys.exit()



class Room1(QDialog):
    def __init__(self):
        super(Room1, self).__init__()

        # setup scherm
        self.ui = Ui_Room1()
        self.ui.setupUi(self)

        # timer om de functie te laten herhalen
        self.ui.rolluik_timer = QtCore.QTimer()
        self.ui.rolluik_timer.timeout.connect(self.rolluik_stand)
        self.ui.rolluik_timer.start(100)

        # conecties knoppen met functies
        self.ui.home.clicked.connect(change_main)
        self.ui.rood.clicked.connect(self.setColor)
        self.ui.blauw.clicked.connect(self.setColor)
        self.ui.groen.clicked.connect(self.setColor)
        self.ui.blauwsld.valueChanged[int].connect(self.dimBlue)
        self.ui.roodsld.valueChanged[int].connect(self.dimRed)
        self.ui.groensld.valueChanged[int].connect(self.dimGreen)
        self.ui.up.clicked.connect(self.rolluik_ts)
        self.ui.down.clicked.connect(self.rolluik_ts)

    def rolluik_stand(self):  # verandert de kelueren van de status blokken
        # lees de stand uit
        conn2 = mysql.connect(user='root', password='masta', database='gip')
        c2 = conn2.cursor()
        c2.execute("SELECT value FROM devices WHERE device = 'reeddown'")
        for row in c2.fetchall():
            reeddown = row[0]
        c2.execute("SELECT value FROM devices WHERE device = 'reedup'")
        for row in c2.fetchall():
            reedup = row[0]

        # verandert de kleur naar de stand van de rolluik
        if reeddown:
            self.ui.boven.setStyleSheet("QFrame { background-color: %s }" %
                                        green.name())
            self.ui.beneden.setStyleSheet("QFrame { background-color: %s }" %
                                          red.name())
            self.ui.mid.setStyleSheet("QFrame { background-color: %s }" %
                                      red.name())
        elif reedup:
            self.ui.beneden.setStyleSheet("QFrame { background-color: %s }" %
                                          green.name())
            self.ui.boven.setStyleSheet("QFrame { background-color: %s }" %
                                        red.name())
            self.ui.mid.setStyleSheet("QFrame { background-color: %s }" %
                                      red.name())
        else:
            self.ui.mid.setStyleSheet("QFrame { background-color: %s }" %
                                      green.name())
            self.ui.beneden.setStyleSheet("QFrame { background-color: %s }" %
                                          red.name())
            self.ui.boven.setStyleSheet("QFrame { background-color: %s }" %
                                        red.name())
        c2.close()
        conn2.close()

    def rolluik_ts(self):  # schrijf naar de database als een knop van de roluik op het scherm wordt gebruikt
        source = self.sender()
        if source.text() == '↑':
            c.execute("UPDATE devices SET value = 1 WHERE device = 'servoup'")
        else:
            c.execute("UPDATE devices SET value = 1 WHERE device = 'servodown'")
        conn.commit()

    def setColor(self):  # schrijft input van de RGB knoppen in de database

        source = self.sender()

        global Ron, Gon, Bon

        if source.text() == "Rood":
            if Ron:
                c.execute("UPDATE devices SET value = 0 WHERE device = 'led1ron'")
                Ron = False
            else:
                c.execute("UPDATE devices SET value = 1 WHERE device = 'led1ron'")
                Ron = True
        elif source.text() == "Groen":
            if Gon:
                c.execute("UPDATE devices SET value = 0 WHERE device = 'led1gon'")
                Gon = False
            else:
                c.execute("UPDATE devices SET value = 1 WHERE device = 'led1gon'")
                Gon = True
        else:
            if Bon:
                c.execute("UPDATE devices SET value = 0 WHERE device = 'led1bon'")
                Bon = False
            else:
                c.execute("UPDATE devices SET value = 1 WHERE device = 'led1bon'")
                Bon = True

        conn.commit()

        # geeft het statusblokje de juiste kleur
        if Bon or Ron or Gon:
            self.ui.status.setStyleSheet("QFrame { background-color: %s }" %
                                         green.name())
        else:
            self.ui.status.setStyleSheet("QFrame { background-color: %s }" %
                                         red.name())

    def dimBlue(self, value):  # schruift de input van de slider voor blauw in de database
        c.execute("UPDATE devices SET value = %s WHERE device = %s", (value, 'led1blue'))
        conn.commit()

    def dimRed(self, value):  # schruift de input van de slider voor rood in de database
        c.execute("UPDATE devices SET value = %s WHERE device = %s", (value, 'led1red'))
        conn.commit()

    def dimGreen(self, value):  # schruift de input van de slider voor groen in de database
        c.execute("UPDATE devices SET value = %s WHERE device = %s", (value, 'led1green'))
        conn.commit()


class Room2(QDialog):
    def __init__(self):
        super(Room2, self).__init__()

        # setup scherm
        self.ui = Ui_Room2()
        self.ui.setupUi(self)

        # timer om de functie te laten herhalen
        self.ui.stat = QtCore.QTimer()
        self.ui.stat.timeout.connect(self.room2stat)
        self.ui.stat.start(100)

        # conecties knoppen met functies
        self.ui.home.clicked.connect(change_main)
        self.ui.light.clicked.connect(self.room2)

    def room2(self):  # schrijf naar de database als de knop van de verlichting op het scherm wordt gebruikt
        conn2 = mysql.connect(user='root', password='masta', database='gip')
        c2 = conn2.cursor()
        global room2
        c2.execute("SELECT value FROM devices WHERE device = 'led2'")
        for row in c2.fetchall():
            led2 = row[0]

        if led2:
            room2 = False
        else:
            room2 = True

        if room2:
            c.execute("UPDATE devices SET value = 1 WHERE device = 'led2'")

        else:
            c.execute("UPDATE devices SET value = 0 WHERE device = 'led2'")

        conn.commit()

    def room2stat(self):  # verandert de kelueren van de status blok
        conn2 = mysql.connect(user='root', password='masta', database='gip')
        c2 = conn2.cursor()
        c2.execute("SELECT value FROM devices WHERE device = 'led2'")
        for row in c2.fetchall():
            led2 = row[0]

        c2.execute("SELECT value FROM devices WHERE device = 'led2bew'")
        for row in c2.fetchall():
            led2bew = row[0]

        if led2 or led2bew:
            self.ui.aanuit.setStyleSheet("QFrame { background-color: %s }" %
                                         green.name())
        else:
            self.ui.aanuit.setStyleSheet("QFrame { background-color: %s }" %
                                         red.name())
        c2.close()
        conn2.close()


class Camera(QDialog):
    def __init__(self):
        super(Camera, self).__init__()

        # setup scherm
        self.ui = Ui_Camera()
        self.ui.setupUi(self)

        # conecties knoppen met functies
        self.ui.home.clicked.connect(change_main)


class Room3(QDialog):
    def __init__(self):
        super(Room3, self).__init__()

        # setup scherm
        self.ui = Ui_Room3()
        self.ui.setupUi(self)
        self.temp()

        # timer om de functie te laten herhalen
        self.ui.stat = QtCore.QTimer()
        self.ui.stat.timeout.connect(self.room3stat)
        self.ui.stat.timeout.connect(self.verwarmingstat)
        self.ui.stat.start(100)

        # conecties knoppen met functies
        self.ui.home.clicked.connect(change_main)
        self.ui.verlivht.clicked.connect(self.room3)
        self.ui.verwarm.clicked.connect(self.verwarm_knop)
        self.ui.temp.setValue(verwarming)
        self.ui.temp.valueChanged[int].connect(self.verwarm)

    def room3(self):  # schrijf naar de database als de knop van de verlichting op het scherm wordt gebruikt
        conn2 = mysql.connect(user='root', password='masta', database='gip')
        c2 = conn2.cursor()
        global room3
        c2.execute("SELECT value FROM devices WHERE device = 'led3'")
        for row in c2.fetchall():
            led3 = row[0]

        if led3:
            room3 = False
        else:
            room3 = True

        if room3:
            c.execute("UPDATE devices SET value = 1 WHERE device = 'led3'")

        else:
            c.execute("UPDATE devices SET value = 0 WHERE device = 'led3'")

        conn.commit()
        c2.close()
        conn2.close()

    def room3stat(self):  # verandert de kelueren van de status blok voor de verlichting
        conn2 = mysql.connect(user='root', password='masta', database='gip')
        c2 = conn2.cursor()
        c2.execute("SELECT value FROM devices WHERE device = 'led3'")
        for row in c2.fetchall():
            led3 = row[0]

        if led3:
            self.ui.stat_verlicht.setStyleSheet("QFrame { background-color: %s }" %
                                                green.name())
        else:
            self.ui.stat_verlicht.setStyleSheet("QFrame { background-color: %s }" %
                                                red.name())
        c2.close()
        conn2.close()

    def verwarm(self, value):  # schrijf naar de database als de slider van de verwarming op het scherm wordt verandert
        global verwarming
        c.execute("UPDATE devices SET value = %s WHERE device = %s", (value, 'verwarmingset'))
        conn.commit()
        verwarming = value

    def verwarm_knop(self):   # schrijf naar de database als de knop van de verwarming op het scherm wordt gebruikt
        conn2 = mysql.connect(user='root', password='masta', database='gip')
        c2 = conn2.cursor()
        c2.execute("SELECT value FROM devices WHERE device = 'verwarming'")
        for row in c2.fetchall():
            heat = row[0]

        if heat:
            Von = False
        else:
            Von = True

        if Von:
            c.execute("UPDATE devices SET value = 1 WHERE device = 'verwarming'")
        else:
            c.execute("UPDATE devices SET value = 0 WHERE device = 'verwarming'")
        conn.commit()
        c2.close()
        conn2.close()

    def verwarmingstat(self):  # verandert de kelueren van de status blok voor de verwarming
        conn2 = mysql.connect(user='root', password='masta', database='gip')
        c2 = conn2.cursor()
        c2.execute("SELECT value FROM devices WHERE device = 'verwarming'")
        for row in c2.fetchall():
            heat = row[0]

        if heat:
            self.ui.stat_verwarm.setStyleSheet("QFrame { background-color: %s }" %
                                               green.name())
        else:
            self.ui.stat_verwarm.setStyleSheet("QFrame { background-color: %s }" %
                                               red.name())
        c2.close()
        conn2.close()

    def temp(self):  # lees de temperatuur voor het touchscreen
        conn2 = mysql.connect(user='root', password='masta', database='gip')
        c2 = conn2.cursor()
        global temp1

        c2.execute("SELECT temp FROM temp WHERE locatie = 'binnen'")
        for row in c2.fetchall():
            temp1 = row[0]

        self.ui.Tbinnen.display(temp1)

        global temp2

        c2.execute("SELECT temp FROM temp WHERE locatie = 'buiten'")
        for row in c2.fetchall():
            temp2 = row[0]
        self.ui.Tbuiten.display(temp2)
        c2.close()
        conn2.close()


class KeyPad(QDialog):
    def __init__(self):
        super(KeyPad, self).__init__()

        # setup scherm
        self.ui = Ui_KeyPad()
        self.ui.setupUi(self)

        # conecties knoppen met functies
        self.ui.een.clicked.connect(self.disable)
        self.ui.twee.clicked.connect(self.disable)
        self.ui.drie.clicked.connect(self.disable)
        self.ui.vier.clicked.connect(self.disable)
        self.ui.vijf.clicked.connect(self.disable)
        self.ui.zes.clicked.connect(self.disable)
        self.ui.zeven.clicked.connect(self.disable)
        self.ui.acht.clicked.connect(self.disable)
        self.ui.negen.clicked.connect(self.disable)
        self.ui.nul.clicked.connect(self.disable)
        self.ui.ster.clicked.connect(self.disable)
        self.ui.hek.clicked.connect(self.disable)

        c.execute("UPDATE devices SET value = 1 WHERE device = 'alarm'")
        conn.commit()

    def disable(self):  # functie voor het code om het alarm uit te schakelen
        source = self.sender()
        global digit, code

        self.ui.fout.setStyleSheet("QFrame { background-color: %s }" %
                                   black.name())

        if source.text() == '*':
            if code == ['6', '5', '4', '3', '2', '1']:
                global w
                c.execute("UPDATE devices SET value = 0 WHERE device = 'alarm'")
                conn.commit()
                w = Main()
                w.setWindowFlags(QtCore.Qt.FramelessWindowHint)
                w.move(0, 0)
                w.show()
                code.clear()
                digit = 0

            else:
                code.clear()
                self.ui.fout.setStyleSheet("QFrame { background-color: %s }" %
                                           red.name())

        else:
            code.insert(0, source.text())
            digit = digit + 1

        if source.text() == '#':
            code.clear()

        print(code)


def change_main():  # verandert het scherm naar het hoofdmenu
    global w
    w = Main()
    w.setWindowFlags(QtCore.Qt.FramelessWindowHint)
    w.move(0, 0)
    w.show()

app = QApplication(sys.argv)
w = Main()
sys.exit(app.exec_())
