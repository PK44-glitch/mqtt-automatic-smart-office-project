from mqtt.mqtt_client import connect 
import json 
from datetime import datetime 

topic_motion = "smart_office/security/motion"
topic_alarm = "smart_office/security/alarm"
topic_dashboard = "smart_office/security/dashboard"

#only kept in True while testing 
demo_mode = False 

client = connect() 

def is_late_hours(): 
    current_hour = datetime.now().hour 

    if demo_mode:
        return False 
    
    if current_hour >= 22 or current_hour < 6: 
        return True 
    else:
        return False
    
def on_connect(client, userdata, flags, rc):
    print("security controller connected to broker ")
    client.subscribe(topic_motion)

def on_message(client, userdata, msg):
    data = json.loads(msg.payload.decode())

    if data["motion_detected"] == True:
        if is_late_hours():
            message = {
                "alarm_status": "ON", 
                "reason": "Motion detected during late hours", 
                "time": str(datetime.now())
        }

        client.publish(topic_alarm, json.dumps(message))
        client.publish(topic_dashboard, json.dumps(message))
        print("Alarm message sent")

    else: 
        message = { 
            "alarm_status": "OFF",
            "reason": "Motion detected during normal hours ", 
            "time": str(datetime.now())
        }
        
        client.publish(topic_alarm, json.dumps(message))
        client.publish(topic_dashboard, json.dumps(message))
        print("No alarm, normal hours")

client.on_connect = on_connect
client.on_message = on_message 

def run_controller():
    client.loop_forever()

if __name__ == "__main__": 
    run_controller() 