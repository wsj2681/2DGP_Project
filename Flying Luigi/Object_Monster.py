from pico2d import *
import random
import game_framework
import game_world

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 16


class Monster_right:
    image = None

    def __init__(self):
        self.x, self. y = random.randint(1500, 7000), 55
        self.random_x = random.randint(100, 500)
        self.frame = 0
        if Monster_right.image is None:
            Monster_right.image = load_image('Images/Monster_right.png')

    def get_bb(self):
        return self.x - 25, self.y - 25, self.x + 25, self.y + 25

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 16
        self.x -= self.random_x * game_framework.frame_time
        if self.x < -100:
            self. x = random.randint(1500, 7000)

    def draw(self):
        self.image.clip_draw(int(self.frame) * 64, 0, 64, 70, self.x, self.y)
        # draw_rectangle(*self.get_bb())

    def remove(self):
        game_world.remove_object(self)


class Monster_left:
    image = None

    def __init__(self):
        self.x, self. y = random.randint(-6000, -500), 55
        self.random_x = random.randint(100, 500)
        self.frame = 0
        if Monster_left.image is None:
            Monster_left.image = load_image('Images/Monster_left.png')

    def get_bb(self):
        return self.x - 25, self.y - 25, self.x + 25, self.y + 25

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 16
        self.x += self.random_x * game_framework.frame_time
        if self.x > 900:
            self.x, self. y = random.randint(-6000, -500), 55

    def draw(self):
        self.image.clip_draw(int(self.frame) * 64, 0, 64, 70, self.x, self.y)
        # draw_rectangle(*self.get_bb())

    def remove(self):
        game_world.remove_object(self)