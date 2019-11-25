from pico2d import *
import game_framework
import game_world
import pause_state
import result_state
import Clear_state
import Hero
import Map
import Ground
from Monster import Monster
from Obstacle import Obstacle
from UI_Hp import Hp
from fire_ball import Fireball
from UI_Score import Score
from Item import Item

name = "MainState"

background = None
ground = None
hero = None
itemes = []
ui_hp = None
ui_score = 0.0
balls = []
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
    global hero, background, itemes, monsters, obstacles, ui_hp, ui_score, ground

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

    itemes = [Item() for i in range(5)]
    game_world.add_objects(itemes, 1)

    ui_score = Score()
    game_world.add_object(ui_score, 2)

    ui_hp = Hp()
    game_world.add_object(ui_hp, 2)


def get_score():
    return ui_score


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

    for monster in monsters:
        for ball in balls:
            if collide(ball, monster):
                monster.x, monster.y = 0, 0
                ball.x, ball.y = -100, 0
                monsters.remove(monster)
                monster.remove()
                balls.remove(ball)
                game_world.remove_object(ball)
                ui_score.score += 100.0

    for obstacle in obstacles:
        if collide(hero, obstacle):
            obstacle.x, obstacle.y = 0, 0
            obstacles.remove(obstacle)
            game_world.remove_object(obstacle)
            ui_hp.life -= 1

    for item in itemes:
        if collide(item, hero):
            item.x, item.y = 0, 0
            itemes.remove(item)
            item.remove()
            ui_hp.life += 1

    if ui_hp.life == 10:
        game_framework.change_state(result_state)

    if len(monsters) == 0:
        game_framework.change_state(Clear_state)


def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()


def pause(): pass


def resume(): pass
