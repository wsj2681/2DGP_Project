from pico2d import *


class Hero:
    def __init__(self):
        # image Size 100, 100
        self.image = load_image('Images/45.png')
        self.x, self.y = 100, 600
        self.vel = None
        self.gravity = 1

    def update(self):
        self.y -= 1 * self.gravity
        if self.y-50 < 20:
            self. y = 600
            # game_framework.push_state(result_state)
            # print("go result state")

    def smash(self, state):
        if state is 1:
            p1 = (self.x, self.y)
            p2 = (200, 25)
            for i in range(0, 100 + 1, 2):
                t = i/100
                self.x = (1-t)*p1[0]+t*p2[0]
                self.y = (1-t)*p1[1]+t*p2[1]
        else:
            self.update()

    def draw(self):
        self.image.draw(self.x, self.y)

    def collusion(self):
        pass
