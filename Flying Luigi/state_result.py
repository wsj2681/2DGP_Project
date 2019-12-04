from pico2d import *

import game_framework
import state_title
import state_main

name = "ResultState"

image = None
font = None


def enter():
    global image, font
    image = load_image('Images/result.png')
    font = load_font('ENCR10B.TTF', 16)


def exit():
    global image
    del image


def update():
    pass


def draw():
    global image, font
    clear_canvas()
    image.draw(400, 300)
    font.draw(350, 250, 'Score: %3.f' % state_main.get_score(), (255, 0, 0))
    update_canvas()


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_KEYDOWN and event.key == SDLK_r:
            game_framework.change_state(state_title)
        if event.type == SDL_KEYDOWN and event.key == SDLK_q:
            game_framework.quit()


def pause(): pass
def resume(): pass