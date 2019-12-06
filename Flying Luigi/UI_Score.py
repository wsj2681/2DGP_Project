from pico2d import *


class Score:
    def __init__(self):
        self.font = load_font('DungGeunMo.TTF', 24)
        self.score = 0.0

    def update(self):
        pass

    def draw(self):
        self.font.draw(650, 525, 'Score: %1.f' % self.score, (255, 0, 0))
