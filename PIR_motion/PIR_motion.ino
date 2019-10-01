/*macro definitions of PIR motion sensor pin and LED pin*/
#include <Wire.h>
#include <Digital_Light_TSL2561.h>

#define PIR_MOTION_SENSOR 2//Use pin 2 to receive the signal from the module


void setup()
{
    Wire.begin();
    pinMode(PIR_MOTION_SENSOR, INPUT);
    Serial.begin(9600);
    TSL2561.init();
}

void loop()
{
    if(digitalRead(PIR_MOTION_SENSOR))//if it detects the moving people?
        Serial.println("Hi,people is coming");
    else
        Serial.println("Watching");

  Serial.print("The Light value is: ");
  Serial.println(TSL2561.readVisibleLux());
  
 delay(100);
}
