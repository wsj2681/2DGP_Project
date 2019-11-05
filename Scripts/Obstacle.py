from pico2d import *
import random


class Obstacle:
    image = None

    def __init__(self):
        self.x, self.y = 750, random.randint(400, 550)
        self.random_x = random.randint(1, 10)
        self.frame = 0
        if Obstacle.image is None:
            Obstacle.image = load_image('Images/obstacle.png')

    def update(self):
        self.frame = (self.frame + 1) % 1
        self.x -= self.random_x
        if self.x < 0:
            self.x = 750

    def draw(self):
        self.image.draw(self.x, self.y, 50, 50)
