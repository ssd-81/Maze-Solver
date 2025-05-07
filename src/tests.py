import unittest

from draw import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 10
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )
    
    def test_maze_create_single_row(self):
        num_cols = 10
        num_rows = 1
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_rows
        )
    

    def test_maze_create_single_column(self):
        num_cols = 1
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            num_cols,
            len(m1._cells[0])
        )
    
    def test_single_cell_maze(self):
        num_cols = 1
        num_rows = 1
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(num_cols,
                        len(m1._cells[0])
        )
        self.assertEqual(num_rows,
                        len(m1._cells)
        )
    
    def test_cell_size_in_maze(self):
        x_size = 10
        y_size = 10
        m1 = Maze(0, 0, 20, 20, x_size, y_size)
        self.assertEqual(m1._cells[0][0]._x2 - m1._cells[0][0]._x1, x_size)
        self.assertEqual(m1._cells[1][1]._y2 - m1._cells[1][1]._y1, y_size)
        

    


if __name__ == "__main__":
    unittest.main()