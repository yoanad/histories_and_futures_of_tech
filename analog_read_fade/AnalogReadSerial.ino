/*
  AnalogReadSerial

  Reads an analog input on pin 0, prints the result to the Serial Monitor.
  Graphical representation is available using Serial Plotter (Tools > Serial Plotter menu).
  Attach the center pin of a potentiometer to pin A0, and the outside pins to +5V and ground.

  This example code is in the public domain.

  http://www.arduino.cc/en/Tutorial/AnalogReadSerial
*/

int brightness = 0;    // how bright the LED is
int fadeAmount = 1;    // how many points to fade the LED by
int led = 9;           // the PWM pin the LED is attached to

// the setup routine runs once when you press reset:
void setup() {
  // initialize serial communication at 9600 bits per second:
  Serial.begin(9600);
  pinMode(led, OUTPUT);
}

// the loop routine runs over and over again forever:
void loop() {
  // read the input on analog pin 0:
  double sensorValue = analogRead(A0);
  sensorValue = map(sensorValue, 0, 1023, 0, 255);

  if (sensorValue < 1023/2) {
    brightness =  sensorValue;
  } else {
    brightness =   sensorValue;
  }

  analogWrite(led, brightness);
  
  Serial.println(255 / sensorValue);
  delay(1);        // delay in between reads for stability
}
