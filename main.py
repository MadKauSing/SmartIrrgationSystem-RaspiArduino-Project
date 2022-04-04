import sys
sys.path.append('./modules/')

import readSerial;
import moist;
import ultrasonic_distance;
import dataDump;

import time

#main loop that runs in the background
while True:
    light,soilmoisture=readSerial.readSerial();

    moistureSensor=moist.MoistureSensor(17);
    ultraSensor=ultrasonic_distance.UltrasonicSensor(18,14)
    
    humidity,temperature=moistureSensor.get()
    height=ultraSensor.distance()
    
    dataDump.writeValues(temperature,soilmoisture,humidity,light,height)
    time.sleep(1000);