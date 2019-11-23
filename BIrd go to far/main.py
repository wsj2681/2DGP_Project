import pico2d

import game_framework
import start_state

pico2d.open_canvas(800, 600, sync=True)
game_framework.run(start_state)
pico2d.close_canvas()
