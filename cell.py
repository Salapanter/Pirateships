# cell.py
# A Cell is one square on the Battleship board.
# It keeps track of whatever it holds part of an enemy ship 
# and wether our canons have fired at it.

class Cell:
    def __init__(self):
        # every cell starts out as open sea that hasn't been fired at
        self._has_ship = False
        self._is_shot = False

    def set_ship(self):
        # puts part of an enemy ship in this cell
        self._has_ship = True

    def has_ship(self):
        # returns True if this cell holds part of a ship
        return self._has_ship

    def is_shot(self):
        # returns True if this cell has already been fired at
        return self._is_shot

    def shoot(self):
        # Fires a canonball at the cell
        # returns True if it was a hit (the cell holds a ship), otherwise False.
        self._is_shot = True
        return self._has_ship

    def get_symbol(self):
        # "~" = not shot at yet. "*" = miss, "#" = wreckage (hit).
        if not self._is_shot:
            return "~"
        elif self._has_ship:
            return "#"
        else:
            return "*"