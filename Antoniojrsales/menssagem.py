import paho.mqtt.client as mqtt
ID_DO_USER = 'pedrohmonteiro'
IP_BROKER = 'test.mosquitto.org'
client = mqtt.Client("pedrohmonteiro12")
print("connecting to broker")
client.connect(IP_BROKER) #connect to
client.publish(ID_DO_USER,'canta garotinho')


