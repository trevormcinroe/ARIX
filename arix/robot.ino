/*
 * -----------------------------------------------------------------------------------------------*/

#ifndef ARDUINO_AVR_MEGA2560
#error Wrong board. Please choose "Arduino/Genuino Mega or Mega 2560"
#endif

// Include FNHR (Freenove Hexapod Robot) library
#include <FNHR.h>
FNHR robot;
String data;
int movement_loops = 5;

void setup() {
  // Set action speed
  // Call this function before robot.Start()
  // The speed can be set to 1~100
  //robot.SetActionSpeed(75);
  // Start Freenove Hexapod Robot with default function
  robot.SetActionGroup(2);
  Serial.begin(9600);
  robot.Start();
}

void loop() {
  while (Serial.available() > 0) {
    data = Serial.readStringUntil('\n');

    if (data == "f") {
      for (int i = 0; i < movement_loops; i++) {
        robot.CrawlForward();
      }
    } else if (data == "r") {
      for (int i = 0; i < movement_loops; i++) {
        robot.CrawlRight();
      }
    } else if (data == "l") {
      for (int i = 0; i < movement_loops; i++) {
        robot.CrawlLeft();
      }
    } else if (data == "b") {
      for (int i = 0; i < movement_loops; i++) {
        robot.CrawlBackward();
      }
    } else {
    delay(1000);
    }
  delay(1000);
  }
}

