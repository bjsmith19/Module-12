import RoboPiLib.RoboPiLib as RPL
import RoboPiLib.setup

sensor_pin = 16


while True:
    sensorRead=RPL.pinMode(sensor_pin,RPL.INPUT)
    print sensorRead
