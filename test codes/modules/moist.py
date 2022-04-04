import Adafruit_DHT

# Set sensor type : Options are DHT11,DHT22 or AM2302
# Set GPIO sensor is connected to

class MoistureSensor():
    def __init__(self,GPIO_PIN):
        self.GPIO_PIN=GPIO_PIN;
        self.sensor=Adafruit_DHT.DHT11
    def get(self):
        humidity,temperature=Adafruit_DHT.read_entry(self.sensor,self.GPIO_PIN);
        return humidity,temperature;


# Reading the DHT11 is very sensitive to timings and occasionally
# the Pi might fail to get a valid reading. So check if readings are valid.



if __name__="__main__":
    sensor=MoistureSensor(17)
    while True:
    
        humidity, temperature = sensor.get();
        if humidity is not None and temperature is not None:
            print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
        else:
            print('Failed to get reading. Try again!')
