from pico2d import *


class Hero:
    def __init__(self):
        self.image = load_image('Images/45.png')
        self.x, self.y = 100, 600
        self.vel = None
        self.gravity = None

    def update(self):
        self.y -= 1
        if self.y < 100:
            self. y = 600
            # game_framework.push_state(result_state)
            # print("go result state")

    def smash(self):
        pass

    def draw(self):
        self.image.draw(self.x, self.y)

    def collusion(self):
        pass
