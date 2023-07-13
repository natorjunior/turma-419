import paho.mqtt.client as mqtt

TOPIC = "Garrafa2"
IP_BROKER = 'test.mosquitto.org'
client = mqtt.Client("Saolim")
print("connecting to broker")
client.connect(IP_BROKER)
client.publish(TOPIC,"Pikachu é foda!")