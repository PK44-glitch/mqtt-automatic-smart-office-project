import json 
import time 
from datetime import datetime 

from paho.mqtt.client import connect 

BROKER = "broker.hivemq.com"
PORT = 1883 
# The MQTT topic used by the motion sensor 
topic_motion = "smart_office/security/motion"

client = connect()
client.loop_start()


def connect_mqtt(): 
    client.connect(BROKER, PORT, 60)
    print("Motion sensor connnected to broker")

def send_motion(): 
    message = { 
       "motion_detected": True, 
       "time": str(datetime.now)()
    }

    client.pusblish(topic_motion, json.dumps(message))
    print("Motion detected message sent")

def run_sensor(): 
    connect_mqtt() 

    while True: 
        user_input = input("press enter to simulate motion or type q to quit:")

        if user_input.lower()== "q": 
            break 

        send_motion() 
    client.disconnect()
    print("Motion sesnor stopped")

if __name__ == "__main__": 
    run_sensor() 


