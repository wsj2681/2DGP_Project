from pico2d import *
import game_framework
import random

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 5

class Obstacle:
    image = None

    def __init__(self):
        self.x, self.y = random.randint(1000, 10000), random.randint(50, 550)
        self.random_x = random.randint(200, 500)
        self.frame = 0
        if Obstacle.image is None:
            Obstacle.image = load_image('Images/Obstacle_right.png')

    def get_bb(self):
        return self.x - 25, self.y - 25, self.x + 25, self.y + 25

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 5
        self.x -= self.random_x * game_framework.frame_time
        if self.x < 0:
            self.x = random.randint(1000, 10000)

    def draw(self):
        self.image.clip_draw(int(self.frame) * (40-3), 0, 35, 48, self.x, self.y)
        draw_rectangle(*self.get_bb())

