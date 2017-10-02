# This class is used for controlling the camera
from Mocks.picamera import PiCamera
from time import sleep
from datetime import datetime


class Camera:
    camera = PiCamera()

    def __init__(self):
        print("Creating new Camera object")
        print("Previewing camera...")
        self.camera.start_preview()
        sleep(3)
        self.camera.stop_preview()
        self.camera.annotate_text = str(datetime.now())

    def TakePicture(self, location):
        print("Taking picture! Saving in {0}".format(location))
        self.camera.capture(location)
        self.camera.stop_preview()

    def TakeVideo(self, location, time):
        print("Taking video for {0} seconds!".format(time))
        self.camera.start_recording(location)
        for i in range(time):
            print(".")
            sleep(1)
        self.camera.stop_recording()
        self.camera.stop_preview()
