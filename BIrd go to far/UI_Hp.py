from pico2d import *

# 충돌에 따른 생명체크


class Hp:
    def __init__(self):
        self.x, self.y = 675, 575
        self.hp_x = load_image('Images/hp_x.png')
        self.hp_o = load_image('Images/hp_o.png')

    def update(self):
        pass

    def draw(self):
        self.hp_o.draw(self.x, self.y, 50, 50)
        self.hp_o.draw(self.x + 50, self.y, 50, 50)
        self.hp_x.draw(self.x + 100, self.y, 50, 50)
