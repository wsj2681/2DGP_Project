import game_framework
from pico2d import *
import title_state
import random

name = "MainState"

hero = None
grass = None
item = None
font = None


class Hero:
    def __init__(self):
        self.image = load_image('bird.png')
        pass

    def update(self):
        pass

    def draw(self):
        pass

    def collusion(self):
        pass


class Grass:
    def __init__(self):
        self.image = load_image('grass.png')
        pass

    def update(self):
        pass

    def collusion(self):
        pass

    def draw(self):
        self.image.draw(400, 30)


class Item:
    def __init__(self):
        pass


def enter():
    pass


def exit():
    global hero, grass, item
    del(hero)
    del(grass)
    del(item)


def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state)
        if event.type == SDL_KEYDOWN and event.key == SDLK_p:
            game_framework.push_state(pause_state)


def update():
    pass


def draw():
    pass


def collusion():
    pass