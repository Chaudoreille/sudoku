class Sudoku:
    @staticmethod
    def ValidGrid(grid):
        """This method tests if the parameter is a valid sudoku grid. \
        The grid must be a 9x9 list matrix of [0 - 9] integers"""

        if (grid is not None and isinstance(grid, list)):
            if (len(grid) == 9
            and all(isinstance(line, list) and len(line) == 9
            for line in grid)):
                for line in grid:
                    if (not all((isinstance(number, int)
                    and number >= 0 and number <= 9)
                    for number in line)):
                        return False
            else:
                return False
        else:
            return False
        return True

    @staticmethod
    def CreateGridFromFile(file):
        pass

    def __init__(self, grid):
        self.grid = grid if grid is not None else [[0] * 9] * 9


    def SetGrid(self, grid):
        """This method sets the sudoku grid to the new one \
        if the provided parameter is a valid sudoku grid"""
        if (Sudoku.ValidGrid(grid)):
            self.grid = grid
