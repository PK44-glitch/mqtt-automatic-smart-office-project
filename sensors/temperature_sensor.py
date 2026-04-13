import time  #this controls the time intervals throughout the program
import random  #this generates a random temperature to simulate a real sensor
import json  # used to format data as JSON
import paho.mqtt.client as mqtt #this is the mqtt communication library

BROKER = "broker.hivemq.com"  # MQTT broker (public test broker)
PORT = 1883
TOPIC = "office/group21/temperature" #this is the channel where the data is sent 

# Create MQTT client
client = mqtt.Client(client_id="TemperatureSensor01") #cresates a sendor device/gives it ID for identification
client.connect(BROKER, PORT) #connects it to the broker

print("MQTT Temperature Sensor Started...")  #confirms that the program is up and running

while True:
    # Simulated temperature value (replace with real sensor later)
    temperature = round(random.uniform(18.0, 30.0), 2)

    # Create a structured JSON payload
    payload = {
        "temperature": temperature,
        "unit": "C"
    }
    
    message = json.dumps(payload)  # this converts dictionary to JSON string
    client.publish(TOPIC, message)
    print(f"Published temperature: {message}")

    # Publish temperature to MQTT topic
    #client.publish(TOPIC, temperature)

    #print(f"Published temperature: {temperature}°C") #shows live dtat in terminal

    time.sleep(5) # Wait 5 seconds before next temperature reading
    