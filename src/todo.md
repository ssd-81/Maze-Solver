check if a cell exists in a particular direction for dfs traversal 
    def _solve_r(self, i, j):
        '''depth first solution; other algorithms can be applied as well'''
        # self._animate()
        self._draw_cell(i, j)
        self._cells[i][j].visited = True
        if self._cells[i][j] == self._cells[self._num_rows-1][self._num_cols-1]:
            return True
        directions = [(i, j+1), (i+1, j), (i, j-1), (i-1, j)]
        for ni, nj in directions:
            if 0 <=ni<self._num_rows and 0<=nj<self._num_cols and not self._cells[ni][nj].visited:
                if ni == i-1 and nj == j:
                    if not self._cells[ni][nj].has_left_wall:
                        self._draw_cell(ni, nj)
                        solved = self._solve_r(ni, nj)
                        if solved:
                            return True
                        else:
                            self._cells[ni][nj].draw_move(self._cells[i][j], True)

                
                elif ni == i and nj == j+1:
                    if not self._cells[ni][nj].has_top_wall:
                        self._draw_cell(ni, nj)
                        solved = self._solve_r(ni, nj)
                        if solved:
                            return True
                        else:
                            self._cells[ni][nj].draw_move(self._cells[i][j], True)

                
                elif ni == i+1 and nj == j:
                    if not self._cells[ni][nj].has_right_wall:
                        self._draw_cell(ni, nj)
                        solved = self._solve_r(ni, nj)
                        if solved:
                            return True
                        else:
                            self._cells[ni][nj].draw_move(self._cells[i][j], True)
                
                elif ni == i and nj == j-1:
                    if not self._cells[ni][nj].has_bottom_wall:
                        self._draw_cell(ni, nj)
                        solved = self._solve_r(ni, nj)
                        if solved:
                            return True
                        else:
                            self._cells[ni][nj].draw_move(self._cells[i][j], True)
                
                else:
                    return False