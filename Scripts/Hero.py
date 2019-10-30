from pico2d import *

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
        hero.frame = 0
        hero.x, hero.y = 100, 550
        hero.timer = 10

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
        if event == SPACE_DOWN:
            hero.velocity += 1
        elif event == SPACE_UP:
            hero.velocity -= 1
        hero.timer = 100

    @staticmethod
    def exit(hero, event):
        pass

    @staticmethod
    def do(hero):
        hero.frame = (hero.frame + 1) % 1
        hero.timer -= 1
        hero.y -= hero.velocity
        hero.x += 0.1739
        if hero.y - 50 < 25 and hero.x > 200:
            hero.y = 600
            hero.x = 100

    @staticmethod
    def draw(hero):
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
            self.cur_state.exit(self.event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self.event)

    def draw(self):
        self.cur_state.draw(self)

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)
