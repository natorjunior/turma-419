import paho.mqtt.client as mqtt
topic = "antoniojrsales"
ip_broker = 'test.mosquitto.org'
client = mqtt.Client("abc")
print("connecting to broker")
client.connect(ip_broker) #connect to
client.publish(topic,'ó u tonhão')