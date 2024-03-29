from pico2d import *

import game_framework
import game_world
import state_title


name = "PauseState"
image = None


def enter():
    global image
    image = load_image('Images/pause.png')


def exit():
    global image
    del image


def update():
    pass


def draw():
    image.draw(400, 300)
    update_canvas()


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_KEYDOWN and event.key == SDLK_r:
            game_framework.pop_state()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_world.clear()
            game_framework.change_state(state_title)


def pause(): pass
def resume(): pass
