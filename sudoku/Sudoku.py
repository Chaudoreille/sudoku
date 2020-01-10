import re

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
    def GridsFromFile(fileName):
        """ takes a filename in parameter and \
        extracts all the sudoku grids from the file. \
        The file must contain one grid per line.\
        Each grid must be a direct sequence of 81 numbers (0 means empty)"""
        grids = []
        file = open(fileName, 'r')
        lines = file.readlines()

        for line in lines:
            sudokuGrid = Sudoku.GridFromString(line)
            grids.append(sudokuGrid)

        return grids

    @staticmethod
    def GridFromString(str):
        """ takes a string of 81 numbers (0 means empty) and \
        builds a Sudoku grid from it """
        grid = []

        str = str.strip('\n')

        if (re.search('^[0-9]{81}$', str) == None):
            raise Exception('impossible to print grid from string "{}"; string \
must be a set of 81 numbers.'.format(str))
        else:
            for i in range(len(str)):
                if (i % 9 == 0):
                    grid.append([])
                grid[i//9].append(int(str[i]))

        return grid

    @staticmethod
    def __build_border(thickness, position='middle'):
        # private method to print grid borders in terminal for display
        # only prints horizontal borders as vertical borders need to be embedded
        # in horizontal lines
        symbol = {
        'thick' : {
            'line' : '\u2501',
            'top' : {
                'left' : '\u250f',
                'mid' : '\u2533',
                'right' : '\u2513',
                'separator' : '\u252f'
            },
            'middle' : {
                'left' : '\u2523',
                'mid' : '\u254b',
                'right' : '\u252b',
                'separator' : '\u253f'
            },
            'bottom' : {
                'left' : '\u2517',
                'mid' : '\u253b',
                'right' : '\u251b',
                'separator' : '\u2537'
            }
        },
        'thin' : {
            'line' : '\u2500',
            'middle' : {
                'left' : '\u2520',
                'mid' : '\u2542',
                'right' : '\u2528',
                'separator' : '\u253c'
            }
        }
        }
        line = symbol[thickness]['line']
        border = symbol[thickness][position]
        square = (line * 3 + border['separator']) * 2 + line * 3

        str = border['left'] + (square + border['mid']) * 2 + square
        str += border['right'] + '\n'
        return str


    def __init__(self, grid):
        """grid must be a valid sudoku grid (9x9 list matrix of [0-9] numbers)\
        see static methods to import from file"""

        self.grid = grid if Sudoku.ValidGrid(grid) else [[0] * 9] * 9
        self.original = self.grid.copy()

    def __str__(self):
        """ Transforms grid in string. The string representation is made for\
        display, and therefore builds a 9x9 table with unicode characters """

        str = ''

        for i, line in enumerate(self.grid):
            if (i == 0):
                str += Sudoku.__build_border('thick', 'top')
            elif (i % 3 == 0):
                str += Sudoku.__build_border('thick', 'middle')
            else:
                 str += Sudoku.__build_border('thin')
            for j, number in enumerate(line):
                str += '\u2503' if j % 3 == 0 else '\u2502'
                str += ' ' + number.__str__() + ' ' if number != 0 else ' ' * 3
            str += '\u2503\n'

        str += Sudoku.__build_border('thick', 'bottom')

        return str

    def SetGrid(self, grid):
        """Sets the sudoku grid to the new one \
        if the provided parameter is a valid sudoku grid"""

        if (Sudoku.ValidGrid(grid)):
            self.grid = grid

    # def Backtrack(self, line=0, column=0):
    #     self.grid[line][column]

    def ValidNumber(self, line, column):
        """Checks if the number at grid[line][column] is a valid number. \
        A number is considered valid if it is unique in its \
        line, column and 3x3 square"""

        # define top-left corner for square
        squareLine = line - line % 3
        squareColumn = column - column % 3

        # if grid[line][column] is empty, return True
        if self.grid[line][column] == 0:
            return True

        # check if number is unique in line & column
        for i in range(9):
            if ((self.grid[line][column] == self.grid[line][i] and i != column)
            or (self.grid[line][column] == self.grid[i][column] and i != line)):
                return False

        # check if number is unique in its square
        for i in range(squareLine, squareLine + 3):
            for j in range (squareColumn, squareColumn + 3):
                if ((i != line or j != column)
                and self.grid[i][j] == self.grid[line][column]):
                    return False
        return True

# grids = Sudoku.GridsFromFile("grids/easy_grids.txt")
# for grid in grids:
#     sudoku = Sudoku(grid)
#     print(sudoku)
