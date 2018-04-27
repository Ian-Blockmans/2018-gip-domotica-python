import mysql.connector as mysql
import time
import datetime
import RPi.GPIO as GPIO
import paho.mqtt.client as mqtt

# pinnen
RGBred = 15
RGBgreen = 18
RGBblue = 14
ledkamer2 = 23
ledkamer3 = 24
bewegingssensor = 16
reed_deur = 12
reed_boven = 8
reed_beneden = 7
servo = 20
verwarmingpin = 21
rolluik_naar_boven = 27
rolluik_naar_beneden = 17

# temperatuur sensor id
sensorid1 = "28-000009acebe1"
sensorid2 = "28-0000097bf4f6"

# globale variabelen voor gebruik tussen functies
temp1 = 0
temp2 = 0
servo_beneden = 8.5
servo_boven = 6.5
richting = 'geen'
last2 = 'led'
last3 = 'led'
lastV = 'von'

# setup voor GPIO pinnen
GPIO.setmode(GPIO.BCM)
GPIO.setup(RGBred, GPIO.OUT)
GPIO.setup(RGBgreen, GPIO.OUT)
GPIO.setup(RGBblue, GPIO.OUT)
GPIO.setup(ledkamer2, GPIO.OUT)
GPIO.setup(ledkamer3, GPIO.OUT)
GPIO.setup(servo, GPIO.OUT)
GPIO.setup(verwarmingpin, GPIO.OUT)
GPIO.setup(bewegingssensor, GPIO.IN)
GPIO.setup(reed_boven, GPIO.IN)
GPIO.setup(reed_beneden, GPIO.IN)
GPIO.setup(rolluik_naar_boven, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(rolluik_naar_beneden, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(reed_boven, GPIO.IN)
GPIO.setup(reed_beneden, GPIO.IN)
pb = GPIO.PWM(RGBblue, 100)
pb.start(0)
pr = GPIO.PWM(RGBred, 100)
pr.start(0)
pg = GPIO.PWM(RGBgreen, 100)
pg.start(0)
heat = GPIO.PWM(verwarmingpin, 50)
heat.start(0)
pservo = GPIO.PWM(servo, 50)
pservo.start(0)

# connectie maken met de database
conn = mysql.connect(user='root', password='masta', database='gip')
c = conn.cursor()

# connectie maken met de MQTT broker
mqttclient = mqtt.Client(client_id="ian159159", clean_session=True, transport="tcp")
mqttclient.connect('localhost', port=1883)

# veriabele voor de tijd
unix = int(time.time())
date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))


def temp():  # leest de temperatuur en schrijft het naar de database, verzend temperatuur naar de MQTT broker
    global temp1, temp2
    """tfile = open("/sys/bus/w1/devices/" + sensorid1 + "/w1_slave")
    text = tfile.read()
    tfile.close()
    secondline = text.split("\n")[1]
    temperaturedata = secondline.split(" ")[9]
    temperature = float(temperaturedata[2:])
    temp1 = temperature / 1000
    locatie = 'binnen'
    c.execute("INSERT INTO temp (locatie, tijd, temp) VALUES (%s, %s, %s)",
              (locatie, date, int(temp1)))
    mqttclient.publish("home/indoor/temp", temp1)"""

    tfile2 = open("/sys/bus/w1/devices/" + sensorid2 + "/w1_slave")
    text2 = tfile2.read()
    tfile2.close()
    secondline2 = text2.split("\n")[1]
    temperaturedata2 = secondline2.split(" ")[9]
    temperature2 = float(temperaturedata2[2:])
    temp2 = temperature2 / 1000
    locatie = 'buiten'
    c.execute("INSERT INTO temp (locatie, tijd, temp) VALUES (%s, %s, %s)",
              (locatie, date, int(temp2)))
    conn.commit()
    mqttclient.publish("home/outdoor/temp", temp2)


