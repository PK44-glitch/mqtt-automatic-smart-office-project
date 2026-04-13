from mqtt.mqtt_client import connect 
import json 

topic_alarm = "smart_office/security/alarm"
client = connect() 

def on_connect(client, userdata, flags, rc):
    print("Alarm device connected")
    client.subscribe(topic_alarm) 

def on_message(client, userdata, msg): 
    data = json.loads(msg.payload.decode())

    if data["alarm_status"] == "ON": 
        print("ALARM IS ON")
        print("Reason:", data["reason"]) 
        print("Time:", data["time"])
    else: 
        print("ALARM IS OFF")
        print("Reason:", data["reason"])
        print("Time:", data["time"])

def run_alarm():
    client = connect()
    client.on_connect = on_connect
    client.on_message = on_message
    client.loop_forever()

if __name__ == "__main__":
    run_alarm()
    




