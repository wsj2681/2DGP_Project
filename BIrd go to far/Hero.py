from pico2d import *

# Hero Event
SPACE_DOWN, SPACE_UP = range(2)

key_event_table = {
    (SDL_KEYDOWN, SDLK_SPACE): SPACE_DOWN,
    (SDL_KEYUP, SDLK_SPACE): SPACE_UP,
}


# Boy States
class IdleState:
    @staticmethod
    def enter(hero, event):
        hero.frame = 0
        hero.x, hero.y

    @staticmethod
    def exit(hero, event):
        pass

    @staticmethod
    def do(hero):
        pass

    @staticmethod
    def draw(hero):
        pass


class SmashState:
    @staticmethod
    def enter(hero, event):
        pass

    @staticmethod
    def exit(hero, event):
        pass

    @staticmethod
    def do(hero):
        pass

    @staticmethod
    def draw(hero):
        pass


class ComebackState:
    @staticmethod
    def enter(hero, event):
        pass

    @staticmethod
    def exit(hero, event):
        pass

    @staticmethod
    def do(hero):
        pass

    @staticmethod
    def draw(hero):
        pass


next_state_table = {
    IdleState: {},
    SmashState: {},
    ComebackState: {}
}


class Hero:

    def __init__(self):
        self.x, self.y = 100, 550
        self.image = load_image('animation_sheet.png')
        self.dir = 1
        self.velocity = 0
        self.frame = 0
        self.timer = 0
        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)

    def change_state(self,  state):
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

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)