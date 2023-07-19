
##mandando mensagem

# import paho.mqtt.client as mqtt
# TOPIC = "Conversa Teste"
# IP_BROKER = 'test.mosquitto.org'
# client = mqtt.Client("Walter")
# print("connecting to broker")
# client.connect(IP_BROKER) #connect to
# client.publish(TOPIC,'teste')

##recebendo mensagem

import paho.mqtt.client as mqtt
import time
def on_message(client, userdata, message):
    msg = message.payload.decode("utf-8")
    print('msg: '+msg)
IP_BROKER = 'test.mosquitto.org'
client = mqtt.Client("Walter")
client.on_message=on_message
print("connecting to broker")
client.connect(IP_BROKER)
client.subscribe("Garrafa2")
client.loop_forever()