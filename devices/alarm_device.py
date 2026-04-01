from mqtt.mqtt_client import connect 
import json 

topic_alarm = "smart_office/security/alarm"
client = connect() 

def on_message(client, userdata, msg): 
    data = json.loads(msg.payload.decode())

    if data["alarm_status"] == "ON": 
        print("ALARM ON:", data["reason"]) 
        print("Reason:", data["reason"]) 
        print("Time:", data["time"])
    else: 
        print("Alarm is OFF")
     

client.on_message = on_message
client.subscribe(topic_alarm)
client.loop_forever() 



