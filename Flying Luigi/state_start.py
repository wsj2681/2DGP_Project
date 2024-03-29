from pico2d import *
import game_framework
import state_title

name = "StartState"
image = None
logo_time = 0.0


def enter():
    global image
    image = load_image('Images/kpu_credit.png')


def exit():
    global image
    del image


def update():
    global logo_time

    if logo_time > 1.0:
        logo_time = 0
        game_framework.change_state(state_title)
        print("go title state")
    delay(0.01)
    logo_time += 0.01


def draw():
    global image

    clear_canvas()
    image.draw(400, 300)
    update_canvas()


def handle_events():
    events = get_events()
    pass


def pause(): pass
def resume(): pass
