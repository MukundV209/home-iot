from machine import Pin
import time

<<<<<<< HEAD
led = Pin(4, Pin.OUT)
=======
led = Pin(0, Pin.OUT)
>>>>>>> 0c38b2f3018037380542aee6c7f78de8a5d5f017
while True:
    led.value(1)
    time.sleep(1)
    led.value(0)
    time.sleep(1)
