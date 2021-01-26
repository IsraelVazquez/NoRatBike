import time
import serial
from serial import Serial

def sendsms(message):
    #recipient = "+525530269862"
    #recipient = "+525516347102"
    #bbva cel
    recipient="+525516347102"
    #message = "Se  ha detectado movimiento"
    #tris tty is fot raspberry pi 4 model B
    phone = serial.Serial("/dev/ttyACM2",9600, timeout=5)
    #this tty is for raspberry pi zero
    #phone = serial.Serial("/dev/ttyAMA0",9600, timeout=5)
    try:
        time.sleep(0.5)
        phone.write(b'AT\r')
        time.sleep(0.5)
        phone.write(b'AT+CMGF=1\r')
        time.sleep(0.5)
        phone.write(b'AT+CMGS="' + recipient.encode() + b'"\r')
        time.sleep(0.5)
        phone.write(message.encode() + b"\r")
        print (phone.read(256))
        time.sleep(2)
        time.sleep(0.5)
        phone.write(bytes([26]))
        time.sleep(0.5)
        print ("sent")
    finally:
        phone.close
    
    return message