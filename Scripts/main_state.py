from Scripts import game_framework
from pico2d import *
from Scripts import pause_state, result_state
from Scripts import Map, Item, Hero, Monster, Obstacle

name = "MainState"

hero = None
background = None
item = None
velocity = None
gravity = None
distance = None
font = None
delta_time = None
monsters = []
obstacles = []


def enter():
    global hero, background, item, monsters, obstacles, delta_time
    hero = Hero.Hero()
    background = Map.Map()
    item = Item.Item()
    monsters = [Monster.Monster() for i in range(4)]
    obstacles = [Obstacle.Obstacle() for i in range(4)]


def exit():
    global hero, background, item, monsters, obstacles
    del(hero)
    del(background)
    del(item)
    del(monsters)
    del(obstacles)


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
            hero.handle_events(event)


def update():
    hero.update()
    background.update()
    for monster in monsters:
        monster.update()
    for obstacle in obstacles:
        obstacle.update()


def draw():
    clear_canvas()
    background.draw()
    hero.draw()
    for monster in monsters:
        monster.draw()
    for obstacle in obstacles:
        obstacle.draw()
    update_canvas()


def collusion():
    pass


def pause(): pass
def resume(): pass
