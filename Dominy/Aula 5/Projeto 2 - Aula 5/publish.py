#Publish
import paho.mqtt.client as mqtt
TOPIC = "Dominy&Juvenal" #topico
IP_BROKER = 'test.mosquitto.org' #ip
client = mqtt.Client("Dominy") #nome no usuário
print("connecting to broker")
client.connect(IP_BROKER) #connect to
client.publish(TOPIC,'Oi, Juvenal') #Mensagem