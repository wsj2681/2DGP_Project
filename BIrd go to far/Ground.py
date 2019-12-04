from pico2d import *
import game_framework


class Ground:
    def __init__(self):
        self.image = load_image('Images/ground.png')
        self.x, self.y = 400, 0
        self.bgm = load_music('Sound/BGM.mp3')
        self.bgm.set_volume(64)
        self.bgm.repeat_play()

    def draw(self):
        self.image.draw(self.x, self.y, 800, 60)
        draw_rectangle(*self.get_bb())

    def update(self):
        pass

    def get_bb(self):
        return self.x - 400, self.y - 30, self.x + 400, self.y + 30
