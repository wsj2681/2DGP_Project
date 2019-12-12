from pico2d import *
import game_framework
import random

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 10


class Obstacle_right:
    image = None

    def __init__(self):
        self.x, self.y = random.randint(1000, 5000), random.randint(125, 550)
        self.random_x = random.randint(100, 400)
        self.frame = 0
        if Obstacle_right.image is None:
            Obstacle_right.image = load_image('Images/Obstacle_right.png')

    def get_bb(self):
        return self.x - 17, self.y - 20, self.x + 17, self.y + 19

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 10
        self.x -= self.random_x * game_framework.frame_time
        if self.x < -100:
            self.x, self.y = random.randint(1000, 5000), random.randint(125, 550)

    def draw(self):
        self.image.clip_draw(int(self.frame) * 40, 0, 40, 48, self.x, self.y)
        # draw_rectangle(*self.get_bb())


class Obstacle_left:
    image = None

    def __init__(self):
        self.x, self.y = random.randint(-2000, -500), random.randint(125, 550)
        self.random_x = random.randint(100, 400)
        self.frame = 0
        if Obstacle_left.image is None:
            Obstacle_left.image = load_image('Images/Obstacle_left.png')

    def get_bb(self):
        return self.x - 17, self.y - 20, self.x + 17, self.y + 19

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 10
        self.x += self.random_x * game_framework.frame_time
        if self.x > 900:
            self.x, self.y = random.randint(-2000, -500), random.randint(125, 550)

    def draw(self):
        self.image.clip_draw(int(self.frame) * 40, 0, 40, 48, self.x, self.y)
        # draw_rectangle(*self.get_bb())
