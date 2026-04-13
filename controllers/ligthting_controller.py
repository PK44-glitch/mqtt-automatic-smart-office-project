import paho.mqtt.client as mqtt
from devices.ligth_device import turn_on, turn_off

motion_detected = 0


def process_data(sensor_type, value):
    global motion_detected

    if sensor_type == "motion":
        motion_detected = value
        handle_light()


def handle_light():
    if motion_detected == 1:
        turn_on()
    else:
        turn_off()


def on_message(client, userdata, msg):
    value = int(msg.payload.decode())
    print("Received:", value)
    process_data("motion", value)


def run_controller():
    client = mqtt.Client()
    client.on_message = on_message

    client.connect("broker.hivemq.com", 1883, 60)
    client.subscribe("office/motion")

    client.loop_forever()


if __name__ == "__main__":
    run_controller()