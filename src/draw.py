import time, random


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def draw(self, canvas, fill_color):
        # fill color is a string like "red" or "black"
        canvas.create_line(
            self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_color, width=2
        )


class Cell:
    def __init__(self, x1, x2, y1, y2, win=None):
        self.visited = False
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        self._win = win

    def draw(self):
        if self._win is None:
            return
        # walls = [self.has_top_wall , self.has_right_wall, self.has_bottom_wall, self.has_left_wall]

        left_wall = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
        color = "black" if self.has_left_wall else "#d9d9d9"
        self._win.draw_line(left_wall, color)

        right_wall = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
        color = "black" if self.has_right_wall else "#d9d9d9"
        self._win.draw_line(right_wall, color)

        top_wall = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
        color = "black" if self.has_top_wall else "#d9d9d9"
        self._win.draw_line(top_wall, color)

        bottom_wall = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
        color = "black" if self.has_bottom_wall else "#d9d9d9"
        self._win.draw_line(bottom_wall, color)

    def draw_move(self, to_cell, undo=False):
        self_center = Point((self._x1 + self._x2) / 2, (self._y1 + self._y2) / 2)
        to_cell_center = Point(
            (to_cell._x1 + to_cell._x2) / 2, (to_cell._y1 + to_cell._y2) / 2
        )
        line = Line(self_center, to_cell_center)
        if not undo:
            self._win.draw_line(line, "red")
        else:
            self._win.draw_line(line, "gray")


class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._create_cells()
        
        # do check this thoroughly 
        if seed is not None:
            random.seed(seed)

    def _create_cells(self):
        self._cells = []
        for i in range(self._num_rows):
            row_cells = []
            for j in range(self._num_cols):
                x1 = self._x1 + (j * self._cell_size_x)  # j affects x (columns)
                y1 = self._y1 + (i * self._cell_size_y)  # i affects y (rows)
                x2 = x1 + self._cell_size_x
                y2 = y1 + self._cell_size_y

                cell = Cell(x1, x2, y1, y2, self._win)
                row_cells.append(cell)

                if self._win is not None:
                    cell.draw()
                    self._animate()

            self._cells.append(row_cells)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        if self._win is not None:
            self._draw_cell(0, 0)
        self._cells[self._num_rows - 1][self._num_cols - 1].has_bottom_wall = False
        if self._win is not None:
            self._draw_cell(self._num_rows - 1, self._num_cols - 1)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            adjacent_positions = [
                (i-1, j),  # North (up)
                (i, j+1),  # East (right)
                (i+1, j),  # South (down)
                (i, j-1)   # West (left)
            ]
            to_visit = []
            for ni, nj in adjacent_positions:
                if  0 <= ni < self._num_rows and 0 <= nj <self._num_cols and not self._cells[ni][nj].visited:
                    to_visit.append((ni, nj))
            if len(to_visit) == 0:
                self._cells[i][j].draw()
                return
            else:
                break_wall = random.choice(to_visit)
                ni, nj = break_wall
                # North
                if ni == i-1 and nj == j:
                    self._cells[i][j].has_top_wall = False
                    self._cells[ni][nj].has_bottom_wall = False
                # East
                elif ni == i and nj == j+1:
                    self._cells[i][j].has_right_wall = False
                    self._cells[ni][nj].has_left_wall = False
                # South
                elif ni == i+1 and nj == j:
                    self._cells[i][j].has_bottom_wall = False
                    self._cells[ni][nj].has_top_wall = False
                # West
                elif ni == i and nj == j-1:
                    self._cells[i][j].has_left_wall = False
                    self._cells[ni][nj].has_right_wall = False
                self._break_walls_r(break_wall[0], break_wall[1])
                
                
    def _reset_cells_visited(self):
        for i in range(self._num_rows):
            for j in range(self._num_cols):
                self._cells[i][j].visited = False
            

    def _draw_cell(self, i, j):
        if self._win is not None:
            self._cells[i][j].draw()
            self._animate()

    def _animate(self):
        if self._win is not None:
            self._win.redraw()
            time.sleep(0.05)
