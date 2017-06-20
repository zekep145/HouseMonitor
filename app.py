from MotionSensor import MotionSensor
from Camera import Camera

def main():

	cam = Camera()
	sensor = MotionSensor()

	location = '/home/pi/Desktop/SecurityImages/'

	for i in range(2):
		cam.TakePicture("{0}image{1}.jpg".format(location, i))


if __name__ == '__main__':

	main()	


