from mqtt.mqtt_client import connect 
import json 

topic_dashnorad = "smart_oficce/security/dashboard"
client = connect() 

def on_connect(client, userdata, flags, rc):
    print("Dashboard connected to broker")
    client.subscribe(topic_dashnorad)

def on_message(client, userdata, msg):
    data = json.loads(msg.payload.decode()) 

    print("----- DASHBOARD -----")
    print("Alarm Status:", data["alarm_status"])
    print("Reason:", data["reason"])
    print("Time:", data["time"])
    print("--------------------")                    

client.on_connect = on_connect
client.on_message = on_message

def run_dashboard(): 
    client.loop_forever()

if __name__ == "__main__": 
    run_dashboard() 