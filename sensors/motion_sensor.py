from mqtt.mqtt_client import connect
import json
from datetime import datetime
import time
import random

topic_security_motion = "smart_office/security/motion"
topic_light_motion = "office/motion"


def send_security_motion(client):
    message = {
        "motion_detected": True,
        "time": str(datetime.now())
    }

    client.publish(topic_security_motion, json.dumps(message))
    print("Security motion detected message sent")


def run_security_sensor():
    client = connect()
    client.loop_start()

    while True:
        user_input = input("Press Enter for security motion or type q to quit security sensor: ")

        if user_input.lower() == "q":
            break

        send_security_motion(client)

    client.disconnect()
    print("Security motion sensor stopped")


def run_lighting_sensor():
    client = connect()

    while True:
        motion = random.choice([0, 1])
        print("Lighting motion:", motion)
        client.publish(topic_light_motion, motion)
        time.sleep(5)


def run_sensor():
    run_security_sensor()


if __name__ == "__main__":
    run_sensor()