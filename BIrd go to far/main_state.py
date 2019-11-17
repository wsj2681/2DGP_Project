from pico2d import *
import game_framework
import game_world
import pause_state
import result_state
import Hero
import Map
import Ground
from Monster import Monster
from Obstacle import Obstacle
from UI_Hp import Hp
from egg import Egg
from UI_Score import Score
import Item

name = "MainState"

background = None
ground = None
hero = None
item = None
ui_hp = None
ui_score = None
eggs = []
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
    global hero, background, item, monsters, obstacles, ui_hp, ui_score, ground

    background = Map.Map()
    game_world.add_object(background, 0)
    ground = Ground.Ground()
    game_world.add_object(ground, 0)

    hero = Hero.Hero()
    game_world.add_object(hero, 1)

    monsters = [Monster() for i in range(50)]
    game_world.add_objects(monsters, 1)
    obstacles = [Obstacle() for i in range(50)]
    game_world.add_objects(obstacles, 1)

    '''
    for i in range(4):
        item = Item.Item()
        game_world.add_object(item, 1)
    '''
    ui_score = Score()
    game_world.add_object(ui_score, 2)
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
        else:
            hero.handle_events(event)


def update():
    for game_object in game_world.all_objects():
        game_object.update()
        if isinstance(game_object, Egg):
            eggs.append(game_object)

    for monster in monsters:
        for egg in eggs:
            if collide(egg, monster):
                monster.x, monster.y = 0, 0
                egg.x, egg.y = -100, 0
                game_world.remove_object(monster)
                monsters.remove(monster)
                game_world.remove_object(egg)
                eggs.remove(egg)
                ui_score.score += 100

    for obstacle in obstacles:
        if collide(hero, obstacle):
            obstacle.x, obstacle.y = 0, 0
            game_world.remove_object(obstacle)
            ui_hp.life -= 1
    if ui_hp.life == 10:
        game_framework.change_state(result_state)


def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()


def pause(): pass


def resume(): pass
