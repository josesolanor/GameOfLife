import unittest
from GameOfLife import Cell, CellState

cell_state = CellState()
cell = Cell()

class Test_CellState(unittest.TestCase):
    def test_should_initialize_with_cell_state(self):
        cell.state = cell_state.ALIVE
        self.assertEqual(cell.state, cell_state.ALIVE)

