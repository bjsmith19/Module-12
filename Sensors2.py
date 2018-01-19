from setup import RPL
import post_to_web as PTW # see post_to_web.py for instructions

sensor_pin = 17
RPL.pinMode(sensor_pin,RPL.INPUT)

while True:
  PTW.state['d1'] = RPL.digitalRead(sensor_pin)
  PTW.post()
<<<<<<< HEAD
  
=======
>>>>>>> 358809a84c7c50b4be5ffe2e691556c0676b9dd8
