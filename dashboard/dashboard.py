from mqtt.mqtt_client import connect 
import json 

topic_dashboard= "smart_office/security/dashboard"
client = connect() 

def on_connect(client, userdata, flags, rc):
    print("Dashboard connected to broker")
    client.subscribe(topic_dashboard)

def on_message(client, userdata, msg):
    data = json.loads(msg.payload.decode()) 

    print("----- DASHBOARD -----")
    print("Alarm Status:", data["alarm_status"])
    print("Reason:", data["reason"])
    print("Time:", data["time"])
    print("--------------------")                    


def run_dashboard():
    client = connect()
    client.on_connect = on_connect
    client.on_message = on_message
    client.loop_forever()

if __name__ == "__main__": 
    run_dashboard() 