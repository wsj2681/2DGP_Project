from pico2d import *

import game_framework
import pause_state
import result_state
import Hero
import Item
import Map
import Monster
import Obstacle
import UI_Hp
import game_world

name = "MainState"

hero = None
item = None
ui_hp = None
background = None
monsters = []
obstacles = []


def enter():
    global hero, background, item, monsters, obstacles, ui_hp

    obstacles = [Obstacle.Obstacle() for i in range(4)]
    monsters = [Monster.Monster() for i in range(4)]
    background = Map.Map()
    hero = Hero.Hero()
    item = Item.Item()
    ui_hp = UI_Hp.Hp()
    game_world.add_object(hero, 0)
    game_world.add_object(background, 1)


def exit():
    game_world.clear()


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        if event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.push_state(pause_state)
            print("go pause state")
        if event.type == SDL_KEYDOWN and event.key == SDLK_y:
            game_framework.push_state(result_state)
        else:
            hero.handle_events(event)


def update():
    for game_object in game_world.all_objects():
        game_object.update()


def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()


def pause(): pass
def resume(): pass