def on_message_verwarming(client, userdata, message): # deze functie word uitgevoert als de verwarming op de website word bediend
    mqttconn = mysql.connect(user='root', password='masta', database='gip')
    mqttc = mqttconn.cursor()

    if str(message.payload) == "b'ON'":
        mqttc.execute("UPDATE devices SET value = 1 WHERE device = 'verwarming'")
    else:
        mqttc.execute("UPDATE devices SET value = 0 WHERE device = 'verwarming'")
    mqttconn.commit()
    mqttc.close()
    mqttconn.close()


def verwarming():  # zet verwarming aan of uit naargelang de temperatuur
    global lastV
    c.execute("SELECT value FROM devices WHERE device = 'verwarming'")
    for row in c.fetchall():
        von = row[0]

    c.execute("SELECT value FROM devices WHERE device = 'verwarmingset'")
    for row in c.fetchall():
        asked = row[0]

    mqttclient.publish("home/goal/temp", asked)

    if von:
        if temp1 > (asked + 1):
            heat.ChangeDutyCycle(0)
        elif temp1 < (asked - 1):
            heat.ChangeDutyCycle(90)

        if lastV != 'verwarmon':
            mqttclient.publish("home/verwarming/on/of", "ON")
        lastV = 'verwarmon'
    else:
        heat.ChangeDutyCycle(0)
        if lastV != 'verwarmof':
            mqttclient.publish("home/verwarming/on/of", "OFF")
        lastV = 'verwarmof'


def verlivhtingRGB():  # zet de RGB verlichting aan naargelang de database
    c.execute("SELECT value FROM devices WHERE device = 'led1'")
    for row in c.fetchall():
        led1 = row[0]
    c.execute("SELECT value FROM devices WHERE device = 'led1red'")
    for row in c.fetchall():
        dimRed = row[0]
    c.execute("SELECT value FROM devices WHERE device = 'led1green'")
    for row in c.fetchall():
        dimGreen = row[0]
    c.execute("SELECT value FROM devices WHERE device = 'led1blue'")
    for row in c.fetchall():
        dimBlue = row[0]
    c.execute("SELECT value FROM devices WHERE device = 'led1ron'")
    for row in c.fetchall():
        ron = row[0]
    c.execute("SELECT value FROM devices WHERE device = 'led1gon'")
    for row in c.fetchall():
        gon = row[0]
    c.execute("SELECT value FROM devices WHERE device = 'led1bon'")
    for row in c.fetchall():
        bon = row[0]

    if led1:
        if ron:
            pr.ChangeDutyCycle(dimRed)
        else:
            pr.ChangeDutyCycle(0)
        if gon:
            pg.ChangeDutyCycle(dimGreen)
        else:
            pg.ChangeDutyCycle(0)
        if bon:
            pb.ChangeDutyCycle(dimBlue)
        else:
            pb.ChangeDutyCycle(0)
    else:
        pr.ChangeDutyCycle(0)
        pg.ChangeDutyCycle(0)
        pb.ChangeDutyCycle(0)


def verlichting():  # zet de normale verlichting aan/uit naargelang de database
    global last2, last3
    c.execute("SELECT value FROM devices WHERE device = 'led2'")
    for row in c.fetchall():
        led2 = row[0]

    c.execute("SELECT value FROM devices WHERE device = 'led2bew'")
    for row in c.fetchall():
        led2bew = row[0]

    c.execute("SELECT value FROM devices WHERE device = 'led3'")
    for row in c.fetchall():
        led3 = row[0]

    if led2 or led2bew:
        GPIO.output(ledkamer2, True)
        if last2 != 'led2on' and led2bew != 1:
            mqttclient.publish("home/kitchen/light", "ON")
        last2 = 'led2on'
    else:
        GPIO.output(ledkamer2, False)
        if last2 != 'led2off':
            mqttclient.publish("home/kitchen/light", "OFF")
        last2 = 'led2off'

    if led3:
        GPIO.output(ledkamer3, True)
        if last3 != 'led3on':
            mqttclient.publish("home/bedroom/light", "ON")
        last3 = 'led3on'
    else:
        GPIO.output(ledkamer3, False)
        if last3 != 'led3off':
            mqttclient.publish("home/bedroom/light", "OFF")
        last3 = 'led3off'


