from pico2d import *
import random
import game_framework


class Monster:
    image = None

    def __init__(self):
        self.x, self. y = random.randint(1000, 10000), 60
        self.random_x = random.randint(100, 1000)
        self.frame = 0
        if Monster.image is None:
            Monster.image = load_image('Images/monster_idle.png')

    def get_bb(self):
        return self.x - 25, self.y - 25, self.x + 25, self.y + 25

    def update(self):
        self.frame = (self.frame + 1) % 4
        self.x -= self.random_x * game_framework.frame_time
        if self.x < 0:
            self. x = random.randint(1000, 10000)

    def draw(self):
        self.image.clip_draw(self.frame * 120, 0, 120, 100, self.x, self.y, 50, 50)
        draw_rectangle(*self.get_bb())

