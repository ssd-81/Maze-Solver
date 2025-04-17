from tkinter import Tk, BOTH, Canvas


class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        root = Tk.Tk()
        root.title = "visualize-maze"  # a placeholder for now
        # might need to recheck this
        canvas = Canvas()
        canvas.pack()
        self.window_running = False
        self.__root = Tk()
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        root.update_idletasks()
        root.update()

    def wait_for_close(self):
        while self.window_running:
            self.redraw()

    def close(self):
        self.window_running = False
