from pico2d import *
import game_framework
# 땅 좌표 y = 20
# 추가 맵 이미지
# 맵 속도


class Map:
    def __init__(self):
        self.image = load_image('Images/background.png')
        self.x, self.y = 0, 300
        self. speed = 100

    def update(self):
        self.x -= self.speed * game_framework.frame_time
        if self.x < 0:
            self.x = 800

    def collusion(self):
        pass

    def draw(self):
        self.image.draw(self.x, self.y)
