import paho.mqtt.client as mqtt
from devices.ligth_device import turn_on, turn_off

light_level = None

def process_data(sensor_type, value):
    global light_level

    if sensor_type == "light":
        light_level = value
        handle_light()

def handle_light():
    if light_level is None:
        return

    if light_level < 300:
        turn_on()
    else:
        turn_off()

def on_message(client, userdata, msg):
    value = int(msg.payload.decode())
    print("Received:", value)
    process_data("light", value)

client = mqtt.Client()
client.on_message = on_message

client.connect("broker.hivemq.com", 1883, 60)
client.subscribe("office/light_level")

client.loop_forever()