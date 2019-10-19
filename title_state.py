import game_framework
from pico2d import *
import main_state

name = "TitleState"
image = None

def enter():
    global image
    image = load_image('title.png')