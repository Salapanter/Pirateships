# board.py
# A board is a two-dimensional grid of Cell objects.
# It can place ships randomly, draw itself, handle shots,
# and check wether all ships have sunk.

from random import randint
from cell import Cell

class Board:
    def __init__(self, num_rows, num_cols):
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cells = self._create_board()

    def _create_board(self):
        # builds a nested list: a list of rows, where each row is a list of Cell objects
        # returns the nested list
        board = []
        for row in range(self._num_rows):
            new_row = []
            for col in range(self._num_cols):
                new_row.append(Cell())
            board.append(new_row)
        return board

    def get_cell(self, row, col):
        # returns the cell at (row, col), or None if the position is outside the board
        # other methods use this so they never crash on an invalid index
        if 0 <= row < self._num_rows and 0 <= col < self._num_cols:
            return self._cells[row][col]
        return None
    
    def draw(self):
        # prints the board with columm numbers on top and row numbers on the left
        print ("  ", end="")
        for col in range(self._num_cols):
            print(col, end=" ")
        print()

        for row in range(self._num_rows):
            print(row, end="  ")
            for col in range(self._num_cols):
                print(self._cells[row][col].get_symbol(), end=" ")
            print()
    
    def place_ship(self, length):
        # places a ship of the given length at a random position,
        # either horizontally or vertically
        # Keeps trying until it finds a position that is inside the board
        # and doesnt overlap another ship
        placed = False
        while not placed:
            direction = randint(0, 1)
            start_row = randint(0, self._num_rows - 1)
            start_col = randint(0, self._num_cols - 1)

            # make a list of all the cells the ship would cover
            ship_cells = []
            for i in range(length):
                if direction == 0:
                    cell = self.get_cell(start_row, start_col + i)
                else:
                    cell = self.get_cell(start_row + i, start_col)
                ship_cells.append(cell)

            # check that ALL the cells are valid: inside the board and empty
            ok = True
            for cell in ship_cells:
                if cell is None or cell.has_ship():
                    ok = False

            # Only place the ship if every cell was valid
            if ok:
                for cell in ship_cells:
                    cell.set_ship()
                placed = True

    def shoot(self, row, col):
        # shoots at (row, col)
        # returns "invalid", "already shot", "hit" or "miss".
        cell = self.get_cell(row, col)
        if cell is None:
            return "invalid"
        if cell.is_shot():
            return "already shot"
        if cell.shoot():
            return "hit"
        return "miss"
    
    def all_ships_sunk(self):
        # returns True if every cell with a ship has been shot at, otherwise False.
        for row in self._cells:
            for cell in row:
                if cell.has_ship() and not cell.is_shot():
                    return False
        return True