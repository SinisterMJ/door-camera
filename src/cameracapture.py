import cv2
from subprocess import Popen

class CameraCapture:
    def __init__(self):
        self.neolink = Popen(['/home/roth/development/door-camera/bin/neolink', 'rtsp', '--config=/home/roth/development/door-camera/bin/neolink.toml'])
        self.cv_capture = cv2.VideoCapture("rtsp://127.0.0.1:8554/Camera01/Main", cv2.CAP_FFMPEG)
        pass
        

    def retrieveImage(self):
        ret, frame = self.cv_capture.read()

        if ret:
            return frame
        else:
            return None


    def __del__(self):
        self.cv_capture.release()
        self.neolink.terminate()
        pass
