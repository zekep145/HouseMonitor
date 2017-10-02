# This class contains all methods that interact with the motion sensor
import Mocks.GPIO as GPIO


class MotionSensor:

    def __init__(self):
        print("Creating new MotionSensor Object")

    def checkformotion(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(26, GPIO.IN)
        if GPIO.input(26) == 1:
            print("Motion detected!")
            return 1
        elif GPIO.input(26) == 0:
            return 0
