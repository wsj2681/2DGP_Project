from pico2d import *

import game_framework
import title_state

name = "PauseState"
image = None
flag = 1


def enter():
    global image
    image = load_image('Images/pause_sel.png')


def exit():
    global image
    del image


def update():
    pass


def draw():
    clear_canvas()
    image.draw(400, 300, 900, 900)
    update_canvas()


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_KEYDOWN and event.key == SDLK_r:
            game_framework.pop_state()
            print("game resume")
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state)
            print("game restart")


def pause(): pass
def resume(): pass
