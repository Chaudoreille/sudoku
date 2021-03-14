import pytest
from ..grid.grid import SudokuGrid

class TestSudoku:
    def test_grid_validator_givenEmptyGrid_shouldReturnTrue(self):
        # with
        grid = [[0 for _ in range (9)] for _ in range(9)]

        # then
        assert SudokuGrid.validator(grid)

    def test_grid_validator_givenValidFullGrid_shouldReturnTrue(self):
        # with
        grid = [
            [5, 6, 9, 7, 2, 8, 3, 1, 4],
            [8, 2, 4, 1, 3, 9, 7, 5, 6],
            [7, 3, 1, 6, 5, 4, 8, 9, 2],
            [4, 1, 8, 5, 9, 6, 2, 7, 3],
            [6, 9, 5, 2, 7, 3, 4, 8, 1],
            [2, 7, 3, 4, 8, 1, 5, 6, 9],
            [1, 8, 2, 3, 6, 5, 9, 4, 7],
            [9, 4, 7, 8, 1, 2, 6, 3, 5],
            [3, 5, 6, 9, 4, 7, 1, 2, 8]
        ]
        # then
        assert SudokuGrid.validator(grid)

    def test_grid_validator_givenBadLine_ShouldReturnFals(self):
        # with
        grid = [[0 for _ in range(9)] for _ in range(9)]

        # when
        for i in range(9):
            grid[0][i] = i+1
        grid[0][0] = grid[0][8]

        # then
        assert not SudokuGrid.validator(grid)

    def test_grid_validator_givenBadColumn_ShouldReturnFals(self):
        # with
        grid = [[0 for _ in range(9)] for _ in range(9)]

        # when
        for i in range(9):
            grid[i][0] = i+1
        grid[0][0] = grid[8][0]

        # then
        assert not SudokuGrid.validator(grid)

    def test_grid_validator_givenBadBox_ShouldReturnFals(self):
        # with
        grid = [[0 for _ in range(9)] for _ in range(9)]

        # when
        for i in range(3):
            for j in range(3):
                grid[i][j] = i*3+j+1
        grid[0][0] = grid[2][2]

        # then
        assert not SudokuGrid.validator(grid)

    def test_grid_validator_givenValidPartialGrid_shouldReturnTrue(self):
        # with
        grid = [
            [5, 0, 9, 7, 2, 8, 0, 0, 4],
            [0, 2, 4, 1, 0, 0, 7, 0, 6],
            [0, 3, 1, 0, 5, 0, 8, 9, 2],
            [4, 1, 8, 5, 0, 0, 2, 7, 0],
            [0, 9, 0, 2, 7, 3, 0, 0, 1],
            [2, 7, 3, 4, 8, 1, 5, 6, 0],
            [1, 8, 2, 0, 6, 5, 0, 4, 7],
            [9, 4, 0, 8, 1, 2, 0, 3, 5],
            [3, 0, 6, 9, 4, 7, 0, 2, 0]
        ]
        # then
        assert SudokuGrid.validator(grid)

    def test_grid_validator_givenInvalidFullGrid_shouldReturnFalse(self):
        # with
        grid = [[1*9]*9]

        # then
        assert not SudokuGrid.validator(grid)

    def test_grid_validator_givenInvalidPartialGrid_shouldReturnFalse(self):
        # with
        grid = [[1 if i % 2 else 0 for i in range(9)] for _ in range(9)]

        # then
        assert not SudokuGrid.validator(grid)

    def test_grid_shouldReturnValidGrid(self):
        # with
        sudoku_grid = SudokuGrid()
        grid = sudoku_grid.generate()

        # then
        assert SudokuGrid.validator(grid)

    def test_partial_grid_givenValidNumber_shouldReturnGridFilledAccordingly(self):
        # with
        sudoku = SudokuGrid()
        grid = sudoku.generate_partial(20)

        # then
        assert sudoku.validator(grid)

