from ast import While
import serial



def readSerial():
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    ser.reset_input_buffer()
    
    #light,soil
    ans=[]
    flag=0
    while True and len(ans)<2:
        
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').rstrip()
            line = line.split()

            
            #k so the serial gives output as one line only that is one line per sensor
            #the flags act like a simple mutex so no conflict of data
            #light is always first value
            #soil is second
            x,value=line
            if x=="S:" and flag==0:
                ans.append(value)
                flag=1
            if x=="L:" and flag==1:
                ans=[value]+ans
                flag=0
    light,soil=ans
    return light,soil
            
if __name__ == '__main__':
    print("\tlight","\tsoil")
    while True:
        light,soil=readSerial()
        print("\t",light,"\t",soil)
    
       