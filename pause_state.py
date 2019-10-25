import game_framework
from pico2d import *
import title_state

name = "PauseState"
image = None
flag = 1


def enter():
    global image
    image = load_image('pause.png')


def exit():
    global image
    del(image)


def update():
    pass


def draw():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_KEYDOWN and event.key == SDLK_r:
            game_framework.pop_state()
            print("game resume")
        if event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state)
            print("game restart")


def pause(): pass
def resume(): pass
