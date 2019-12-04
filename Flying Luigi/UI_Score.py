from pico2d import *


class Score:
    def __init__(self):
        self.font = load_font('ENCR10B.TTF', 16)
        self.score = 0.0

    def update(self):
        pass

    def draw(self):
        self.font.draw(675, 525, 'Score: %3.f' % self.score, (255, 0, 0))
