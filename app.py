from MotionSensor import MotionSensor
from Camera import Camera
from flask import Flask
from flask import render_template
from time import sleep
import os


def main():
    app = Flask(__name__)
    cam = Camera()
    sensor = MotionSensor()

    dir_path = os.path.dirname(os.path.realpath(__file__))
    picLocation = dir_path + '\\static\\'

    vidLocation = '/home/pi/Desktop/SecurityVideos/'

    motion_detected = sensor.checkformotion()

    @app.route('/post/<int:post_id>')
    def show_post(post_id):
        # show the post with the given id, the id is an integer
        return 'Post %d' % post_id

    cam.TakePicture(picLocation)

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/takepicture')
    def takepicture():
        cam.TakePicture(picLocation)
        return render_template('picture.html')

    app.run(debug=True)

if __name__ == '__main__':
    main()
