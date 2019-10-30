from Scripts import game_framework
from pico2d import *
from Scripts import pause_state, result_state
from Scripts import Grass, Item, Hero, Monster

name = "MainState"

hero = None
grass = None
item = None
velocity = None
gravity = None
distance = None
font = None
delta_time = None
monsters =[]

def enter():
    global hero, grass, item, monsters, delta_time
    hero = Hero.Hero()
    grass = Grass.Grass()
    item = Item.Item()
    monsters = [Monster.Monster() for i in range(4)]

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
        if event.type == SDL_MOUSEMOTION:
            x, y = event.x, 600 - 1 - event.y
        if event.type == SDL_KEYDOWN and event.key == SDLK_LSHIFT:
            pass
        elif event.type == SDL_KEYDOWN and event.key == SDLK_LSHIFT:
            pass
        else:
            hero.handle_events(event);

def update():
    hero.update()
    grass.update()
    for monster in monsters:
        monster.update()


def draw():
    clear_canvas()
    grass.draw()
    hero.draw()
    for monster in monsters:
        monster.draw()
    update_canvas()


def collusion():
    pass


def pause(): pass
def resume(): pass
