class CellState():
    ALIVE = 1
    DEAD = 0

class Cell():
    state = None

    def __init___(self, state):
        self.state = state

    def next_generation_state(self, neighbors):
        self.state = CellState.DEAD

