#include <Arduino.h>
#include <stdint.h>
#include "Wire.h"
#include "SCMD.h"
#include "SCMD_config.h"
#include "Adafruit_MLX90393.h"

SCMD motorDriver;
Adafruit_MLX90393 magFieldSensor = Adafruit_MLX90393();

const byte cmd_Run = 114; // ASCII 'r'

const byte state_Wait = 0;
const byte state_Run = 1;
byte state = state_Wait;

void getFieldStrength(int step)
{
  const int numReads = 3;
  const unsigned long waitTime = 50;

  float x, y, z, totalZ;
  z = 0;
  totalZ = 0;
  for (int i = 0; i < numReads; i++)
  {
    delay(waitTime);
    magFieldSensor.readData(&x, &y, &z);
    totalZ += z;
  }
  float avgZ = totalZ / numReads;
  // Send data over USB
  Serial.print(step);
  Serial.print(",");
  Serial.println(avgZ);
}

void setup()
{
  pinMode(LED_BUILTIN, OUTPUT);
  digitalWrite(LED_BUILTIN, HIGH);
  Serial.begin(115200);
  while (!Serial)
    ;
  // Initialize motor driver
  motorDriver.settings.commInterface = I2C_MODE;
  motorDriver.settings.I2CAddress = 0x5D;
  motorDriver.begin();
  while (motorDriver.begin() != 0xA9)
    ;
  while (motorDriver.ready() == false)
    ;
  while (motorDriver.busy())
    ;
  motorDriver.enable();
  motorDriver.setDrive(0, 0, 0);
  motorDriver.setDrive(1, 0, 0);
  // Initialize magnetic field sensor
  while (magFieldSensor.begin_I2C() == false)
    ;
  magFieldSensor.setOversampling(MLX90393_OSR_2);
  magFieldSensor.setFilter(MLX90393_FILTER_6);
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
      digitalWrite(LED_BUILTIN, HIGH);
      state = state_Run;
      break;
    }
  }

  switch (state)
  {
  case state_Run:
    // Increase voltage from 0V to Vin
    for (int i = 0; i < 256; i++)
    {
      motorDriver.setDrive(0, 0, i);
      motorDriver.setDrive(1, 0, i);
      getFieldStrength(i);
    }
    // Decrease voltage from Vin to 0V
    for (int i = 255; i >= 0; i--)
    {
      motorDriver.setDrive(0, 0, i);
      motorDriver.setDrive(1, 0, i);
      getFieldStrength(i);
    }
    Serial.flush();
    digitalWrite(LED_BUILTIN, LOW);
    state = state_Wait;
    break;
  }
}