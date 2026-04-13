import json
import time
import random
import paho.mqtt.client as mqtt

BROKER = "localhost"
ROOM = "room1"

TOPIC_SENSOR = f"meetingroom/{ROOM}/sensor"
TOPIC_CONTROL = f"meetingroom/{ROOM}/control"

# When connected
def on_connect(client, userdata, flags, rc):
    print("Connected" if rc == 0 else "Connection failed")
    client.subscribe(TOPIC_CONTROL)

# When message received
def on_message(client, userdata, msg):
    try:
        data = json.loads(msg.payload.decode())
        print("Received:", data)
    except:
        print("Invalid message")

# Setup client
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER, 1883, 60)
client.loop_start()

# Main loop
try:
    while True:
        data = {
            "room": ROOM,
            "temperature": round(random.uniform(20, 25), 1),
            "occupancy": random.choice([True, False])
        }

        client.publish(TOPIC_SENSOR, json.dumps(data))
        print("Sent:", data)

        time.sleep(5)

except KeyboardInterrupt:
    print("Stopping...")
    client.loop_stop()
    client.disconnect()