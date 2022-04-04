from ast import While
import serial



def readSerial():
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    ser.reset_input_buffer()
    
    #light,soil
    ans=[]
    while True and len(ans)<2:
        
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').rstrip()
            line = line.split("\n")

            x,value=line
            if x=="S:":
                ans.append(value)
            if x=="L:"
                ans=[value]+ans
    print(ans)
            



if __name__ == '__main__':
    readSerial()

       