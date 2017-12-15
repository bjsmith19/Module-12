import RoboPiLib.RoboPiLib as RPL
import RoboPiLib.setup

sensor_pin = 17
RPL.pinMode(sensor_pin,RPL.INPUT)

while True:
  PTW.state['d1'] = RPL.digitalRead(sensor_pin)
  PTW.post()
