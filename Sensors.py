import RoboPiLib.RoboPiLib as RPL
import RoboPiLib.setup
import RoboPiLib.post_to_web as PTW

sensor_pin = 17
RPL.pinMode(sensor_pin,RPL.INPUT)

while True:
  PTW.state['d1'] = RPL.digitalRead(sensor_pin)
  PTW.post()
