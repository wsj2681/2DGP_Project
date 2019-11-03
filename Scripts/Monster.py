from pico2d import *
import random


class Monster:
    image = None

    def __init__(self):
        self.x, self. y = 750, 75
        self.random_x = random.randint(1, 10)
        self.frame = 0
        if Monster.image is None:
            Monster.image = load_image('Images/monster_idle.png')

    def update(self):
        self.frame = (self.frame + 1) % 4
        self.x -= self.random_x
        if self.x < 0:
            self. x = 750

    def draw(self):
        self.image.clip_draw(self.frame * 120, 0, 120, 100, self.x, self.y)

