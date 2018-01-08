import RoboPiLib.RoboPiLib as RPL
import RoboPiLib.setup
import RoboPiLib.post_to_web as PTW

sensor_pin = 16
RPL.pinMode(sensor_pin,RPL.INPUT)

while True:
  PTW.state['d2'] = RPL.digitalRead(sensor_pin)
  PTW.post()
