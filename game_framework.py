class GameState:
    def __init__(self, state):
        self.enter = state.enter
        self.exit = state.exit
        self.pause = state.pause
        self.resume = state.resume
        self.handle_events = state.handel_events
        self.update = state.update
        self.draw = state.draw
        self.collusion = state.collusion

    def enter(self):
        pass
    def exit(self):
        pass
    def pause(self):
        pass
    def resume(self):
        pass
    def handle_events(self):
        pass
    def update(self):
        pass
    def draw(self):
        pass
    def collusion(self):
        pass
