from window import Window
from draw import Point, Line, Cell


def main():
    win = Window(800, 600)

    # line = Line(Point(100, 200), Point(300, 800))
    # win.draw_line(line, "black")

    test_cell_1 = Cell(100, 200, 200, 300, win)
    # test_cell_1.has_right_wall = False
    test_cell_2 = Cell(500, 700, 350, 450, win)
    # test_cell_2.has_left_wall = False
    test_cell_1.draw()
    test_cell_2.draw()
    test_cell_1.draw_move(test_cell_2)
    win.wait_for_close()


if __name__ == "__main__":
    main()