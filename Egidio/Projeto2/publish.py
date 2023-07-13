import paho.mqtt.client as mqtt

TOPIC = "aula05/bitcoin"

IP_BROKER = "test.mosquitto.org"

client = mqtt.Client("EHolanda")

print("connecting to broker...")
client.connect(IP_BROKER)#connect to

client.publish(TOPIC,'Boa noite galeraaa')