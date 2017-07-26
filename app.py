from MotionSensor import MotionSensor
from Camera import Camera


def main():
    cam = Camera()
    sensor = MotionSensor()

    picLocation = '/home/pi/Desktop/SecurityImages/'

    vidLocation = '/home/pi/Desktop/SecurityVideos/'

    #for i in range(2):
    #    cam.TakePicture("{0}image{1}.jpg".format(picLocation, i + 2))

    #cam.TakeVideo("{0}testvideo.h264".format(vidLocation), 5)

    motion_detected = sensor.checkformotion()

if __name__ == '__main__':
    main()
