from pico2d import *
import curve_movement
import game_world

smash_line = []


def fill_smash_location(hero):
    global smash_line
    smash_line = []
    points = [(hero.x, hero.y), (200, 300), (200, 50), (100, 300)]
    for i in range(0, 100, 2):
        t = i / 100
        res = curve_movement.mathematics_type_b(t, points[3], points[0], points[1], points[2])
        smash_line.append(res)
    for i in range(0, 100, 2):
        t = i / 100
        res = curve_movement.mathematics_type_b(t, points[0], points[1], points[2], points[3])
        smash_line.append(res)
    for i in range(0, 100, 2):
        t = i / 100
        res = curve_movement.mathematics_type_b(t, points[1], points[2], points[3], points[0])
        smash_line.append(res)
    for i in range(0, 100, 2):
        t = i / 100
        res = curve_movement.mathematics_type_b(t, points[2], points[3], points[0], points[1])
        smash_line.append(res)


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
        hero.x, hero.y = 100, 550
        hero.timer = 10

    @staticmethod
    def exit(hero, event):
        pass

    @staticmethod
    def do(hero):
        hero.timer -= 1

        if hero.timer == 0:
            hero.dir *= -1
            hero.timer = 10

        if hero.dir is -1:
            hero.y -= 1
        elif hero.dir is 1:
            hero.y += 1

    @staticmethod
    def draw(hero):
        hero.image.draw(hero.x, hero.y)


class SmashState:
    @staticmethod
    def enter(hero, event):
        global smash_line
        hero.timer = 200
        fill_smash_location(hero)
        print(len(smash_line))

    @staticmethod
    def exit(hero, event):
        pass

    @staticmethod
    def do(hero):
        hero.timer -= 1
        if hero.timer == 0:
            hero.timer = 200
        hero.x = smash_line[200 - hero.timer][0]
        hero.y = smash_line[200 - hero.timer][1]
        if hero.x == smash_line[199][0]:
            hero.add_event(SPACE_UP)

    @staticmethod
    def draw(hero):
        hero.image.draw(hero.x, hero.y)


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
    IdleState: {SPACE_DOWN: SmashState, SPACE_UP: SmashState},
    SmashState: {SPACE_DOWN: IdleState, SPACE_UP: IdleState},
    ComebackState: {}
}


class Hero:

    def __init__(self):
        self.x, self.y = 100, 550
        self.image = load_image('Images/45.png')
        self.life = 3
        self.dir = 1
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

    def handle_events(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)
