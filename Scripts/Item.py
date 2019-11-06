from pico2d import *
import random
# 추가 아이템 목록
# 덫
# 회복
# 몬스터 속도 감소
# 몬스터 속도 증가


class Trap:
    image = None

    def __init__(self):
        self.x, self.y = 750, 75
        self. random_x = random.randint(1, 5)
        self.frame = 0
        if Trap.image is None:
            Trap.image = load_image('Images/boom.png')

    def update(self):
        self.frame = (self.frame + 1) % 1
        self.x -= self.random_x
        if self.x < 0:
            self.x = 750

    def draw(self):
        self.image.draw(self.x, self.y, 100, 100)


class Heart:
    def __init__(self):
        pass

    def update(self):
        pass

    def draw(self):
        pass


class VelocityUp:
    def __init__(self):
        pass

    def update(self):
        pass

    def draw(self):
        pass


class VelocityDown:
    def __init__(self):
        pass

    def update(self):
        pass

    def draw(self):
        pass
