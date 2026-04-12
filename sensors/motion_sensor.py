<<<<<<< HEAD
import json 
from datetime import datetime 
from mqtt.mqtt_client import connect 

topic_motion = "smart_office/security/motion"

client = connect()
client.loop_start()

def send_motion():
    message = { 
       "motion_detected": True, 
       "time": str(datetime.now())
    }

    client.publish(topic_motion, json.dumps(message))
    print("Motion detected message sent")

def run_sensor(): 
    while True: 
        user_input = input("press enter to simulate motion or type q to quit:")

        if user_input.lower() == "q": 
            break 

        send_motion() 
    client.disconnect()
    print("Motion sensor stopped")

if __name__ == "__main__": 
    run_sensor() 


=======
import time
import random
from mqtt.mqtt_client import connect

client = connect()

def publish_motion():
    while True:
        motion = random.choice([0, 1])
        print(f"[Sensor] Motion: {motion}")
        
        client.publish("office/motion", motion)
        time.sleep(7)

if __name__ == "__main__":
    publish_motion()
>>>>>>> 379b398 (Added smart lighting controller and device integration)
