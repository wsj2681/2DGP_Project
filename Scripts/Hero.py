from pico2d import *


# init smash line
smash_line = []
smash_line_cnt = 0


def line():
    global smash_line
    p1 = (100, 600)
    p2 = (200, 25)

    x1, y1 = p1[0], p1[1]
    x2, y2 = p2[0], p2[1]
    a = (y2-y1) / (x2 - x1)
    b = y1 - x1 * a
    for x in range(x1, x2+1, 1):
        y = a * x + b
        smash_line.append((x, y))


# Hero Event
SPACE_DOWN, SPACE_UP = range(2)

key_event_table = {
    (SDL_KEYDOWN, SDLK_SPACE): SPACE_DOWN,
    (SDL_KEYUP, SDLK_SPACE): SPACE_UP
}


# Hero States
class IdleState:
    @staticmethod
    def enter(hero, event):
        hero.x, hero.y = 100, 550
        hero.timer = 10
        hero.frame = 0

    @staticmethod
    def exit(hero, event):
        pass

    @staticmethod
    def do(hero):
        hero.frame = (hero.frame + 1) % 1
        hero.timer -= 1

        if hero.timer is 0:
            hero.flag *= -1
            hero.timer = 10

        if hero.flag is -1:
            hero.y -= 1
        elif hero.flag is 1:
            hero.y += 1

    @staticmethod
    def draw(hero):
        hero.image.draw(hero.x, hero.y)


class SmashState:
    @staticmethod
    def enter(hero, event):
        hero.frame = 0
        hero.timer = 100

    @staticmethod
    def exit(hero, event):
        pass

    @staticmethod
    def do(hero):
        hero.frame = (hero.frame + 1) % 1
        hero.timer -= 1
        hero.y -= 1
        hero.x += 0.1739

    @staticmethod
    def draw(hero):
        global smash_line, smash_line_cnt
        smash_line_cnt += 1
        hero.x = smash_line[smash_line_cnt][0]
        hero.y = smash_line[smash_line_cnt][1]
        hero.image.draw(hero.x, hero.y)


next_state_table = {
    IdleState: {SPACE_DOWN: SmashState, SPACE_UP: IdleState},
    SmashState: {SPACE_DOWN: SmashState, SPACE_UP: IdleState}
}


class Hero:
    def __init__(self):
        # image Size 100, 100
        self.image = load_image('Images/45.png')
        self.x, self.y = 100, 600
        self.dir = 1
        self.velocity = 0
        self.frame = 0
        self.timer = 0
        self.flag = 1
        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)

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

    def handle_events(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)
