from machine import Pin
import time as t
import usocket as socket
import network

w = network.WLAN(network.STA_IF)
n = 0
ssid = "Mukund_4G"
pwd = "Mukund@2005"
sys = Pin(17,Pin.OUT)
led = Pin(2,Pin.OUT)
r1 = Pin(14,Pin.OUT)
r2 = Pin(27,Pin.OUT)
r3 = Pin(26,Pin.OUT)
r4 = Pin(25,Pin.OUT)
sys.value(0)
led.value(0)
r1.value(1)
r2.value(1)
r3.value(1)
r4.value(1)
led_state = "OFF"
r1_state = "OFF"
r2_state = "OFF"
r3_state = "OFF"
r4_state = "OFF"

# Switching off and on to establish a new connection
w.active(False)
t.sleep(1)
w.active(True)

w.connect(ssid, pwd)

if not w.isconnected():
    sys.value(0)
    while not w.isconnected() and n < 5:
        print(5-n)
        n = n + 1
        t.sleep(1)

if w.isconnected():
    print(">>>>>>>>>>>>",w.ifconfig()[0],"<<<<<<<<<<<<")
    sys.value(1)


html='''
<!DOCTYPE html>
<html>
<head>
<title>ESP32 view</title>
<style>
.btn0{FONT-SIZE: 20px; HEIGHT: 35px; FONT-FAMILY: Arial; WIDTH: 100px}
.btn1{FONT-SIZE: 20px; HEIGHT: 35px; FONT-FAMILY: Arial; WIDTH: 100px}
div{width: 500px;
  height: 400px;  
  border: 1px solid red;
  background-color: grey;
}
</style>
</head>
<body style= "background-color: powderblue">
<center>
<div>
<h1>ESP32 Home Automation</h1>
<h2>Test LED
<button class='btn0' id='TH' onClick=location.href=\"/LED/H\">ON</button>
<button class='btn1' id='TL' onClick=location.href=\"/LED/L\">OFF</button>
<h4 id='led' hidden>%s</h4>
</h2>
<h2>1. Light
<button class='btn0' id='L1H' onClick=location.href=\"/S1/H\">ON</button>
<button class='btn1' id='L1L' onClick=location.href=\"/S1/L\">OFF</button>
<h4 id='s1' hidden>%s</h4>
</h2>
<h2>2. Light
<button class='btn0' id='L2H' onClick=location.href=\"/S2/H\">ON</button>
<button class='btn1' id='L2L' onClick=location.href=\"/S2/L\">OFF</button>
<h4 id='s2' hidden>%s</h4>
</h2>
<h2>3. Light
<button class='btn0' id='L3H' onClick=location.href=\"/S3/H\">ON</button>
<button class='btn1' id='L3L' onClick=location.href=\"/S3/L\">OFF</button>
<h4 id='s3' hidden>%s</h4>
</h2>
<h2>4. Light
<button class='btn0' id='L4H' onClick=location.href=\"/S4/H\">ON</button>
<button class='btn1' id='L4L' onClick=location.href=\"/S4/L\">OFF</button>
<h4 id='s4' hidden>%s</h4>
</h2>
<h2>ALL Sockets
<button class='btn0' id='A4H' onClick=location.href=\"/ALL/H\">ON</button>
<button class='btn1' id='A4L' onClick=location.href=\"/ALL/L\">OFF</button>
</div>
</center>
<script>
var str0 = document.getElementById('led').textContent
var str1 = document.getElementById('s1').textContent
var str2 = document.getElementById('s2').textContent
var str3 = document.getElementById('s3').textContent
var str4 = document.getElementById('s4').textContent
var str5 = str1+str2+str3+str4
if (str0 == 'ON'){document.getElementById('TH').disabled = true; document.getElementById('TL').removeAttribute('disabled');}
else if (str0 == 'OFF'){document.getElementById('TL').disabled = true; document.getElementById('TH').removeAttribute('disabled');}
if (str1 == 'ON'){document.getElementById('L1H').disabled = true; document.getElementById('L1L').removeAttribute('disabled');}
else if (str1 == 'OFF'){document.getElementById('L1L').disabled = true; document.getElementById('L1H').removeAttribute('disabled');}
if (str2 == 'ON'){document.getElementById('L2H').disabled = true; document.getElementById('L2L').removeAttribute('disabled');}
else if (str2 == 'OFF'){document.getElementById('L2L').disabled = true; document.getElementById('L2H').removeAttribute('disabled');}
if (str3 == 'ON'){document.getElementById('L3H').disabled = true; document.getElementById('L3L').removeAttribute('disabled');}
else if (str3 == 'OFF'){document.getElementById('L3L').disabled = true; document.getElementById('L3H').removeAttribute('disabled');}
if (str4 == 'ON'){document.getElementById('L4H').disabled = true; document.getElementById('L4L').removeAttribute('disabled');}
else if (str4 == 'OFF'){document.getElementById('L4L').disabled = true; document.getElementById('L4H').removeAttribute('disabled');}
if (str5'ONONONON'){document.getElementById('A4H').disabled = true; document.getElementById('A4L').removeAttribute('disabled');}
else {document.getElementById('A4L').disabled = true; document.getElementById('A4H').removeAttribute('disabled');}
</script>
</body>
</html>
 '''


soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = ""
port = 80
soc.bind((host,port))

soc.listen(5)


while True:
    cl, addr = soc.accept()
#     print(">>>>>>>>>>>>",addr,"<<<<<<<<<<<<")
    req = cl.recv(1024)
    req = str(req)
#     print("*****************************")
#     print("Contents.....", req)
#     print("*****************************")
    led_on = req.find('/LED/H')
    led_off = req.find('/LED/L')
    r1_on = req.find('/S1/H')
    r2_on = req.find('/S2/H')
    r3_on = req.find('/S3/H')
    r4_on = req.find('/S4/H')
    r1_off = req.find('/S1/L')
    r2_off = req.find('/S2/L')
    r3_off = req.find('/S3/L')
    r4_off = req.find('/S4/L')
    a_on = req.find('/ALL/H')
    a_off = req.find('/ALL/L')
    
    if led_on == 6:
        led.value(1)
        led_state = "ON"
    elif led_off == 6:
        led.value(0)
        led_state = "OFF"
    elif r1_on == 6:
        r1.value(0)
        r1_state = "ON"
    elif r1_off == 6:
        r1.value(1)
        r1_state = "OFF"
    elif r2_on == 6:
        r2.value(0)
        r2_state = "ON"
    elif r2_off == 6:
        r2.value(1)
        r2_state = "OFF"
    elif r3_on == 6:
        r3.value(0)
        r3_state = "ON"
    elif r3_off == 6:
        r3.value(1)
        r3_state = "OFF"
    elif r4_on == 6:
        r4.value(0)
        r4_state = "ON"
    elif r4_off == 6:
        r4.value(1)
        r4_state = "OFF"
    elif a_on == 6:
        r1.value(0)
        r2.value(0)
        r3.value(0)
        r4.value(0)
        r1_state = "ON"
        r2_state = "ON"
        r3_state = "ON"
        r4_state = "ON"
    elif a_off == 6:
        r1.value(1)
        r2.value(1)
        r3.value(1)
        r4.value(1)
        r1_state = "OFF"
        r2_state = "OFF"
        r3_state = "OFF"
        r4_state = "OFF"
    
    res = html % (led_state, r1_state, r2_state, r3_state, r4_state)
    cl.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
    cl.send(res)
    cl.close()


