from ast import While
import serial



def readSerial():
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    ser.reset_input_buffer()
    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').rstrip()
            line = line.split("\n")
            
            ans=[]
            for i in line:
                x,value=i.split()
                ans.append(value)
            print(ans)
            print(line)
            



if __name__ == '__main__':
    readSerial()

       