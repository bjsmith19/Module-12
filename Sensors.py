from setup import RPL
import post_to_web as PTW

sensor_pin = 16
RPL.pinMode(16,RPL.INPUT)

while True:
  PTW.state['d1'] = RPL.digitalRead(16)
  PTW.post()
