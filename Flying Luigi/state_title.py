from pico2d import *

import game_framework
import state_main
import game_world
name = "TitleState"
image = None
font_64 = None
font_32 = None


def enter():
    global image, font_64, font_32
    image = load_image('Images/title.png')

    font_64 = load_font('DungGeunMo.TTF', 64)
    font_32 = load_font('DungGeunMo.TTF', 32)


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
    font_64.draw(220, 300, 'FLYING LUIGI', (0, 0, 255))
    font_32.draw(240, 50, 'Press Space to Start', (255, 0, 0))
    update_canvas()


def update(): pass
def pause(): pass
def resume(): pass
