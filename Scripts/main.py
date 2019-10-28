from Scripts import game_framework, start_state
import pico2d

pico2d.open_canvas(800, 600)
game_framework.run(start_state)
pico2d.close_canvas()