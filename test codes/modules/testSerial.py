
import serial

def readSerial():
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    ser.reset_input_buffer()
    if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').rstrip()
            print(line)


if __name__ == '__main__':
    readSerial()

