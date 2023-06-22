import cv2
import numpy as np
import threading

class ColorChanger(threading.Thread):
    def __init__(self):
        super(ColorChanger, self).__init__()

    def run(self, color):
        blue = int(color[0]) + 10
        green = int(color[1]) - 10
        red = int(color[2]) - 10
        return (blue, green, red)