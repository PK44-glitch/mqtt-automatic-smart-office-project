import paho.mqtt.client as mqtt
##This code sets up the connection to an MQTT broker
#Here, I’m importing the Paho MQTT library.This allows Python to communicate using the MQTT protocol, which is commonly used in IoT systems like smart homes or offices.

BROKER = "broker.hivemq.com"
PORT = 1883
#BROKER → the server we are connecting to In this case: a public MQTT broker (

client = mqtt.Client()
#This creates an MQTT client object Think of it as your device’s identity on the networkIt will be used to:connect send messages receive messges

def connect():
    client.connect(BROKER, PORT, 60)
    return client
#Connects to the broker 60 = keepalive time (seconds) tells the broker “I’m still active” Returns the connected client so other parts of the system can use it