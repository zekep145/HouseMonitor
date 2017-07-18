# This class contains all methods that interact with the motion sensor
import RPi.GPIO as GPIO
import time

class MotionSensor:

    def __init__(self):
        print("Creating new MotionSensor Object")


    def waitformotion(self, seconds):
        timer = 1
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(26, GPIO.IN)
        print("Waiting for motion to be detected...")
        while timer/10 < seconds:
            if (GPIO.input(26) == 1):
                print("Motion detected!")
		break
            elif (GPIO.input(26) == 0):
                print("Motion not detected")
            time.sleep(0.1)
