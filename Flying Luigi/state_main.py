from pico2d import *
import game_framework
import game_world
import state_pause
import state_result
import state_clear
import state_ranking
import Obejct_Hero
import Map
import Ground
from Map import Cloud
# from Map import Cloud2
from Ground import Mountain
from Object_Monster import Monster_right
from Object_Monster import Monster_left
from Object_Obstacle import Obstacle_right
from Object_Obstacle import Obstacle_left
from UI_Hp import Hp
from UI_Score import Score
from Object_Item import Item

name = "MainState"

background = None
ground = None
mountain = None
cloudes = []
cloudes2 = []
hero = None
itemes = []

ui_hp = None
ui_score = 0.0

balls = []
monsters = []
monsters_right = []
monsters_left = []
obstacles = []
obstacles_right = []
obstacles_left = []


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
    global background
    background = Map.Map()
    game_world.add_object(background, 0)

    global mountain
    mountain = Mountain()
    game_world.add_object(mountain, 0)

    global ground
    ground = Ground.Ground()
    game_world.add_object(ground, 0)

    global cloudes, cloudes2
    cloudes = [Cloud() for i in range(5)]
    game_world.add_objects(cloudes, 0)

    global hero
    hero = Obejct_Hero.Hero()
    game_world.add_object(hero, 1)

    global monsters, monsters_right, monsters_left
    monsters_right = [Monster_right() for i in range(25)]
    monsters_left = [Monster_left() for i in range(25)]
    monsters = monsters_right + monsters_left
    game_world.add_objects(monsters, 1)

    global obstacles, obstacles_right, obstacles_left
    obstacles_right = [Obstacle_right() for i in range(25)]
    obstacles_left = [Obstacle_left() for i in range(25)]
    obstacles = obstacles_right + obstacles_left
    game_world.add_objects(obstacles, 1)

    global itemes
    itemes = [Item() for i in range(5)]
    game_world.add_objects(itemes, 1)

    global ui_score
    ui_score = Score()
    game_world.add_object(ui_score, 2)

    global ui_hp
    ui_hp = Hp()
    game_world.add_object(ui_hp, 2)


def get_score():
    return ui_score.score



def exit():
    game_world.clear()


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        if event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.push_state(state_pause)
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
            hero.collide_obstacle()
            ui_hp.life -= 1

    for item in itemes:
        if collide(item, hero):
            item.x, item.y = 0, 0
            itemes.remove(item)
            item.remove()
            hero.pick_heart()
            ui_hp.life += 1

    if ui_hp.life < 0:
        ground.bgm.set_volume(0)
        hero.die()
        delay(3.0)
        state_ranking.curr_data = ui_score.score
        game_framework.change_state(state_result)

    if len(monsters) == 0:
        game_framework.change_state(state_clear)


def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()


def pause():
    ground.bgm.set_volume(0)


def resume():
    ground.bgm.set_volume(64)
