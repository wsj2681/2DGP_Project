from Scripts import game_framework, title_state
from pico2d import *


name = "ResultState"
image = None


def enter():
    global image

    image = load_image('Images/gameover.png')


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
        if event.type == SDL_KEYDOWN and event.key == SDLK_r:
            game_framework.change_state(title_state)
            print("game restart")
        if event.type == SDL_KEYDOWN and event.key == SDLK_q:
            game_framework.quit()
            print("game over")


def pause(): pass
def resume(): pass
