This is a IOT based micropython project that uses ESP32 controller board and Arduino IOT cloud service
The requirement of Git is to create a OTA like interference
This is not a automated OTA instead on knowing or makeing in a change which is commited and pushed. The user need to restart the device.
On restarting the device, it does not check for updates but instead it replaces and runs the action.py file.

Appart from the main and action files you will be requiring a file in the name "cred.py" which contains WIFI SSID, password, Device ID, Device key and git link.

This project starts by creating a cloud "thing" in arduino iot cloud where you will get dev id and cloud key.
