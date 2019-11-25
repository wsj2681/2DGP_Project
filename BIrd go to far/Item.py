from pico2d import *
import random
import game_framework
import game_world
# 추가 아이템 목록
# 덫
# 회복


class Item:
    image = None

    def __init__(self):
        if Item.image is None:
            Item.image = load_image('Images/heart.png')
        self.x, self.y = random.randint(1000, 10000), random.randint(125, 550)
        self.random_x = random.randint(100, 400)

    def draw(self):
        self.image.draw(self.x, self.y, 50, 50)
        draw_rectangle(*self.get_bb())

    def update(self):
        self.x -= self.random_x * game_framework.frame_time

    def get_bb(self):
        return self.x - 25, self.y - 25, self.x + 25, self.y + 25

    def remove(self):
        game_world.remove_object(self)
