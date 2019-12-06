from pico2d import *
import game_framework
import random


# image_right size = x:2691, y:59
class Ground:
    def __init__(self):
        self.image = load_image('Images/grass.png')
        self.x, self.y = 2691//2, 0

        self.bgm = load_music('Sound/BGM.mp3')
        self.bgm.set_volume(64)
        self.bgm.repeat_play()

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        self.x -= 200 * game_framework.frame_time
        if self.x < 0:
            self.x = 2691//2

    def get_bb(self):
        return self.x - 2691//2, self.y - 30, self.x + 2691//2, self.y + 30


class Mountain:
    def __init__(self):
        self.image = load_image('Images/mountain.png')
        self.x, self.y = random.randint(400, 600), 30

    def draw(self):
        self.image.draw(self.x, self.y, 800, 188)

    def update(self):
        self.x -= 10 * game_framework.frame_time
        if self.x < -500:
            self.x = random.randint(500, 1000)