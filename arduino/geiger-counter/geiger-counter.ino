// geiger-counter

#include <Arduino.h>

const int pin_Sensor = 3; // HIGH when GM tube event

const byte cmd_Run = 114; // ASCII 'r'

const byte state_Wait = 0;
const byte state_Run = 1;
byte state = state_Wait;

unsigned long start_Millis = 0;
unsigned long current_Millis = 0;
const unsigned long sample_Millis = 30000;

volatile unsigned long counts = 0;

void ISR_tube_event()
{
  counts++;
}

void setup()
{
  pinMode(pin_Sensor, INPUT);
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
      counts = 0;
      digitalWrite(LED_BUILTIN, HIGH);
      start_Millis = millis();
      interrupts();
      attachInterrupt(digitalPinToInterrupt(pin_Sensor), ISR_tube_event, FALLING);
      state = state_Run;
      break;
    }
  }
  switch (state)
  {
  case state_Run:
    current_Millis = millis();
    if (current_Millis - start_Millis > sample_Millis)
    {
      detachInterrupt(digitalPinToInterrupt(pin_Sensor));
      Serial.println(counts);
      Serial.flush();
      digitalWrite(LED_BUILTIN, LOW);
      state = state_Wait;
    }
    break;
  }
}
