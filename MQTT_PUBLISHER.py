import paho.mqtt.client as paho
from paho import mqtt
import time
from time import sleep
import RPi.GPIO as GPIO
import Adafruit_DHT


PIN_DHT = 4



# define static variable
# broker = "localhost" # for local connection
broker = "broker.hivemq.com"  # for online version
port = 1883
timeout = 60

username = ''
password = ''
topic = "KELAPAN"

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
 
def on_publish(client,userdata,result):
	print("data published \n")
	


client1 = paho.Client("device1",userdata=None,protocol=paho.MQTTv5)
client1.username_pw_set(username=username,password=password)
client1.on_connect = on_connect
client1.on_publish = on_publish
client1.connect(broker,port,timeout)

def initSensor():
	#GPIO Mode (BOARD / BCM)
	GPIO.setmode(GPIO.BCM)
	
def getSensor():
    DHT_SENSOR = Adafruit_DHT.DHT11
    DHT_PIN = 4
    humidity = None
    temperature = None

    while temperature is None:
        humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
        time.sleep(1)

    return temperature


initSensor()
    

while True:
	message = getSensor()
	ret = client1.publish(topic,payload=message,qos=2)
	print(f'message: {message}')
	sleep(1)