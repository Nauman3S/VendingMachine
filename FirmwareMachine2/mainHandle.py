import os
import paho.mqtt.client as mqtt #import the client
import time
import time
import random, string
import vendHandler

vendIt=0
def getClientID():
    x = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
    return x

############
def on_message(client, userdata, message):
    global vendIt
    msgV=str(message.payload.decode("utf-8"))
    print("message received " ,str(message.payload.decode("utf-8")))
    print("message topic=",message.topic)
    print("message qos=",message.qos)
    print("message retain flag=",message.retain)

    if(message.topic=="vend-machine/vend"):
        print(msgV)
        if(msgV=='2'):
            print('vending')
            vendHandler.SetAngle(90)#rotate servo
            vendIt=1

    
########################################
broker_address="broker.hivemq.com"
#broker_address="iot.eclipse.org"
print("creating new instance")
client = mqtt.Client(getClientID()) #create new instance
client.on_message=on_message #attach function to callback
print("connecting to broker")
client.connect(broker_address) #connect to broker
client.loop_start() #start the loop

client.subscribe("vend-machine/vend")

start = time.time()
counter=5
while 1:
    #print("running")
    time.sleep(0.1)
    if(vendIt==1):
        if (time.time() - start > 1):
            start = time.time()
            counter = counter - 1
        if(counter<=0):
            vendIt=0
            counter=5
            vendHandler.SetAngle(0)#rotate servo

vendHandler.cleanUp()
