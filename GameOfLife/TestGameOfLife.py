import unittest
from GameOfLife import Cell, CellState

cell_state = CellState()
cell = Cell()
neighbors = None

# La celula deberia poder iniciarse con un estado: Vivo o Muerto
class Test_InitializeCellState(unittest.TestCase):
    def test_cell_should_initialize_alive(self):
        cell.state = cell_state.ALIVE
        self.assertEqual(cell.state, cell_state.ALIVE)

    def test_cell_should_initialize_dead(self):
        cell.state = cell_state.DEAD
        self.assertEqual(cell.state, cell_state.DEAD)

# Reglas del juego a seguir:

# Cualquier célula viva con menos de dos vecinos vivos muere.
class Test_CellShouldDieLessTwoNeighbors(unittest.TestCase):
    def test_cell_should_die_with_zero_neighbors(self):
        neighbors = 0
        cell.state = cell_state.ALIVE
        cell.next_generation_state(neighbors)
        self.assertEqual(cell.state, cell_state.DEAD)

    def test_cell_should_die_with_one_neighbor(self):
        neighbors = 1
        cell.state = cell_state.ALIVE
        cell.next_generation_state(neighbors)
        self.assertEqual(cell.state, cell_state.DEAD)

# Cualquier célula viva con dos o tres vecinos vivos sigue viviendo para la siguiente generación.
class Test_CellShouldAliveTwoOrThreeNeighbors(unittest.TestCase):
    def test_cell_should_alive_with_two_neighbors(self):
        neighbors = 2
        cell.state = cell_state.ALIVE
        cell.next_generation_state(neighbors)
        self.assertEqual(cell.state, cell_state.ALIVE)

    def test_cell_should_alive_with_three_neighbors(self):
        neighbors = 3
        cell.state = cell_state.ALIVE
        cell.next_generation_state(neighbors)
        self.assertEqual(cell.state, cell_state.ALIVE)


# Cualquier célula viva con más de tres vecinos vivos muere (cantidad maxima 8 vecinos en una grilla).
class Test_CellShouldDieWithMoreThanThreeNeighbors(unittest.TestCase):
    def test_cell_should_die_with_more_than_three_neighbors(self):
        neighbors = [4,5,6,7,8]
        cell.state = cell_state.ALIVE
        for neighbor in neighbors:
            cell.next_generation_state(neighbor)
            self.assertEqual(cell.state, cell_state.DEAD)

# Cualquier célula muerta con exactamente tres vecinos vivos se convierte en una célula viva.
class Test_CellShouldAliveWithExactlyThreeNeighbors(unittest.TestCase):
    def test_cell_should_alive_with_exactly_three_neighbors(self):
        neighbors = 3
        cell.state = cell_state.DEAD
        cell.next_generation_state(neighbors)
        self.assertEqual(cell.state, cell_state.ALIVE)

if __name__ == '__main__':
    unittest.main()