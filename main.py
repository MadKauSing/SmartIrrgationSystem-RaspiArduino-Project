import sys
sys.path.append('./modules/')

import readSerial;
import moist;
import ultrasonic_distance;
import dataDumpTest;

import time

#main loop that runs in the background
while True:
    light,soilmoisture=readSerial.readSerial();

    moistureSensor=moist.MoistureSensor(17);
    ultraSensor=ultrasonic_distance.UltrasonicSensor(18,14)
    
    humidity,temperature=moistureSensor.get()
    height=ultraSensor.distance()
    
    dataDumpTest.writeValuesTest(temperature,soilmoisture,humidity,light,height)
    ##600 secs
    time.sleep(600);
    print("check")
    ##anyone who is editing this code run and see if values are appending to csv file
    ##to reset csv run dataDumpInit.py
    
    
    