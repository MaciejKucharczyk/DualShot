import cv2
import threading
import numpy as np

class Ball(threading.Thread):
    def __init__(self, x_pos, y_pos, speed, radius):
        super(Ball, self).__init__()
        # self.ball_thread = ball_thread
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.speed = speed
        self.radius = radius

    def move(self, speed):
        self.x_pos += speed[0]
        self.y_pos += speed[1]

    def run(self, speed, width, height):
        # while self.running:
        self.move(speed)
        self.WindowDetection(width, height)

    def WindowDetection(self, window_width, window_height):
        # Wykrywanie odbić od krawędzi okna
        if self.x_pos + self.radius >= window_width or self.x_pos - self.radius <= 0:
            self.speed[1] *= -1

        if self.y_pos + self.radius >= window_height or self.y_pos - self.radius <= 0:
            self.speed[0] *= -1