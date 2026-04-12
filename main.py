from mqtt.mqtt_client import connect
from controllers.central_controller import process_message

def on_connect(client, userdata, flags, rc):
    print("Connected to broker")
    client.subscribe("office/light_level")
    client.subscribe("office/motion")

def on_message(client, userdata, msg):
    topic = msg.topic
    payload = msg.payload.decode()

    print(f"[MQTT] {topic}: {payload}")
    process_message(topic, payload)

client = connect()

client.on_connect = on_connect
client.on_message = on_message

client.loop_forever()