from window import Window
from draw import Point, Line, Cell, Maze


def main():
    win = Window(800, 600)

    maze = Maze(50, 50, 10, 10, 20, 20, win)
    # maze._create_cells()
    win.wait_for_close()


if __name__ == "__main__":
    main()