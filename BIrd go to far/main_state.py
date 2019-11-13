from pico2d import *

import game_framework
import pause_state
import result_state
import Hero
import Item
import Map
from Monster import Monster
from Obstacle import Obstacle
from UI_Hp import Hp
import game_world

name = "MainState"

hero = None
item = None
ui_hp = None
background = None
monsters = []
obstacles = []


def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b:
        return False
    if right_a < left_b:
        return False
    if top_a < bottom_b:
        return False
    if bottom_a > top_b:
        return False

    return True


def enter():
    global hero, background, item, monsters, obstacles, ui_hp

    background = Map.Map()
    game_world.add_object(background, 0)
    hero = Hero.Hero()
    game_world.add_object(hero, 1)

    monsters = [Monster() for i in range(4)]
    game_world.add_objects(monsters, 1)
    obstacles = [Obstacle() for i in range(4)]
    game_world.add_objects(obstacles, 1)

    '''
    for i in range(4):
        item = Item.Item()
        game_world.add_object(item, 1)
    '''

    ui_hp = Hp()
    game_world.add_object(ui_hp, 2)


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
        else:
            hero.handle_events(event)


def update():
    for game_object in game_world.all_objects():
        game_object.update()
    for monster in monsters:
        if collide(hero, monster):
            monster.x, monster.y = 0, 0
            game_world.remove_object(monster)
    for obstacle in obstacles:
        if collide(hero, obstacle):
            obstacle.x, obstacle.y = 0, 0
            game_world.remove_object(obstacle)
            ui_hp.life -= 1
    if ui_hp.life == 100:
        game_framework.change_state(result_state)


def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()


def pause(): pass
def resume(): pass
