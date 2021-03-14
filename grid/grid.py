from random import sample, seed, shuffle
import copy

class SudokuGrid():
    @classmethod
    def validator(cls, grid):
        columns = [set() for i in range(9)]
        lines = [set() for i in range(9)]
        boxes = [set() for i in range(9)]

        for i in range(9):
            for j in range(9):
                current_value = grid[i][j]
                current_box = int(i / 3) * 3 + int(j / 3)

                if current_value == 0:
                    continue

                if current_value in columns[j]:
                    return False
                else:
                    columns[j].add(current_value)

                if current_value in lines[i]:
                    return False
                else:
                    lines[i].add(current_value)

                if current_value in boxes[current_box]:
                    return False
                else:
                    boxes[current_box].add(current_value)

        return True

    @classmethod
    def print_grid(cls, grid):
        print('┌'+'-'*5+'┬'+'-'*5+'┬'+'-'*5+'┐')
        for x,line in enumerate(grid):
            print('|', end='')
            for y,square in enumerate(line):
                separator = '|' if y % 3 == 2 else ' '
                print(square if square else ' ', end=separator)
            print()
            if x == 8:
                print('└'+'-'*5+'┴'+'-'*5+'┴'+'-'*5+'┘')
            elif x % 3 == 2:
                print('├'+'-'*5+'┼'+'-'*5+'┼'+'-'*5+'┤')
        print()

    def __init__(self):
        self._checkList = None
        self._grid = None
        self._values_grid = None

    def _empty_check_list(self):
        return {
            "lines": [set() for i in range(9)],
            "columns": [set() for i in range(9)],
            "boxes": [set() for i in range(9)],
        }

    def _empty_grid(self):
        return [[0 for i in range(9)] for i in range(9)]

    def _shuffled_values(self):
        seed()
        return sample([i for i in range(1,10)], 9)

    def _valid_entry(self, x, y):
        entry = self._grid[x][y]

        if entry == 0:
            return False

        for i in range(x):
            if self._grid[i][y] == entry:
                return False

        for j in range(y):
            if self._grid[x][j] == entry:
                return False

        square_start = (int(x/3)*3, int(y/3)*3)
        for i in range(square_start[0], square_start[0]+3):
            for j in range(square_start[1], square_start[1]+3):
                if i != x and j != y and self._grid[i][j] == entry:
                    return False

        return True

    def _keep_elements(self, n):
        if n == -1:
            return

        remove = 9*9
        values = [x for x in range(9)]
        seed()

        if remove > n:
            remove -= n

        while remove:
            shuffle(values)
            x = values[0]
            shuffle(values)
            y = values[0]

            if self._grid[x][y]:
                self._grid[x][y] = 0
                remove -= 1

    def generate(self):
        self._checkList = self._empty_check_list()
        self._grid = self._empty_grid()
        self._values_grid = [[self._shuffled_values() for _ in range(9)] for _ in range(9)]
        next_square = [(0,0)]

        while next_square and next_square[-1][0] < 9:
            x,y = next_square.pop()
            valid = False
            possible_values = self._values_grid[x][y]

            while not valid and possible_values:
                self._grid[x][y] = possible_values.pop()
                valid = self._valid_entry(x,y)

            if not valid:
                previous_y = (y-1)%9
                previous_x = x-int((y-1)/8)
                self._grid[previous_x][previous_y] = 0
                self._grid[x][y] = 0
                self._values_grid[x][y] = self._shuffled_values()
                continue

            next_square.append((x,y))
            y = (y + 1) % 9
            x = x if y else x + 1

            next_square.append((x, y))

        return copy.deepcopy(self._grid)

    def generate_partial(self, filled_slots=-1):
        self.generate()
        if filled_slots >= 0:
            self._keep_elements(filled_slots)
        return copy.deepcopy(self._grid)

