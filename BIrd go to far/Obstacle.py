from pico2d import *
import game_framework
import random


class Obstacle:
    image = None

    def __init__(self):
        self.x, self.y = random.randint(1000, 10000), random.randint(50, 550)
        self.random_x = random.randint(200, 500)
        self.frame = 0
        if Obstacle.image is None:
            Obstacle.image = load_image('Images/obstacle.png')

    def get_bb(self):
        return self.x - 25, self.y - 25, self.x + 25, self.y + 25

    def update(self):
        self.frame = (self.frame + 1) % 1
        self.x -= self.random_x * game_framework.frame_time
        if self.x < 0:
            self.x = random.randint(1000, 10000)

    def draw(self):
        self.image.draw(self.x, self.y, 50, 50)
        draw_rectangle(*self.get_bb())
