import RoboPiLib as RPL
import setup
x = 1
Sensor_pin = 16
Sensor_pin = 15
RPL.pinMode(sensor_pin,RPL.INPUT)
while x == 1:
    reading = RPL.digitalRead(16)
    reading = RPL.digitalRead(15)
    if reading == 0:
        RPL.servoWrite(0, 1600)
    elif reading == 1:
        RPL.servoWrite(0, 1500)
