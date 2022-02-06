// spectrophotometry

#include <Arduino.h>
#include <Wire.h>
#include "SparkFun_AS7265X.h"

AS7265X sensor;

const byte cmd_Run = 114; // ASCII 'r'

const byte state_Wait = 0;
const byte state_Run = 1;
byte state = state_Wait;

float channel[18];
const int num_Samples = 10;

void setup()
{
  pinMode(LED_BUILTIN, OUTPUT);
  digitalWrite(LED_BUILTIN, HIGH);
  Serial.begin(115200);
  while (!Serial)
    ;
  digitalWrite(LED_BUILTIN, LOW);
}

void loop()
{
  if (Serial.available())
  {
    byte cmd = Serial.read();
    switch (cmd)
    {
    case cmd_Run:
      state = state_Run;
      break;
    }
  }
  switch (state)
  {
  case state_Run:
    digitalWrite(LED_BUILTIN, HIGH);
    // Prepare the sensor
    sensor.begin();
    sensor.setBulbCurrent(AS7265X_LED_CURRENT_LIMIT_100MA, AS7265x_LED_WHITE);
    sensor.setBulbCurrent(AS7265X_LED_CURRENT_LIMIT_25MA, AS7265x_LED_UV);
    sensor.setBulbCurrent(AS7265X_LED_CURRENT_LIMIT_50MA, AS7265x_LED_IR);
    sensor.setIntegrationCycles(127);
    sensor.setGain(AS7265X_GAIN_16X);
    sensor.setIndicatorCurrent(AS7265X_INDICATOR_CURRENT_LIMIT_1MA);
    sensor.disableIndicator();
    // Zero out the accumulating channel values
    for (int i = 0; i < 18; i++)
    {
      channel[i] = 0;
    }
    // Take multiple samples per channel
    for (int sample = 0; sample < num_Samples; sample++)
    {
      sensor.takeMeasurementsWithBulb();
      channel[0] += sensor.getCalibratedA();
      channel[1] += sensor.getCalibratedB();
      channel[2] += sensor.getCalibratedC();
      channel[3] += sensor.getCalibratedD();
      channel[4] += sensor.getCalibratedE();
      channel[5] += sensor.getCalibratedF();
      channel[6] += sensor.getCalibratedG();
      channel[7] += sensor.getCalibratedH();
      channel[8] += sensor.getCalibratedR();
      channel[9] += sensor.getCalibratedI();
      channel[10] += sensor.getCalibratedS();
      channel[11] += sensor.getCalibratedJ();
      channel[12] += sensor.getCalibratedT();
      channel[13] += sensor.getCalibratedU();
      channel[14] += sensor.getCalibratedV();
      channel[15] += sensor.getCalibratedW();
      channel[16] += sensor.getCalibratedK();
      channel[17] += sensor.getCalibratedL();
      delay(500);
    }
    sensor.disableBulb(AS7265x_LED_WHITE);
    sensor.disableBulb(AS7265x_LED_IR);
    sensor.disableBulb(AS7265x_LED_UV);
    // Average of each channel and sum all channel values
    for (int i = 0; i < 18; i++)
    {
      channel[i] /= num_Samples;
    }
    // Create CSV string of readings and send over USB
    for (int i = 0; i < 17; i++)
    {
      Serial.print(channel[i]);
      Serial.print(", ");
    }
    Serial.println(channel[17]);
    Serial.flush();
    digitalWrite(LED_BUILTIN, LOW);
    state = state_Wait;
    break;
  }
}
