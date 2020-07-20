#include <Servo.h>

int pos = 0;

Servo servo_9;
 
void setup()
{
    Serial.begin(9600);    
    servo_9.attach(9);
    servo_9.write(pos);
}
 
void loop()
{
    pos = Serial.parseFloat();
    servo_9.write(pos);

    Serial.print(pos);
    delay(12);
}
