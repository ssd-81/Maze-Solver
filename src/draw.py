
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
    def __init__(self):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None # I don't know 
        self._x2 = None 
        

