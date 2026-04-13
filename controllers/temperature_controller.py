import json
import paho.mqtt.client as mqtt

BROKER = "broker.hivemq.com"
PORT = 1883
TOPIC = "office/group21/temperature"
CONTROL_TOPIC = "office/group21/control"

#when the message arrives
def on_message(client, userdata, msg):  #sensor send in data
    payload = msg.payload.decode()
    data = json.loads(payload)

    temperature = data["temperature"]
    print(f"Received temperature: {temperature}°C")

    # controller command for heating and cooling
    if temperature > 20:
      print("Alert: Temperature is too high! Turning heater OFF and fan ON")
      client.publish(CONTROL_TOPIC, "HEATER_OFF")
      client.publish(CONTROL_TOPIC, "FAN_ON")

    elif temperature <15:
      print ("Alert: Temperature is too low! Turning heater ON and fan OFF")
      client.publish(CONTROL_TOPIC, "HEATER_ON")
      client.publish(CONTROL_TOPIC, "FAN_OFF")
    else:
      print("Temperature is currently normal. Fan and heater OFF")
      client.publish(CONTROL_TOPIC, "HEATER_OFF")
      client.publish(CONTROL_TOPIC, "FAN_OFF")

client = mqtt.Client(client_id="TemperatureController01")
client.on_message = on_message #processes the message/data from the client

client.connect(BROKER, PORT) #this connects the client to the broker
client.subscribe(TOPIC) #subscribes to sensor topic
print("MQTT Controller Started.. Waiting for data")

client.loop_forever() #waits for data till it receives it