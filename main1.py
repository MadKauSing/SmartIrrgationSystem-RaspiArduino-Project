
from platform import release
import sys
sys.path.append('./modules/')

import readSerial;
import moist;
import ultrasonic_distance;
import dataDumpTest;
import dataDump;
import runMotor;
import time


data_offset=time.time()
RelayPinMotor=21
runMotor.setup(RelayPinMotor)
motorThresh=350
motorRun=5

init_time=time.time()


#main loop that runs in the background
while True:
    temp_time=time.time();
    if(temp_time-init_time>=5):
        init_time=temp_time
        
        light,soilmoisture=readSerial.readSerial()
        moistureSensor=moist.MoistureSensor(17)
        ultraSensor=ultrasonic_distance.UltrasonicSensor(18,14)
        
        
    
    # light,soilmoisture=readSerial.readSerial()

    # moistureSensor=moist.MoistureSensor(17)
    # ultraSensor=ultrasonic_distance.UltrasonicSensor(18,14)
    
    # humidity,temperature=moistureSensor.get()
    # height=ultraSensor.distance()
    
    # dataDump.writeValuesTest(temperature,soilmoisture,humidity,light,height)
    
    # if humidity<motorThresh:
    #     data_offset+=runMotor.loop(motorRun)
        
        
    
    
    # ##600 secs
    # time.sleep(600)
    # print("check")
    # ##anyone who is editing this code run and see if values are appending to csv file
    ##to reset csv run dataDumpInit.py
    
    
    