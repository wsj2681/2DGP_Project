from Scripts import game_framework
from pico2d import *
from Scripts import pause_state, result_state
from Scripts import Grass, Item, Hero

name = "MainState"

hero = None
grass = None
item = None
velocity = None
gravity = None
distance = None
font = None
delta_time = None


def enter():
    global hero, grass, item, delta_time
    hero = Hero.Hero()
    grass = Grass.Grass()
    item = Item.Item()


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
        if event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            hero.smash()


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