def bew():  # funcrie voor de bewegingssensor
    c.execute("SELECT value FROM devices WHERE device = 'led2'")
    for row in c.fetchall():
        led2 = row[0]

    if led2:
        pass
    else:
        if GPIO.input(bewegingssensor):
            c.execute("UPDATE devices SET value = 1 WHERE device = 'led2bew'")
            GPIO.output(led2, True)
        else:
            c.execute("UPDATE devices SET value = 0 WHERE device = 'led2bew'")
            GPIO.output(led2, False)


def on_message_living_light(client, userdata, message): # word doorlopen als de website de verlichting aan zet
    mqttconn = mysql.connect(user='root', password='masta', database='gip')
    mqttc = mqttconn.cursor()

    if str(message.payload) == "b'ON'":
        mqttc.execute("UPDATE devices SET value = 1 WHERE device = 'led1'")
    else:
        mqttc.execute("UPDATE devices SET value = 0 WHERE device = 'led1'")
    mqttconn.commit()
    mqttc.close()
    mqttconn.close()


def on_message_kitchen_light(client, userdata, message): # word doorlopen als de website de verlichting aan zet
    mqttconn = mysql.connect(user='root', password='masta', database='gip')
    mqttc = mqttconn.cursor()

    if str(message.payload) == "b'ON'":
        mqttc.execute("UPDATE devices SET value = 1 WHERE device = 'led2'")
    else:
        mqttc.execute("UPDATE devices SET value = 0 WHERE device = 'led2'")
    mqttconn.commit()
    mqttc.close()
    mqttconn.close()


def on_message_bedroom_light(client, userdata, message): # word doorlopen als de website de verlichting aan zet
    mqttconn = mysql.connect(user='root', password='masta', database='gip')
    mqttc = mqttconn.cursor()

    if str(message.payload) == "b'ON'":
        mqttc.execute("UPDATE devices SET value = 1 WHERE device = 'led3'")
    else:
        mqttc.execute("UPDATE devices SET value = 0 WHERE device = 'led3'")
    mqttconn.commit()
    mqttc.close()
    mqttconn.close()


def rolluikup(rolluik_naar_boven):  # schrijf hardwareknop voor de rolluik input in de database
    c.execute("UPDATE devices SET value = 1 WHERE device = 'servoup'")
    conn.commit()


def rolluikdown(rolluik_naar_beneden):  # schrijf hardwareknop voor de rolluik input in de database
    c.execute("UPDATE devices SET value = 1 WHERE device = 'servodown'")
    conn.commit()


def on_message_shutter(client, userdata, message): # word doorlopen als de knoppen op de site van de rolluik worden bediend 
    mqttconn = mysql.connect(user='root', password='masta', database='gip')
    mqttc = mqttconn.cursor()

    if message.payload == "b'UP'":
        mqttc.execute("UPDATE devices SET value = 1 WHERE device = 'servoup'")
    elif message.payload == "b'DOWN'":
        mqttc.execute("UPDATE devices SET value = 1 WHERE device = 'servodown'")
    else:
        mqttc.execute("UPDATE devices SET value = 1 WHERE device = 'servostop'")
    mqttconn.commit()
    mqttc.close()
    mqttconn.close()


