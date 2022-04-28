from platform import release
import sys
sys.path.append('./modules/')

import readSerial;
import moist;
import ultrasonic_distance;
import dataDumpTest;
import dataDump;
#import runMotor;

import time

def func():
	start_time=time.time()
	data_offset=time.time()
	#RelayPinMotor=21
	#runMotor.setup(RelayPinMotor)
	#motorThresh=250
	#motorRun=3

	#main loop that runs in the background
	while True:
	    
		light,soilmoisture=readSerial.readSerial()

		moistureSensor=moist.MoistureSensor(17)
		ultraSensor=ultrasonic_distance.UltrasonicSensor(18,14)
	    
		humidity,temperature=moistureSensor.get()
		height=ultraSensor.distance()
	    
		dataDump.writeValues(int(temperature),int(soilmoisture),int(humidity),int(light),int(height))
	   # if int(soilmoisture)<motorThresh:
	        #data_offset+=runMotor.loop(motorRun)
	       # runMotor.setup(RelayPinMotor)
	        
	    #print(start_time-data_offset)
	    
	    
	    ##600 secs
		time.sleep(5)
	    #print("check")
	    ##anyone who is editing this code run and see if values are appending to csv file
	    ##to reset csv run dataDumpInit.py
try:
	func()
except:
	print("Error")
	func()
    
    
