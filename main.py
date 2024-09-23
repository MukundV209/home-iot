import os
import network
import urequests
import ubinascii
from creds import *

# WiFi connection function
def connect_wifi(ssid, password):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('Connecting to WiFi...')
        wlan.connect(ssid, password)
        while not wlan.isconnected():
            pass
    print('Connected to WiFi:', wlan.ifconfig())

# Delete the existing action.py if it exists
def delete_action_file():
    try:
        os.remove('action.py')
        print('Deleted existing action.py')
    except OSError:
        print('No action.py file found to delete')

# Download the new action.py from GitHub
def download_action_file(github_url):
    try:
        response = urequests.get(github_url)
        if response.status_code == 200:
            with open('action.py', 'w') as f:
                f.write(response.text)
            print('action.py downloaded successfully')
        else:
            print('Failed to download action.py:', response.status_code)
    except Exception as e:
        print('Error downloading action.py:', e)

# Run the action.py file
def run_action_file():
    try:
        with open('action.py') as f:
            exec(f.read())
        print('action.py executed successfully')
    except Exception as e:
        print('Error running action.py:', e)


# Main execution
connect_wifi(WIFI_SSID, WIFI_PASSWORD)
delete_action_file()
download_action_file(GITHUB_URL)
run_action_file()
