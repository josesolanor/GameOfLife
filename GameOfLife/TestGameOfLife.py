import unittest
from GameOfLife import Cell, CellState

cell_state = CellState()
cell = Cell()

# La celula deberia poder iniciarse con un estado: Vivo o Muerto
class Test_InitializeCellState(unittest.TestCase):
    def test_cell_should_initialize_alive(self):
        cell.state = cell_state.ALIVE
        self.assertEqual(cell.state, cell_state.ALIVE)

    def test_cell_should_initialize_dead(self):
        cell.state = cell_state.DEAD
        self.assertEqual(cell.state, cell_state.DEAD)