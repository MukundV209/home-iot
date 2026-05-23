from hcsr04 import HCSR04
from time import sleep

sensor = HCSR04(trigger_pin=12, echo_pin=14)

while True:
    distance = sensor.distance_cm()
    print('Distance:', distance, 'cm')
    sleep(1)
