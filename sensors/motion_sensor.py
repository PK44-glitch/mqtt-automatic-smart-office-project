import time
import random
from mqtt.mqtt_client import connect

client = connect()

def publish_motion():
    while True:
        motion = random.choice([0, 1])  # 0 = no motion, 1 = motion
        print(f"[Sensor] Motion: {motion}")
        
        client.publish("office/motion", motion)
        time.sleep(5)

if __name__ == "__main__":
    publish_motion()
