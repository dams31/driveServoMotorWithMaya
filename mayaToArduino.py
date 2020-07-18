import logging
import threading
import time

tracked = "_L_000_jnt_CTRL"
ARDUINO_SERIAL_ADRESS = '/dev/tty.usbmodem141201'

def send_to_arduino(interval):
    from maya import cmds
    import maya.utils as utils
    import serial
    
    global ARDUINO_SERIAL_ADRESS
    ser = serial.Serial(ARDUINO_SERIAL_ADRESS, 9600, timeout=1)
        
    def read_and_send():

        global tracked

        angle = cmds.getAttr(tracked + ".ry")    
        if (0 <= angle <= 180):
            ser.write(str(round(angle,3)))
        else:
            print "Servo angle must be an integer between 0 and 180.\n"

    while True:
        time.sleep(interval)
        utils.executeDeferred(read_and_send)
        # always use executeDeferred or evalDeferredInMainThreadWithResult\
        # if you're running a thread in Maya!
        # Read the serial value
        global stop_threads

        if stop_threads:
            break

# launch thread, will open a thread who read the rotationY of object tracked
stop_threads = False
t = threading.Thread(None, target=send_to_arduino, args=(1.05,))
t.start()
print('thread open')

# kill thread
time.sleep(1) 
stop_threads = True
t.join()
print('thread killed')
