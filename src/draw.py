import time


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
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._create_cells()

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

    def _draw_cell(self, i, j):
        if self._win is not None:
            self._cells[i][j].draw()
            self._animate()

    def _animate(self):
        if self._win is not None:
            self._win.redraw()
            time.sleep(0.05)
