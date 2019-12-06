from pico2d import *
import random
import game_framework


class Map:
    def __init__(self):
        self.image = load_image('Images/back.png')
        self.x, self.y = 400, 300
        self. speed = 100

    def update(self):
        pass

    def collusion(self):
        pass

    def draw(self):
        self.image.draw(self.x, self.y, 800, 600)


class Cloud:
    image = None

    def __init__(self):
        self.x, self.y = random.randint(0, 1000), random.randint(300, 600)
        self.random_x = random.randint(50, 200)
        if Cloud.image is None:
            Cloud.image = load_image('Images/Cloud2.png')

    def update(self):
        self.x -= self.random_x * game_framework.frame_time
        if self.x < -100:
            self.x, self.y = random.randint(800, 1000), random.randint(300, 600)

    def draw(self):
        self.image.draw(self.x, self.y)


class Cloud2:
    image = None

    def __init__(self):
        self.x, self.y = random.randint(0, 1000), random.randint(300, 600)
        self.random_x = random.randint(50, 200)
        if Cloud.image is None:
            Cloud.image = load_image('Images/Cloud2.png')

    def update(self):
        self.x -= self.random_x * game_framework.frame_time
        if self.x < 0:
            self.x = random.randint(800, 1000)

    def draw(self):
        self.image.draw(self.x, self.y)
