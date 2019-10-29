from Scripts import game_framework
from pico2d import *
import random


class Monster:
    image = None

    def __init__(self):
        self.x, self. y = 750, 35
        self.random_x = random.randint(0, 50)
        self. frame = 0
        if Monster.image is None:
            Monster.image is load_image('Images/froges.png')

    def update(self):
        self.frame = (self.frame + 1) % 5
        self.x -= self.random_x
        if self.x < 0:
            self. x = 750

    def draw(self):
        self.image.clip_draw(self.frame * 122, 984, 100, 100, self.x, self.y)

