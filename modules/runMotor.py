import RPi.GPIO as GPIO
import time
 
RelayPin = 40 # Set pin11 as Out
 
def setup():
    GPIO.setmode(GPIO.BOARD) # Set GPIO as numbering
    GPIO.setup(RelayPin, GPIO.OUT)
    GPIO.output(RelayPin, GPIO.HIGH)
 
def loop():
    while True:
        print ('Relay Channel One is On')
        GPIO.output(RelayPin, GPIO.LOW)
        time.sleep(0.5)
        print ('Relay Channel One is Off')
        GPIO.output(RelayPin, GPIO.HIGH)
        time.sleep(0.5)
 
def destroy():
    GPIO.output(RelayPin, GPIO.HIGH)
    GPIO.cleanup()
 
if __name__ == '__main__': # Program start from here
    setup()
    try:
        loop()
    except KeyboardInterrupt: # When Control C is pressed program will destroy()
        destroy()