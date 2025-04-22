from tkinter import Tk, BOTH, Canvas
from draw import Point, Line


class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.__root = Tk()
        self.__root.title("visualize-maze")
        self.canvas = Canvas(self.__root, height=self.height, width=self.width)
        self.canvas.pack(fill=BOTH, expand=1)
        self.window_running = True
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.window_running = True
        while self.window_running:
            self.redraw()

    def draw_line(self, line, fill_color):
        # check if the method call is correct
        line.draw(self.canvas, fill_color)

    def close(self):
        self.window_running = False
