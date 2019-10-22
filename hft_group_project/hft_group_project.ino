#include "DHT.h"
#define DHTPIN 2
#define DHTTYPE DHT11
#include <Digital_Light_TSL2561.h>
DHT dht(DHTPIN, DHTTYPE); //Initialize DHT sensor
#include <Wire.h>
#include <LiquidCrystal_I2C.h>
#include <SPI.h>
#include <SD.h>

#include "RTClib.h"
RTC_DS1307 rtc;

#define I2C_ADDR 0x3F
#define BACKLIGHT_PIN 3
#define En_pin 2
#define Rw_pin 1
#define Rs_pin 0
#define D4_pin 4
#define D5_pin 5
#define D6_pin 6
#define D7_pin 7

LiquidCrystal_I2C lcd(0x3F, En_pin, Rw_pin, Rs_pin, D4_pin, D5_pin, D6_pin, 7, BACKLIGHT_PIN, POSITIVE);
File myFile;

// Soil sensor
int sensorPin = A0;
int soil;
int limit = 300;

// Light sensor
float light;

//Temp and humidity sensor
float humidity;
float temperature;

// Date
String day;
String month;
String year;
String hours;
String minutes;
String seconds;

void setup() {
  Serial.begin(9600);
  
  while (!Serial) {
    ; // wait for serial port to connect. Needed for native USB port only
  }

  Serial.print("Initializing SD card...");

  if (!SD.begin(10)) {
    Serial.println("initialization failed!");
    while (1);
  }
  Serial.println("initialization done.");


  myFile = SD.open("logging.csv", FILE_WRITE);
  if (myFile) {

    myFile.print("date"); //col 0
    myFile.print(",");
    myFile.print("temperature"); //col 1
    myFile.print(",");
    myFile.print("humidity"); //col 2
    myFile.print(",");
    myFile.print("light"); //col 3
    myFile.print(",");
    myFile.print("soil"); //col 4
    myFile.println("");

    myFile.close();
  } else {
    Serial.println("error opening logging.csv");
  }

  pinMode(13, OUTPUT);
  Wire.begin();
  
  rtc.begin();
//  rtc.adjust(DateTime(__DATE__, __TIME__));
  TSL2561.init();

  dht.begin();
  lcd.begin(16, 3);
  lcd.backlight();
  delay(1000);
}

void loop() {
  delay(500);

  DateTime now = rtc.now();

  day = now.day();
  month = now.month();
  year = now.year();
  hours = now.hour();
  minutes = now.minute();
  seconds = now.second();

  humidity = readHumidity();
  temperature = readTemp();
  light = readLight();
  soil = readSoil();

  if (soil < limit) {
    digitalWrite(13, HIGH);
  }
  else {
    digitalWrite(13, LOW);
  }

  lcd.scrollDisplayRight();
  lcd.setCursor(0, 0);
  lcd.print(String("") + "T:    " + temperature + "C" + "   " + "H: " + humidity + "%");
  lcd.setCursor(0, 1);
  lcd.print(String("") + "Light: " + light  + "   " + "Soil: " + soil);


  myFile = SD.open("logging.csv", FILE_WRITE);

  // if the file opened okay, write to it:
  if (myFile) {


    myFile.print(year + '/' + month + '/' + day + ' ' + hours + ':' +  minutes + ':' + seconds); //col 0
    myFile.print(",");
    myFile.print(temperature); //col 1
    myFile.print(",");
    myFile.print(humidity); //col 2
    myFile.print(",");
    myFile.print(light); //col 3
    myFile.print(",");
    myFile.print(soil); //col 4
    myFile.println(""); // end of line

    // close the file:
    myFile.close();
    Serial.println("done.");
  } else {
    // if the file didn't open, print an error:
    Serial.println("error opening logging.csv");
  }

  //  lcd.print(String("") + "H:" + humidity + "%");
  //  lcd.setCursor(0, 1);
  //  lcd.print(String("") + "T:" + temperature + (char)223 + "C");
  //  lcd.setCursor(0, 2);
  //  lcd.print(String("") + "Light: " + light);
  //  lcd.setCursor(0, 3);
  //  lcd.print(String("") + "Soil: " + soilVal);

  Serial.print("Humidity: ");
  Serial.print(humidity);
  Serial.print(" %\t");
  Serial.print("Temperature: ");
  Serial.print(temperature);
  Serial.print(" *C ");
  Serial.print("The Light value is: ");
  Serial.println(light);
  Serial.print("Soil Value : ");
  Serial.println(soil);
}

float readHumidity() {

  float res = dht.readHumidity();

  if (isnan(res)) {
    return 0.0;
  } else {
    return res;
  }
}

float readTemp() {
  if (isnan(temperature)) {
    return 0.0;
  } else {
    return dht.readTemperature();
  }
}

float readLight() {
  float res = TSL2561.readVisibleLux();
  if (isnan(res)) {
    return 0.0;
  } else {
    return res;
  }
}

float readSoil() {
  if (isnan(soil)) {
    return 0.0;
  } else {
    return analogRead(sensorPin);
  }
}
