import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)
GPIO.setup(3, GPIO.OUT)
# pwm=GPIO.PWM(3, 50)
# pwm.start(0)

def MotorHandle(st):

	
	GPIO.output(3, st)
	

def cleanUp():
	
    
    GPIO.cleanup()