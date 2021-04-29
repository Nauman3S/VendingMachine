import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)
# pwm=GPIO.PWM(3, 50)
# pwm.start(0)

def MotorHandle(st):

	
	GPIO.output(4, st)
	

def cleanUp():
	
    
    GPIO.cleanup()