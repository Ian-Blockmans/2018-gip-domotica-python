import mysql.connector as mysql
import time
import datetime


temp1 = 0
temp2 = 0
sensorid1 = "28-000009acebe1"
sensorid2 = "28-0000097bf4f6"
date = 'i'
unix = int(time.time())
date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))

conn = mysql.connect(user='root', password='masta', database='gip')
c = conn.cursor()


def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS devices(tijd TEXT, device TEXT, value INT)")
    c.execute("CREATE TABLE IF NOT EXISTS temp(locatie TEXT, tijd TEXT, temp INT)")
    c.execute("INSERT INTO devices (tijd, device, value) VALUES (%s, %s, %s)",
              (date, 'led1', 1))
    c.execute("INSERT INTO devices (tijd, device, value) VALUES (%s, %s, %s)",
              (date, 'led1ron', 0))
    c.execute("INSERT INTO devices (tijd, device, value) VALUES (%s, %s, %s)",
              (date, 'led1gon', 0))
    c.execute("INSERT INTO devices (tijd, device, value) VALUES (%s, %s, %s)",
              (date, 'led1bon', 0))
    c.execute("INSERT INTO devices (tijd, device, value) VALUES (%s, %s, %s)",
              (date, 'led2', 0))
    c.execute("INSERT INTO devices (tijd, device, value) VALUES (%s, %s, %s)",
              (date, 'led3', 0))
    c.execute("INSERT INTO devices (tijd, device, value) VALUES (%s, %s, %s)",
              (date, 'reedup', 0))
    c.execute("INSERT INTO devices (tijd, device, value) VALUES (%s, %s, %s)",
              (date, 'reeddown', 0))
    c.execute("INSERT INTO devices (tijd, device, value) VALUES (%s, %s, %s)",
              (date, 'servo', 0))
    c.execute("INSERT INTO devices (tijd, device, value) VALUES (%s, %s, %s)",
              (date, 'servoup', 0))
    c.execute("INSERT INTO devices (tijd, device, value) VALUES (%s, %s, %s)",
              (date, 'servodown', 0))
    c.execute("INSERT INTO devices (tijd, device, value) VALUES (%s, %s, %s)",
              (date, 'verwarming', 0))
    c.execute("INSERT INTO devices (tijd, device, value) VALUES (%s, %s, %s)",
              (date, 'verwarmingset', 20))
    c.execute("INSERT INTO devices (tijd, device, value) VALUES (%s, %s, %s)",
              (date, 'led1red', 75))
    c.execute("INSERT INTO devices (tijd, device, value) VALUES (%s, %s, %s)",
              (date, 'led1green', 75))
    c.execute("INSERT INTO devices (tijd, device, value) VALUES (%s, %s, %s)",
              (date, 'led1blue', 75))
    c.execute("INSERT INTO devices (tijd, device, value) VALUES (%s, %s, %s)",
              (date, 'alarm', 0))
    c.execute("INSERT INTO devices (tijd, device, value) VALUES (%s, %s, %s)",
              (date, 'stop', 0))
    c.execute("INSERT INTO devices (tijd, device, value) VALUES (%s, %s, %s)",
              (date, 'led2bew', 0))

    conn.commit()
    c.close()
    conn.close()

#def data_entry():
#    global temp1, date, temp2
#    tfile = open("/sys/bus/w1/devices/" + sensorid1 + "/w1_slave")
#    text = tfile.read()
#    tfile.close()
#    secondline = text.split("\n")[1]
#    temperaturedata = secondline.split(" ")[9]
#    temperature = float(temperaturedata[2:])
#    temp1 = temperature / 1000
#    locatie = 'binnen'
#
#
#    c.execute("INSERT INTO temp (locatie, tijd, temp) VALUES (%s, %s, %s)",
#              (locatie, date, int(temp1)))
#    conn.commit()


create_table()
#data_entry()
