# This class is used for controlling the camera
from picamera import PiCamera
from time import sleep

class Camera:

	camera = PiCamera()

	def __init__(self):
		print("Creating new Camera object")
		print("Previewing camera...")
		self.camera.start_preview()
		sleep(10)
		self.camera.stop_preview()
		

	def TakePicture(self, location):
		print("Focusing...")
		self.camera.start_preview()
		sleep(4)
		print("Taking picture!")
		self.camera.capture(location)
		self.camera.stop_preview()

	def TakeVideo(self, time):
		print("Fill in implementation") 
