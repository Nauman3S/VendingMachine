import os
import paho.mqtt.client as mqtt #import the client
import time
import time
import random, string
import vendHandler

vendIt=0
def getClientID():
    l = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    s=""
    for i in range(0,16):
        s=s+l[random.randint(0,25)]
    return s
    

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
            vendHandler.MotorHandle(True)#rotate servo
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
counter=5#turn motor on for 5 seconds
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
            vendHandler.MotorHandle(False)#turn off the motor

vendHandler.cleanUp()