import paho.mqtt.client as mqtt

# define static variable
# broker = "localhost" # for local connection
broker = "broker.hivemq.com"  # for online version
port = 1883
timeout = 60

username = ''
password = ''

topic = "KELAPAN"
 
# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
 
    # Subscribing in on_connect() - if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe(topic,qos=2)
 
# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print("Topic " + msg.topic)
    payload_decoded = msg.payload.decode('utf-8')
    print(f'message received: {payload_decoded}')
          
        
# Create an MQTT client and attach our routines to it.
client = mqtt.Client("device0")
client.username_pw_set(username=username,password=password)
client.on_connect = on_connect
client.on_message = on_message
client.connect(broker, port, timeout)

client.loop_forever()