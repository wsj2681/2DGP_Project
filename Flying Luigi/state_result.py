from pico2d import *

import game_framework
import state_title
import state_main
import state_ranking
name = "ResultState"

image = None
font = None
font_24 = None

def enter():
    global image, font, font_24
    image = load_image('Images/result.png')
    font = load_font('DungGeunMo.TTF', 32)
    font_24 = load_font('DungGeunMo.TTF', 24)

def exit():
    global image
    del image


def update():
    pass


def draw():
    global image, font
    clear_canvas()
    image.draw(400, 300)
    font.draw(300, 350, 'Game Over', (255, 0, 0))
    font.draw(300, 300, 'Score: %1.f' % state_main.get_score(), (0, 0, 255))
    font_24.draw(200, 200, 'Restart(R)', (0, 0, 0))
    font_24.draw(400, 200, 'Quit(ESC)', (0, 0, 0))
    font_24.draw(300, 150, 'View Ranking(V)', (0, 255, 0))
    update_canvas()


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_KEYDOWN and event.key == SDLK_r:
            game_framework.change_state(state_title)
        if event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        if event.type == SDL_KEYDOWN and event.key == SDLK_v:
            game_framework.change_state(state_ranking)


def pause(): pass
def resume(): pass
