import cv2
import threading
import numpy as np

class EdgeDetectionThread(threading.Thread):
    def __init__(self, camera_thread):
        super(EdgeDetectionThread, self).__init__()
        self.camera_thread = camera_thread
        self.edges = None
        self.running = True

    def run(self):
        while self.running:
            frame = self.camera_thread.get_frame()
            if frame is not None:
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                edges = cv2.Canny(gray, 200, 600) # parameters for edges
                edges = cv2.dilate(edges, None, iterations=2) # iteration - thickness of edges
                edges_colored = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
                edges_colored[np.where((edges_colored == [255, 255, 255]).all(axis=2))] = [0, 0, 255]
                self.edges = edges_colored

    def stop(self):
        self.running = False

    def get_edges(self):
        return self.edges