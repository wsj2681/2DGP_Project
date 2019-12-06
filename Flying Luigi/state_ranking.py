import random
import json
import pickle
import os

from pico2d import *
import game_framework
import game_world
import state_title
# import world_build_state


name = "RankingState"

curr_data = 0
ranking = []
font = None


def enter():
    global ranking, font, curr_data

    with open('ranking_data.json', 'r') as f:
        ranking = json.load(f)

    ranking.append(curr_data)
    ranking.sort(reverse=True)

    hide_cursor()
    hide_lattice()
    font = load_font('DungGeunMo.ttf', 20)

    with open('ranking_data.json', 'w') as f:
        json.dump(ranking, f)


def exit():
    pass


def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_world.save()
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_world.save()
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_r:
            game_framework.change_state(state_title)


def update():
    pass


def draw():
    clear_canvas()
    font.draw(300, 500, "[Ranking Chart]", (255, 0, 0))

    for i in range(min(10, len(ranking))):
        font.draw(350, 450 - i * 20, "#" + str(i + 1), (0, 0, 255))
        font.draw(390, 450 - i * 20, "%1d" % int(ranking[i]), (255, 255, 0))

    update_canvas()