def rolluik():  # sturing van de rolluik
    global richting
    down = 0
    up = 0
    stop = 0
    c.execute("SELECT value FROM devices WHERE device = 'servodown'")
    for row in c.fetchall():
        down = row[0]

    c.execute("SELECT value FROM devices WHERE device = 'servoup'")
    for row in c.fetchall():
        up = row[0]

    c.execute("SELECT value FROM devices WHERE device = 'servostop'")
    for row in c.fetchall():
        stop = row[0]

    if GPIO.input(reed_beneden) and up:
        pservo.ChangeDutyCycle(servo_boven)
        richting = 'boven'

    elif GPIO.input(reed_boven) and down:
        pservo.ChangeDutyCycle(servo_beneden)
        richting = 'beneden'

    elif richting == 'beneden' and GPIO.input(reed_beneden):
        pservo.ChangeDutyCycle(0)
        richting = 'geen'

    elif richting == 'boven' and GPIO.input(reed_boven):
        pservo.ChangeDutyCycle(0)
        richting = 'geen'

    elif (not GPIO.input(reed_beneden)) and (not GPIO.input(reed_boven)):

        if (richting == 'boven' or richting == 'beneden') and (up or down or stop):
            pservo.ChangeDutyCycle(0)
            richting = 'geen'

        elif richting == 'geen' and up:
            pservo.ChangeDutyCycle(servo_boven)
            richting = 'boven'

        elif richting == 'geen' and down:
            pservo.ChangeDutyCycle(servo_beneden)
            richting = 'beneden'

    elif GPIO.input(reed_beneden) and GPIO.input(reed_boven):
        pservo.ChangeDutyCycle(0)
        richting = 'geen'

    if down:
        c.execute("UPDATE devices SET value = 0 WHERE device = 'servodown'")

    if up:
        c.execute("UPDATE devices SET value = 0 WHERE device = 'servoup'")

    if stop:
        c.execute("UPDATE devices SET value = 1 WHERE device = 'servostop'")
    conn.commit()


def handler(i):  # functie voor als het alarm getrigert wordt
    time.sleep(20)
    c.execute("SELECT value FROM devices WHERE device = 'alarm'")
    for row in c.fetchall():
        alarm = row[0]

    while 1:
        if alarm:
            break
        else:
            break


def alarm_enable():  # set interupt voor alarm
    GPIO.add_event_detect(bewegingssensor, GPIO.RISING, callback=handler, bouncetime=10)


def alarm_disable():  # verwijder interupt voor alarm
    GPIO.remove_event_detect(bewegingssensor)

# interupts voor hardware knoppen
GPIO.add_event_detect(rolluik_naar_beneden, GPIO.RISING, callback=rolluikup, bouncetime=500)
GPIO.add_event_detect(rolluik_naar_boven, GPIO.RISING, callback=rolluikdown, bouncetime=500)

# subscripties voor MQTT
mqttclient.message_callback_add("home/living/light", on_message_living_light)
mqttclient.message_callback_add("home/kitchen/light", on_message_kitchen_light)
mqttclient.message_callback_add("home/bedroom/light", on_message_bedroom_light)
mqttclient.message_callback_add("home/verwarming/on/of", on_message_verwarming)
mqttclient.message_callback_add("home/living/shutter", on_message_shutter)
on_message = mqttclient.on_message
mqttclient.subscribe("home/#")

mqttclient.loop_start()

while 1:  # alle functies worden doorlopen met bepaalde timing

    temp()
    verwarming()

    for i in range(0, 11):  # elke 5 seconde worden deze functies doorlopen
        c.execute("SELECT value FROM devices WHERE device = 'stop'")
        for row in c.fetchall():
            stop = row[0]

        c.execute("SELECT value FROM devices WHERE device = 'alarm'")
        for row in c.fetchall():
            alarm = row[0]

        if alarm:
            time.sleep(20)
            alarm_enable()
        else:
            alarm_disable()

        if stop:
            c.execute("UPDATE devices SET value = 0 WHERE device = 'stop'")
            conn.commit()
            mqttclient.loop_stop()
            c.close()
            conn.close()
            GPIO.cleanup()
            quit()

        for j in range(0, 499):  # elke 0.1 seconde word deze functies doorlopen
            verlivhtingRGB()
            verlichting()
            bew()
            rolluik()
            time.sleep(0.01)
nyaa.is
