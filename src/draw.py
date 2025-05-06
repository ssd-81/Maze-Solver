
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
        canvas.create_line(self.p1.x, self.p1.y, self.p2.x, self.p2.y,
        fill=fill_color, width=2)

class Cell:
    def __init__(self, x1, x2, y1, y2, win):
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
        if self.has_left_wall:
            left_wall = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
            self._win.draw_line(left_wall, "black")
        if self.has_right_wall:
            right_wall = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
            self._win.draw_line(right_wall, "black")
        if self.has_top_wall:
            top_wall = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
            self._win.draw_line(top_wall, "black")
        if self.has_bottom_wall:
            bottom_wall = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
            self._win.draw_line(bottom_wall, "black")
    
    def draw_move(self, to_cell, undo=False):
        self_center = Point((self._x1 + self._x2)/2, (self._y1 + self._y2)/2)
        to_cell_center = Point((to_cell._x1 + to_cell._x2)/2, (to_cell._y1 + to_cell._y2)/2)
        line = Line(self_center, to_cell_center)
        if not undo:
            self._win.draw_line(line, "red")
        else:
            self._win.draw_line(line, "gray")

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows 
        self._num_cols = num_cols 
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
    
    def _create_cells(self):
        for rows in self._num_rows:
            for cell in self._num_cols:
                cell = Cell()