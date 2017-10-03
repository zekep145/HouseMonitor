from MotionSensor import MotionSensor
from Camera import Camera
from flask import Flask
from flask import render_template
import os

from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop


def main():
    app = Flask(__name__)
    cam = Camera()
    sensor = MotionSensor()

    dir_path = os.path.dirname(os.path.realpath(__file__))
    print(dir_path)
    picLocation = dir_path + '/static/test.jpg'
    vidLocation = '/home/pi/Desktop/SecurityVideos/'

    motion_detected = sensor.checkformotion()

    @app.route('/post/<int:post_id>')
    def show_post(post_id):
        # show the post with the given id, the id is an integer
        return 'Post %d' % post_id

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/takepicture')
    def takepicture():
        cam.TakePicture(picLocation)
        return render_template('picture.html')

    http_server = HTTPServer(WSGIContainer(app))
    http_server.listen(80)  # serving on port 5000
    IOLoop.instance().start()

if __name__ == '__main__':
    main()
