import RoboPiLib.RoboPiLib import RPL
import RoboPiLib.setup
import RoboPiLib.Post_to_web as PTW

sensor_pin ls = 16
RPL.pinMode(sensor_pin,RPL.INPUT)

while True:
  PTW.state['d1'] = RPL.digitalRead(sensor_pin)

PTW.post()
