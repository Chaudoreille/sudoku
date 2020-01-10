import sys, os
testdir = os.path.dirname(__file__)
srcdir = '../'
sys.path.insert(0, os.path.abspath(os.path.join(testdir, srcdir)))

from Sudoku import Sudoku

def testGridValidator():
    # valid grids
    grid1 = [[1] * 9] * 9
    grid2 = [[2] * 9] * 9
    grid3 = [
    [0,1,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,3,0,0,0,3,0,8],
    [0,0,0,0,0,0,0,7,0],
    [0,0,0,9,0,0,0,0,0],
    [0,0,6,0,2,0,0,0,0],
    [0,0,0,0,0,9,0,0,0],
    [0,0,4,0,0,0,0,8,0],
    [0,1,0,0,6,0,0,0,0],
    ]

    # invalid grids
    grid4 = [
    [0,1,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,'a',3,0,0,0,3,0,8],
    [0,0,0,0,0,0,0,7,0],
    [0,0,0,9,0,0,0,0,0],
    [0,0,6,0,2,0,0,0,0],
    [0,0,0,0,0,9,0,0,0],
    [0,0,4,0,0,0,0,8,0],
    [0,1,0,0,6,0,0,0,0],
    ]
    grid5 = [[2] * 9] * 8
    grid6 = [[2] * 8] * 9

    # tests grid validity with different sets of grids
    assert(Sudoku.ValidGrid(grid1))
    assert(Sudoku.ValidGrid(grid2))
    assert(Sudoku.ValidGrid(grid3))
    assert(not Sudoku.ValidGrid(grid4))
    assert(not Sudoku.ValidGrid(grid5))
    assert(not Sudoku.ValidGrid(grid6))
    assert(not Sudoku.ValidGrid(4))

def testGridFromString():
    try:
        grid1 = Sudoku.GridFromString('000014000030000200070000000000900030601000000000000080200000104000050600000708000')
        grid2 = Sudoku.GridFromString('000000520080400000030009000501000600200700000000300000600010000000000704000000030')
    except:
        assert(False)
    else:
        assert(Sudoku.ValidGrid(grid1))
        assert(Sudoku.ValidGrid(grid2))

    try:
        grid3 = Sudoku.GridFromString('000000520080400000030009')
    except:
        pass
    else:
        assert(False)

    try:
        grid4 = Sudoku.GridFromString('abasdjaksbdkasdkjaskdjbaskjdbaskbdaskbdkjasbdkabsdkabsdkbasdkjbaksbdausdhqwoiqpid')
    except:
        pass
    else:
        assert(False)

def testGridFromFile():
    # tests importing grids fromm file
    try:
        grids = Sudoku.GridsFromFile("grids/easy_grids.txt")

        for grid in grids:
            assert(Sudoku.ValidGrid(grid))
    except:
        assert(False)

def testValidNumber():
    grid = [
    [3,0,7,2,0,0,0,0,3],
    [0,0,9,1,0,7,0,0,0],
    [7,0,6,0,3,0,5,0,0],
    [0,7,0,0,0,9,0,8,0],
    [9,0,0,9,2,0,0,0,4],
    [0,1,0,8,0,0,0,5,0],
    [0,0,9,0,4,0,3,0,1],
    [0,0,0,7,0,2,0,0,0],
    [0,0,0,0,0,8,0,0,6],
    ]
    sudokuGrid = Sudoku(grid)
    # check validNumber on faulty on line
    assert(not sudokuGrid.ValidNumber(0,0))
    # check validNumber on faulty on square
    assert(not sudokuGrid.ValidNumber(0,2))
    # check validNumber on faulty on column
    assert(not sudokuGrid.ValidNumber(1,2))
    # check validNumber on empty square
    assert(sudokuGrid.ValidNumber(1,1))
    # check validNumber on valid number
    assert(sudokuGrid.ValidNumber(8,8))

testGridValidator()
testGridFromString()
testGridFromFile()
testValidNumber()
