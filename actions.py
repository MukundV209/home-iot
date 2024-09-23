from machine import Pin
import time
import network
from arduino_iot_cloud import ArduinoCloudClient
from secrets import *


led = Pin(2, Pin.OUT)
r1 = Pin(14, Pin.OUT)
r2 = Pin(27, Pin.OUT)
r3 = Pin(26, Pin.OUT)
r4 = Pin(25, Pin.OUT)
r1.value(1)
r2.value(1)
r3.value(1)
r4.value(1)

def led_stat(client, value):
    led.value(value)

def r1_stat(client, value):
    r1.value(not value)

def r2_stat(client, value):
    r2.value(not value)

def r3_stat(client, value):
    r3.value(not value)

def r4_stat(client, value):
    r4.value(not value)

def wifi_connect():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(WIFI_SSID, WIFI_PASSWORD)
    while not wlan.isconnected():
        print("Trying to connect....")
        time.sleep_ms(500)
    print(f"WiFi Connected {wlan.ifconfig()}")

wifi_connect()
    
# Create a client object to connect to the Arduino Cloud.
# For MicroPython, the key and cert files must be stored in DER format on the filesystem.
# Alternatively, a username and password can be used to authenticate:
client = ArduinoCloudClient(device_id=DEVICE_ID, username=DEVICE_ID, password=CLOUD_PASSWORD)

# Register Cloud objects.
# Note: The following objects must be created first in the dashboard and linked to the device.
# This Cloud object is initialized with its last known value from the Cloud. When this object is updated
# from the dashboard, the on_switch_changed function is called with the client object and the new value.

client.register("led1", value=None, on_write=led_stat, interval=0.250)
client.register("relay1", value=None, on_write=r1_stat, interval=0.250)
client.register("relay2", value=None, on_write=r2_stat, interval=0.250)
client.register("relay3", value=None, on_write=r3_stat, interval=0.250)
client.register("relay4", value=None, on_write=r4_stat, interval=0.250)

# Start the Arduino Cloud client.
client.start()