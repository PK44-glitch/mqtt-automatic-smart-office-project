import time
import random
#Imports the **time module**  Used to pause the program using `time.sleep()`
from mqtt.mqtt_client import connect

client = connect()
# This function: .connects to the MQTT broker .returns a client object  

def publish_light_data():
    #Starts the MQTT **network loop in the background**
#This is VERY important because:
# MQTT needs to constantly listen/send data  
#Without this, messages may not be delivered properly  
#Runs on a separate thread so your program can continue
    while True:
        light_level = random.randint(0, 1000)
        #Creates an **infinite loop**
#This means: the sensor keeps running continuously  keeps sending data forever  
        print(f"[Sensor] Light Level: {light_level}")
        
        client.publish("office/light_level", light_level)
# Helps with:- debugging  - monitoring what the sensor is sending time.sleep(5)

 if __name__ == "__main__":
    #pauses the program for 5 seconds
    #prevents -sending too many messages -overwhelming the system
    #the data is sent every 5 seconds
    publish_light_data() 
     #This scripts act as a publisher MQTT
     #it publishes the data and does not recieve the data
     