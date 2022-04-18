//Sensor pins
#define sensorPowerSoil 7
#define sensorPowerLight 3
#define sensorPinSoil A0
#define sensorPinLight A3
int sensorValueLight=0;

void setup() {
  
  pinMode(sensorPowerSoil, OUTPUT);
  digitalWrite(sensorPowerSoil, LOW);

  pinMode(sensorPowerLight, OUTPUT);
  digitalWrite(sensorPowerLight, LOW);
  
  Serial.begin(9600);
}

void loop() {
  //get the reading from the function below and print it

  //sensorValueLight=analogRead(sensorPinLight);
  Serial.print("S: ");
  Serial.println(readSensor());
  Serial.print("L: ");
  Serial.println(readSensorLight());
  
  //Serial.print("L:"); 
  //Serial.println(sensorValueLight);

  
  delay(2000);
}

int readSensorLight(){
  digitalWrite(sensorPowerLight, HIGH);  // Turn the sensor ON
  delay(10);              // Allow power to settle
  int val = analogRead(sensorPinLight);  // Read the analog value form sensor
  digitalWrite(sensorPowerLight, LOW);   // Turn the sensor OFF
  return val;     
}


//  This function returns the analog soil moisture measurement
int readSensor() {
  digitalWrite(sensorPowerSoil, HIGH);  // Turn the sensor ON
  delay(10);              // Allow power to settle
  int val = analogRead(sensorPinSoil);  // Read the analog value form sensor
  digitalWrite(sensorPowerSoil, LOW);   // Turn the sensor OFF
  return val;             // Return analog moisture value
}
