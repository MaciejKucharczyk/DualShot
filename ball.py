import cv2
import numpy as np

class Ball:
    def __init__(self, x_pos, y_pos, speed, radius):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.speed = speed
        self.radius = radius
        self.window_width = None
        self.window_height = None

    def set_window_size(self, width, height):
        self.window_width = width
        self.window_height = height

    def move(self):
        self.x_pos += self.speed[0]
        self.y_pos += self.speed[1]

        if self.x_pos <= self.radius or self.x_pos >= self.window_width - self.radius:
            self.speed[0] *= -1

        if self.y_pos <= self.radius or self.y_pos >= self.window_height - self.radius:
            self.speed[1] *= -1

    def detect_collision(self, edges):
        edges_gray = cv2.cvtColor(edges, cv2.COLOR_BGR2GRAY)
        ret, edges_binary = cv2.threshold(edges_gray, 1, 255, cv2.THRESH_BINARY)
        mask = np.zeros_like(edges_binary)
        cv2.circle(mask, (self.x_pos, self.y_pos), self.radius, 255, -1)
        intersection = cv2.bitwise_and(mask, edges_binary)
        if cv2.countNonZero(intersection) > 0:
            self.speed[0] *= -1
            self.speed[1] *= -1

