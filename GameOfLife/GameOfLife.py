class CellState():
    ALIVE = 1
    DEAD = 0

class Cell():
    state = None

    def __init___(self, state):
        self.state = state

    def next_generation_state(self, neighbors):
        if neighbors == 2:
            self.state = CellState.ALIVE
        else:
            self.state = CellState.DEAD

