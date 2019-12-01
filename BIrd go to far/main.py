import pico2d

import game_framework
import state_start

pico2d.open_canvas(800, 600, sync=True)
game_framework.run(state_start)
pico2d.close_canvas()
