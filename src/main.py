from window import Window
from draw import Point, Line


def main():
    win = Window(800, 600)
    line = Line(Point(100, 200), Point(300, 800))
    win.draw_line(line, "black")
    win.wait_for_close()


if __name__ == "__main__":
    main()