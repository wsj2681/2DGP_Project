from pico2d import *

import game_framework
import state_main
import game_world
name = "TitleState"
image = None
font = None

def enter():
    global image,font
    image = load_image('Images/title.png')

    font = load_font('DungGeunMo.TTF', 64)


def exit():
    global image
    del image


def handle_events():
    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if(event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                game_framework.change_state(state_main)
                print("go main_state")


def draw():
    clear_canvas()
    image.draw(400, 300)
    font.draw(220, 50, 'Flying Luigi', (0, 0, 0))
    update_canvas()


def update(): pass
def pause(): pass
def resume(): pass
