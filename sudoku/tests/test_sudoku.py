import sys, os
testdir = os.path.dirname(__file__)
srcdir = '../'
sys.path.insert(0, os.path.abspath(os.path.join(testdir, srcdir)))

from Sudoku import Sudoku

def testGridValidator():
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

    assert(Sudoku.ValidGrid(grid1))
    assert(Sudoku.ValidGrid(grid2))
    assert(Sudoku.ValidGrid(grid3))
    assert(not Sudoku.ValidGrid(grid4))
    assert(not Sudoku.ValidGrid(grid5))
    assert(not Sudoku.ValidGrid(grid6))
    assert(not Sudoku.ValidGrid(4))

testGridValidator()
