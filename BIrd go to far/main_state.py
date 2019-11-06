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


name = "MainState"

hero = None
trap = None
ui_hp = None
background = None
monsters = []
obstacles = []


def enter():
    global hero, background, trap, monsters, obstacles, ui_hp

    obstacles = [Obstacle.Obstacle() for i in range(4)]
    monsters = [Monster.Monster() for i in range(4)]
    background = Map.Map()
    hero = Hero.Hero()
    trap = Item.Trap()
    ui_hp = UI_Hp.Hp()


def exit():
    global hero, background, trap, monsters, obstacles,ui_hp

    del hero
    del background
    del trap
    del monsters
    del obstacles
    del ui_hp


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
    hero.update()
    background.update()
    for monster in monsters:
        monster.update()
    for obstacle in obstacles:
        obstacle.update()
    trap.update()


def draw():
    clear_canvas()
    background.draw()
    for monster in monsters:
        monster.draw()
    for obstacle in obstacles:
        obstacle.draw()
    trap.draw()
    hero.draw()
    ui_hp.draw()
    update_canvas()


def pause(): pass
def resume(): pass