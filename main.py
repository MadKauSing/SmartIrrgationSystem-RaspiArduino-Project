import sys
sys.path.append('./modules/')

import readSerial;
import moist;
import ultrasonic_distance;
import dataDump;

import time

#main loop that runs in the background
while True:
    light,soil=readSerial.readSerial();

    moistureSensor=moist.MoistureSensor(17);
    ultraSensor=ultrasonic_distance.UltrasonicSensor(18,14)
    
