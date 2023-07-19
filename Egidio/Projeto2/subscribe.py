import paho.mqtt.client as mqtt
import time

def on_message(client, userdata, message):
    msg = message.payload.decode("utf-8")
    print('msg: '+msg)

IP_BROKER = 'test.mosquitto.org'

client = mqtt.Client("Eholanda")

client.on_message=on_message

print("connecting to broker...")

client.connect(IP_BROKER)

client.subscribe("aula05/bitcoin")

client.loop_forever()