from pico2d import *


class Grass:
    def __init__(self):
        self.image = load_image('background.png')
        self.x, self.y = 0, 300

    def update(self):
        self.x -= 5
        if self.x < 0:
            self.x = 800

    def collusion(self):
        pass

    def draw(self):
        self.image.draw(self.x, self.y)
