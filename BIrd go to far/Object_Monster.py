from pico2d import *
import random
import game_framework
import game_world

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 16

class Monster:
    image = None

    def __init__(self):
        self.x, self. y = random.randint(1000, 10000), 60
        self.random_x = random.randint(100, 700)
        self.frame = 0
        if Monster.image is None:
            Monster.image = load_image('Images/Monster.png')

    def get_bb(self):
        return self.x - 25, self.y - 25, self.x + 25, self.y + 25

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 16
        self.x -= self.random_x * game_framework.frame_time
        if self.x < 0:
            self. x = random.randint(1000, 10000)

    def draw(self):
        self.image.clip_draw(int(self.frame) * 64, 0, 64, 64, self.x, self.y)
        # draw_rectangle(*self.get_bb())

    def remove(self):
        game_world.remove_object(self)

