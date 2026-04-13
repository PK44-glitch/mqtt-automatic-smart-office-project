import time
import random

# Imports the time module used to pause the program using time.sleep()
from mqtt.mqtt_client import connect

client = connect()
# Connects to the MQTT broker and returns a client object


def publish_light_data():
    # Starts MQTT network loop and publishes data continuously
    # Runs in an infinite loop so sensor keeps sending data

    while True:
        light_level = random.randint(0, 1000)

        # Generate random light level
        print(f"[Sensor] Light Level: {light_level}")

        # Publish light level to MQTT topic
        client.publish("office/light_level", light_level)

        # Wait 5 seconds before sending next value
        time.sleep(5)


if __name__ == "__main__":
    publish_light_data()