from pico2d import *
from Obejct_Hero import *

# 충돌에 따른 생명체크


class Hp:

    def __init__(self):
        self.x, self.y = 675, 575
        self.life_image = load_image('Images/life.png')
        self.life = 3
        self.font = load_font('DungGeunMo.TTF', 32)

    def update(self):
        pass

    def draw(self):
        self.life_image.draw(self.x + 30, self.y, 50, 50)
        self.font.draw(self.x + 60, self.y, 'X %1.f' % self.life, (255, 0, 0))