// Sensor pins
#define sensorPower 7
#define sensorPin A0

void setup() {
  pinMode(sensorPower, OUTPUT);
  
  // Initially keep the sensor OFF
  digitalWrite(sensorPower, LOW);
  
  Serial.begin(9600);
}

void loop() {
  //get the reading from the function below and print it
  Serial.print("Analog output: ");
  Serial.println(readSensor());`
  
  delay(1000);
}

//  This function returns the analog soil moisture measurement
int readSensor() {
  digitalWrite(sensorPower, HIGH);  // Turn the sensor ON
  delay(10);              // Allow power to settle
  int val = analogRead(sensorPin);  // Read the analog value form sensor
  digitalWrite(sensorPower, LOW);   // Turn the sensor OFF
  return val;             // Return analog moisture value
}
