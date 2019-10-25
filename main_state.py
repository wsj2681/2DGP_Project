import game_framework
from pico2d import *
import pause_state
import result_state
import time

name = "MainState"

hero = None
grass = None
item = None
velocity = None
gravity = None

font = None


class Hero:
    def __init__(self):
        self.image = load_image('45.png')
        self.x, self.y = 100, 600

    def update(self):
        self.y -= 1
        if self.y < 100:
            self. y = 600
            # game_framework.push_state(result_state)
            # print("go result state")

    def draw(self):
        self.image.draw(self.x, self.y)

    def collusion(self):
        pass


class Grass:
    def __init__(self):
        self.image = load_image('background.png')
        self.x, self.y = 0, 300

    def update(self):
        self.x -= 5
        if self.x < 0:
            self.x = 800

    def collusion(self):
        pass

    def draw(self):
        self.image.draw(self.x, self.y)


class Item:
    def __init__(self):
        pass


def enter():
    global hero, grass, item
    hero = Hero()
    grass = Grass()
    item = Item()


def exit():
    global hero, grass, item
    del(hero)
    del(grass)
    del(item)


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        if event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.push_state(pause_state)
            print("go pause state")


def update():
    hero.update()
    grass.update()

def draw():
    clear_canvas()
    grass.draw()
    hero.draw()
    update_canvas()


def collusion():
    pass


def pause(): pass
def resume(): pass
