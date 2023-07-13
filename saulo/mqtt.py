import paho.mqtt.client as mqtt

TOPIC = "aula05/projeto02"
IP_BROKER = 'test.mosquitto.org'
client = mqtt.Client("Saolim")
print("connecting to broker")
client.connect(IP_BROKER)
client.publish(TOPIC,"Pikachu é o melhor pokemon!")