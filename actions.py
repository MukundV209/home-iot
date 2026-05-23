from machine import Pin
from hcsr04 import HCSR04
from time import sleep

led = Pin(2,Pin.OUT)
led.value(1)
sensor = HCSR04(trigger_pin=12, echo_pin=14)

while True:
    led.value(0)
    distance = sensor.distance_cm()
    print('Distance:', distance, 'cm')
    sleep(1)
    led.value(1)
