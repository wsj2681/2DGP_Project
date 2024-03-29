from pico2d import *
import game_world
import game_framework
from Object_Fireball import Fireball
import state_main

# Hero Move Speed
PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
MOVE_SPEED_KMPH = 30.0  # Km / Hour
MOVE_SPEED_MPM = (MOVE_SPEED_KMPH * 1000.0 / 60.0)
MOVE_SPEED_MPS = (MOVE_SPEED_MPM / 60.0)
MOVE_SPEED_PPS = (MOVE_SPEED_MPS * PIXEL_PER_METER)

# Hero Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 6

# Hero Event
# 상하좌우 이동가능
RIGHT_DOWN, RIGHT_UP, LEFT_DOWN, LEFT_UP, UP_DOWN, UP_UP, DOWN_DOWN, DOWN_UP, SPACE = range(9)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP,
    (SDL_KEYDOWN, SDLK_UP): UP_DOWN,
    (SDL_KEYUP, SDLK_UP): UP_UP,
    (SDL_KEYDOWN, SDLK_DOWN): DOWN_DOWN,
    (SDL_KEYUP, SDLK_DOWN): DOWN_UP,

    (SDL_KEYDOWN, SDLK_SPACE): SPACE,
}


# Boy States
class IdleState:
    @staticmethod
    def enter(hero, event):
        if event == RIGHT_DOWN:
            hero.velocity_x += MOVE_SPEED_PPS
        elif event == RIGHT_UP:
            hero.velocity_x -= MOVE_SPEED_PPS
        if event == LEFT_DOWN:
            hero.velocity_x -= MOVE_SPEED_PPS
        elif event == LEFT_UP:
            hero.velocity_x += MOVE_SPEED_PPS

        if event == UP_DOWN:
            hero.velocity_y += MOVE_SPEED_PPS
        elif event == UP_UP:
            hero.velocity_y -= MOVE_SPEED_PPS
        if event == DOWN_DOWN:
            hero.velocity_y -= MOVE_SPEED_PPS
        elif event == DOWN_UP:
            hero.velocity_y += MOVE_SPEED_PPS
        hero.timer = 10

    @staticmethod
    def exit(hero, event):
        if event == SPACE:
            fireball = Fireball(hero.x, hero.y, 300)
            game_world.add_object(fireball, 1)
            state_main.balls.append(fireball)
            hero.fireball()

    @staticmethod
    def do(hero):
        hero.timer -= 1
        hero.frame = (hero.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 5
        if hero.timer == 0:
            hero.sleep *= -1
            hero.timer = 10

        if hero.sleep is -1:
            hero.y -= 1
        elif hero.sleep is 1:
            hero.y += 1

        hero.x += hero.velocity_x * game_framework.frame_time
        hero.x = clamp(25, hero.x, 800 - 25)
        hero.y += hero.velocity_y * game_framework.frame_time
        hero.y = clamp(150, hero.y, 600 - 25)

    @staticmethod
    def draw(hero):
        if hero.velocity_x > 0:
            hero.image_right.clip_draw(int(hero.frame) * 35, 0, 35, 50, hero.x, hero.y)
            hero.dir = 1
        elif hero.velocity_x < 0:
            hero.image_left.clip_draw(int(hero.frame) * 35, 0, 35, 50, hero.x, hero.y)
            hero.dir = -1
        else:
            if hero.dir == 1:
                hero.image_right.clip_draw(int(hero.frame) * 35, 0, 35, 50, hero.x, hero.y)
            elif hero.dir == -1:
                hero.image_left.clip_draw(int(hero.frame) * 35, 0, 35, 50, hero.x, hero.y)


class MoveState:
    @staticmethod
    def enter(hero, event):
        if event == RIGHT_DOWN:
            hero.velocity_x += MOVE_SPEED_PPS
        elif event == RIGHT_UP:
            hero.velocity_x -= MOVE_SPEED_PPS
        if event == LEFT_DOWN:
            hero.velocity_x -= MOVE_SPEED_PPS
        elif event == LEFT_UP:
            hero.velocity_x += MOVE_SPEED_PPS

        if event == UP_DOWN:
            hero.velocity_y += MOVE_SPEED_PPS
        elif event == UP_UP:
            hero.velocity_y -= MOVE_SPEED_PPS
        if event == DOWN_DOWN:
            hero.velocity_y -= MOVE_SPEED_PPS
        elif event == DOWN_UP:
            hero.velocity_y += MOVE_SPEED_PPS

    @staticmethod
    def exit(hero, event):
        if event == SPACE:
            fireball = Fireball(hero.x, hero.y, 300)
            game_world.add_object(fireball, 1)
            state_main.balls.append(fireball)
            hero.fireball()

    @staticmethod
    def do(hero):
        hero.x += hero.velocity_x * game_framework.frame_time
        hero.x = clamp(25, hero.x, 800 - 25)
        hero.y += hero.velocity_y * game_framework.frame_time
        hero.y = clamp(150, hero.y, 600 - 25)

        hero.frame = (hero.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 5

    @staticmethod
    def draw(hero):
        if hero.velocity_x > 0:
            hero.image_right.clip_draw(int(hero.frame) * 35, 0, 35, 50, hero.x, hero.y)
            hero.dir = 1
        elif hero.velocity_x < 0:
            hero.image_left.clip_draw(int(hero.frame) * 35, 0, 35, 50, hero.x, hero.y)
            hero.dir = -1
        else:
            if hero.velocity_y > 0 or hero.velocity_y < 0:
                if hero.dir == 1:
                    hero.image_right.clip_draw(int(hero.frame) * 35, 0, 35, 50, hero.x, hero.y)
                else:
                    hero.image_left.clip_draw(int(hero.frame) * 35, 0, 35, 50, hero.x, hero.y)



next_state_table = {
    IdleState: {RIGHT_DOWN: MoveState, RIGHT_UP: IdleState,
                LEFT_DOWN: MoveState, LEFT_UP: IdleState,
                UP_DOWN: MoveState, UP_UP: IdleState,
                DOWN_DOWN: MoveState, DOWN_UP: IdleState,
                SPACE: IdleState},

    MoveState: {RIGHT_DOWN: MoveState, RIGHT_UP: IdleState,
                LEFT_DOWN: MoveState, LEFT_UP: IdleState,
                UP_DOWN: MoveState, UP_UP: IdleState,
                DOWN_DOWN: MoveState, DOWN_UP: IdleState,
                SPACE: MoveState},
}


class Hero:

    def __init__(self):
        self.x, self.y = 400, 300
        self.image_right = load_image('Images/Hero_right.png')
        self.image_left = load_image('Images/Hero_left.png')
        self.life = 3
        self.velocity_x = 0
        self.velocity_y = 0
        self.sleep = 1
        self.dir = 1
        self.frame = 0
        self.timer = 0
        self.egg_cool_time = 0
        self.score = 0
        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)

        # Sound
        self.fireball_sound = load_wav('Sound/Fireball.wav')
        self.fireball_sound.set_volume(32)
        self.pickup_sound = load_wav('Sound/Heart_Up.wav')
        self.pickup_sound.set_volume(32)
        self.collide_obstacle_sound = load_wav('Sound/Hit.wav')
        self.collide_obstacle_sound.set_volume(32)
        self.death_sound = load_wav('Sound/Die.wav')
        self.death_sound.set_volume(32)

    def get_bb(self):
        return self.x - 13, self.y - 23, self.x + 10, self.y + 8

    def fireball(self):
        self.fireball_sound.play()

    def pick_heart(self):
        self.pickup_sound.play()

    def collide_obstacle(self):
        self.collide_obstacle_sound.play()

    def die(self):
        self.death_sound.play()

    def change_state(self, state):
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)

    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)
        # draw_rectangle(*self.get_bb())

    def handle_events(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)
