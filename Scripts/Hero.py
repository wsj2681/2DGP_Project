from pico2d import *

# Hero Event
SPACE_DOWN, SPASE_UP = range(2)

key_event_table = {
    (SDL_KEYDOWN, SDLK_SPACE): SPACE_DOWN,
    (SDL_KEYUP, SDLK_SPACE): SPASE_UP
}


# Hero States
class IdleState:
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


next_state_table = {
    IdleState: {},
    SmashState: {}
}


class Hero:
    def __init__(self):
        # image Size 100, 100
        self.image = load_image('Images/45.png')
        self.dir = 1
        self.velocity = 0
        self.frame = 0
        self.timer = 0
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
            self.cur_state.exit(self.event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self.event)

    def draw(self):
        self.cur_state.draw(self.x, self.y)

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)
