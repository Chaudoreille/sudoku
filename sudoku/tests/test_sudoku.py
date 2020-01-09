import sys, os
testdir = os.path.dirname(__file__)
srcdir = '../'
sys.path.insert(0, os.path.abspath(os.path.join(testdir, srcdir)))

from Sudoku import Sudoku

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

def testGridValidator():
    # tests grid validity with different sets of grids
    assert(Sudoku.ValidGrid(grid1))
    assert(Sudoku.ValidGrid(grid2))
    assert(Sudoku.ValidGrid(grid3))
    assert(not Sudoku.ValidGrid(grid4))
    assert(not Sudoku.ValidGrid(grid5))
    assert(not Sudoku.ValidGrid(grid6))
    assert(not Sudoku.ValidGrid(4))

def testSetGrid():
    pass

def testGridFromString():
    # tests importing a grid fromm a string of 49 characters
    # Sudoku.GridFromString('000014000030000200070000000000900030601000000000000080200000104000050600000708000')
    # Sudoku.GridFromString('000000520080400000030009000501000600200700000000300000600010000000000704000000030')
    # Sudoku.GridFromString('602050000000003040000000000430008000010000200000000700500270000000000081000600000')
    # Sudoku.GridFromString('052400000000070100000000000000802000300000600090500000106030000000000089700000000')
    # Sudoku.GridFromString('602050000000004030000000000430008000010000200000000700500270000000000081000600000')
    # Sudoku.GridFromString('092300000000080100000000000107040000000000065800000000060502000400000700000900000')
    # Sudoku.GridFromString('600302000050000010000000000702600000000000054300000000080150000000040200000000700')
    # Sudoku.GridFromString('060501090100090053900007000040800070000000508081705030000050200000000000076008000')
    # Sudoku.GridFromString('005000987040050001007000000200048000090100000600200000300600200000009070000000500')
    # Sudoku.GridFromString('306070000000000051800000000010405000700000600000200000020000040000080300000500000')
    pass
    
def testGridFromFile():
    # tests importing grids fromm file
    grids = Sudoku.GridsFromFile("grids/easy_grids.txt")

    for grid in grids:
        assert(Sudoku.ValidGrid(grid))

testGridValidator()
testGridFromFile()
