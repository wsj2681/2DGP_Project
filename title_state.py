import game_framework
from pico2d import *
import main_state

name = "TitleState"
image = None


def enter():
    global image
    image = load_image('title.png')
    print("load title image")


def exit():
    global image
    del(image)
    print("delete title image")


def handle_events():
    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
            print("cancel canvas")
        else:
            if(event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
                print("cancel canvas")
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                game_framework.change_state(main_state)
                print("go main_state")


def draw():
    clear_canvas()
    image.draw(400, 300)
    update_canvas()


def update(): pass
def pause(): pass
def resume(): pass
