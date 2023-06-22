import cv2
import threading

class CameraThread(threading.Thread):
    def __init__(self):
        super(CameraThread, self).__init__()
        self.camera = cv2.VideoCapture(0)
        self.frame = None
        self.running = True

    def run(self):
        while self.running:
            ret, frame = self.camera.read()
            if ret:
                self.frame = frame
        self.camera.release()

    def stop(self):
        self.running = False

    def get_frame(self):
        flipped_frame = cv2.flip(self.frame, 1)
        return self.frame