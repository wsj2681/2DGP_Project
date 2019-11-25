from pico2d import *

import game_framework
import start_state
import UI_Score

name = "ClearState"
image = None


def enter():
    global image
    image = load_image('Images/clear.png')


def exit():
    global image
    del image


def update():
    pass


def draw():
    global image
    clear_canvas()
    image.draw(400, 300)
    update_canvas()


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_KEYDOWN:
            game_framework.change_state(start_state)


def pause(): pass
def resume(): pass
