import paho.mqtt.client as mqtt
import time
def on_message(client,userdata,message):
    msg = message.payload.decode("utf-8")
    print('msg:'+msg)
ip_broker = 'test.mosquitto.org'
client = mqtt.Client("pedromonteiro")
client.on_message=on_message
print ("connecting to broker")
client.connect(ip_broker)
client.subscribe("pedrohmonteiro")
client.loop_forever()

