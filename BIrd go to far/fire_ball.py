from pico2d import *
import game_framework
import game_world


class Fireball:
    image = None

    def __init__(self, x=400, y=300, velocity=1):
        self.x, self.y, self.velocity = x, y, velocity
        if Fireball.image is None:
            Fireball.image = load_image('Images/fire_ball.png')

    def draw(self):
        self.image.draw(self.x, self.y, 24, 24)
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 12, self.y - 12, self.x + 12, self.y + 12

    def update(self):
        self.y -= self.velocity * game_framework.frame_time

        if self.y < 50:
            self.x = 25
            game_world.remove_object(self)
