import RoboPiLib.RoboPiLib as RPL
import RoboPiLib.setup

sensor_pin = 16
RPL.pinMode(sensor_pin,RPL.INPUT)

while True:
    sensorRead = RPL.digitalRead(sensor_pin)
    print sensorRead
