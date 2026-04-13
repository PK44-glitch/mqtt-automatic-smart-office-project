import paho.mqtt.client as mqtt #this imports the mqtt library so the device fan device can comminicate with the broker

#connect the fan device to the MQTT broker
BROKER = "broker.hivemq.com" #the mqtt server
PORT = 1883
CONTROL_TOPIC = "office/group21/control" #the channel where the commands are sent

def on_message(client, userdata, msg): #this function will run whenever a message is received from the controller 
    command = msg.payload.decode() #converts the message into a readable text
    print(f"Fan command received: {command}")

    if command == "FAN_ON":  #if the controller sends a fan on message, the fan turns on
        print("Fan is turned ON")
    elif command == "FAN_OFF":
        print("Fan is turned OFF")

client = mqtt.Client(client_id="FanDevice01")
client.on_message = on_message

client.connect(BROKER, PORT)
client.subscribe(CONTROL_TOPIC)  #tells the fan to listen to the control topic

print("Fan device running...")
client.loop_forever()  #keeps the program running so it can continuosly receive messages from the controller 