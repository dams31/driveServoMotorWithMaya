import logging
import threading
import time

stop_threads = False

import serial

ARDUINO_SERIAL_ADRESS = '/dev/tty.usbserial-14120'
ser = serial.Serial(ARDUINO_SERIAL_ADRESS, 9600, timeout=1)

def read_and_send():
    global driven
    angle = 135#cmds.getAttr(driven + ".ry")    
    if (0 <= angle <= 180):
        print "angle value :: ", angle, "\n"

        ser.write(str(angle))
        ser.flushInput()
        serialValue = ser.readline().strip()
        print "Serial value :: ", serialValue, "\n"
        
    else:
        print "Servo angle must be an integer between 0 and 180.\n"

while True:
    time.sleep(1)
    #utils.executeDeferred(read_and_send)
    # always use executeDeferred or evalDeferredInMainThreadWithResult if you're running a thread in Maya!
    # Read the serial value
    read_and_send()
