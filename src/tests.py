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
    
    def test_entry_exit_removal(self):
        num_rows = 10
        num_cols = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(m1._cells[0][0].has_top_wall, True)
        self.assertEqual(m1._cells[num_rows-1][num_cols-1].has_bottom_wall, True)
        m1._break_entrance_and_exit()
        self.assertEqual(m1._cells[0][0].has_top_wall, False)
        self.assertEqual(m1._cells[num_rows-1][num_cols-1].has_bottom_wall, False)

    
    def test_visited_state_after_maze_is_constructed(self):
        num_rows = 10
        num_cols = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(m1._cells[0][1].visited, False)
        m1._break_walls_r(0,1)
        self.assertEqual(m1._cells[0][1].visited, True)
        m1._reset_cells_visited()
        self.assertEqual(m1._cells[0][1].visited, False)
        


if __name__ == "__main__":
    unittest.main()