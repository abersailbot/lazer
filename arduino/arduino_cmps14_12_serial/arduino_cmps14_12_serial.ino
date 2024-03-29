/*****************************************
*   CMPS12 Serial example for Arduino    *
*        By James Henderson, 2014        * 
*****************************************/

#include <SoftwareSerial.h>

#define CMPS_GET_ANGLE8 0x12
#define CMPS_GET_ANGLE16 0x13
#define CMPS_GET_PITCH 0x14
#define CMPS_GET_ROLL 0x15

SoftwareSerial CMPS12 = SoftwareSerial(2,3);

unsigned char high_byte, low_byte, angle8;
char pitch, roll;
unsigned int angle16;

void printData() {
  Serial.print("roll: ");            // Display roll data
  Serial.print(roll, DEC);
  
  Serial.print("    pitch: ");          // Display pitch data
  Serial.print(pitch, DEC);
  
  Serial.print("    angle full: ");       // Display 16 bit angle with decimal place
  Serial.print(getFullAngle(), DEC);
  Serial.print(".");
  Serial.print(angle16 % 10, DEC);
  
  Serial.print("    angle 8: ");        // Display 8bit angle
  Serial.println(angle8, DEC);
}

float getFullAngle() {
  CMPS12.write(CMPS_GET_ANGLE16);
    // Request and read 16 bit angle
  while(CMPS12.available() < 2);
  high_byte = CMPS12.read();
  low_byte = CMPS12.read();
  angle16 = high_byte;                // Calculate 16 bit angle
  angle16 <<= 8;
  angle16 += low_byte;
  return angle16 / 10.0;
}

void setup()
{
  Serial.begin(9600);            // Start serial ports
  CMPS12.begin(9600);
  Serial.println(getFullAngle());
}

void loop()
{
  
}
