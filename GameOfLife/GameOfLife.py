class CellState():
    ALIVE = 1
    DEAD = 0

class Cell():
    state = None

    def __init___(self, state):
        self.state = state

    def next_generation_state(self, neighbors):

        if self.state == CellState.ALIVE:
            if neighbors == 2 or neighbors == 3:
                self.state = CellState.ALIVE
            else:
                self.state = CellState.DEAD

        elif self.state == CellState.DEAD:
            if neighbors == 3:
                self.state = CellState.ALIVE


