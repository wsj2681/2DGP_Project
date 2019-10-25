import game_framework
from pico2d import *
import title_state


name = "ResultState"
image = None


def enter():
    pass


def exit():
    pass


def update():
    pass


def draw():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_KEYDOWN and event.key == SDLK_r:
            game_framework.change_state(title_state)
            print("game restart")
        if event.type == SDL_KEYDOWN and event.key == SDLK_q:
            game_framework.quit()
            print("game over")


def pause(): pass
def resume(): pass
