# This class is used to mock the PiCamera class


class PiCamera:

    def __init__(self):
        print("MOCKING new Camera object")

    def start_preview(self):
        print("MOCKING camera start_preview")
        pass

    def stop_preview(self):
        print("MOCKING camera stop_preview")
        pass

    def capture(self, location):
        print("MOCKING camera capture at {0}".format(location))
        pass

    def start_recording(self, location):
        print("MOCKING camera start_recording at {0}".format(location))
        pass

    def stop_recording(self):
        print("MOCKING camera stop_recording")
        pass