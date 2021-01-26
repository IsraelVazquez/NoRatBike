import serial
import time
import string
import pynmea2
from sms import sendsms

while True:
    try:
        port="/dev/ttyAMA0"
        ser=serial.Serial(port, baudrate=9600, timeout=0.5)
        dataout = pynmea2.NMEAStreamReader()
        newdata=ser.readline()
        if newdata[0:6] == "$GNGGA":
            newmsg=pynmea2.parse(newdata)
            lat=newmsg.latitude
            lng=newmsg.longitude
            gps = " Latitude= " + str(lat) + " and Longitude= " + str(lng)
            sendsms(gps)
            print(gps)
            time.sleep(5)
    except Exception:
        print ("No connection")
        time. sleep(2)
