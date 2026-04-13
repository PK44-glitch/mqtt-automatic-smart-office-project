import paho.mqtt.client as mqtt  #this imports the mqtt library so the device heater device can comminicate with the broker

#connect the heater device to the MQTT broker
BROKER = "broker.hivemq.com"  #the mqtt server
PORT = 1883
CONTROL_TOPIC = "office/group21/control"  #the channel where the commands are sent

def on_message(client, userdata, msg):  #this function will run whenever a message is received from the controller
    command = msg.payload.decode() #converts the message into a human-readable text
    print(f"Heater command received: {command}")

    if command == "HEATER_ON":  
        print("Heater is turned ON")
    elif command == "HEATER_OFF":
        print("Heater is turned OFF")

client = mqtt.Client(client_id="HeaterDevice01")
client.on_message = on_message

client.connect(BROKER, PORT)
client.subscribe(CONTROL_TOPIC) #tells the heater to listen to the control topic

print("Heater running...")
client.loop_forever() #keeps the program running so it can conntinuously recive messages from the controller