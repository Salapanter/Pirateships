# game.py
# A game runs one priate battle.
# it holds a Board, places the enemy ships, reads orders from the captain,
# counts the canon shots and prints random pirate dialogue.

from random import choice
from board import Board


class Game:
    def __init__(self):
        # create 10x10 board and place the ships on it
        self._board = Board(10, 10)
        self._num_shots = 0
        self._ship_lengths = [5, 4, 3, 3, 2]
        for length in self._ship_lengths:
            self._board.place_ship(length)

        # Dialgoue: one list per event, one line is picked at random with choice()
        self._welcome_lines = [
            "\nAhoy, Captain! Enemy ships be hidin' in these waters. Sink 'em all!",
            "\nWelcome aboard! Load the cannons and find those scurvy ships!",
        ]
        self._invalid_lines = [
            "Arr, that be gibberish! Give me two numbers, like: 3 5",
            "The gunner can't make sense o' that, Captain. Try again!",
            "Speak plainly! Row and column, savvy?",
        ]
        self._outside_lines = [
            "That be beyond the edge o' the map! Here be dragons!",
            "We can't fire off the map, Captain!",
        ]
        self._already_shot_lines = [
            "We already blasted that spot, ye forgetful sea dog!",
            "Nothin' left there but smoke and splinters. Pick another spot!",
        ]
        self._hit_lines = [
            "KABOOM! A direct hit, Captain!",
            "Shiver me timbers, we hit something!",
            "Ha! That'll leave a mark on their hull!",
            "HIT! Their crew be swimmin' for it!",
        ]
        self._miss_lines = [
            "Splash! Nothin' but fish down there.",
            "Missed! The sea swallowed our cannonball.",
            "Bah! Only seagulls were harmed",
            "A miss! The enemy be laughin' at us, Captain...",
        ]
        self._quit_lines = [
            "Abandon ship! We'll fight another day...",
            "Ye turn tail and flee? Very well, Captain...",
        ]
        
    def _read_coordinate(self):
        # asks the player for a coordinate
        # returns:
        # "quit"     if the player typed q
        #  None      if the input was invalid
        # (row, col) if the input was two numbers
        text = input("Where shall we fire, Captain? (row col, or q to abandon ship): ")
        text = text.strip().lower()

        if text == "q":
            return "quit"
        
        parts = text.split()
        if len(parts) != 2:
            return None
        if not (parts[0].isdigit() and parts[1].isdigit()):
            return None
        
        return (int(parts[0]), int(parts[1]))
    
    def play(self):
        # The message that will be shown under the board in the next round
        message = choice(self._welcome_lines)

        while not self._board.all_ships_sunk():
            print("\n" * 30)            # push the old board out of view
            print("~" * 30)
            self._board.draw()
            print("~" * 30)
            print()
            print(message)              # the dialogue always appears here
            print()
            print("Cannonballs fired:", self._num_shots)
            print()

            coordinate = self._read_coordinate()

            if coordinate == "quit":
                print()
                print(choice(self._quit_lines))
                return

            if coordinate is None:
                message = choice(self._invalid_lines)
                continue

            row, col = coordinate
            result = self._board.shoot(row, col)

            # Save the message instead of printing it
            if result == "invalid":
                message = choice(self._outside_lines)
            elif result == "already shot":
                message = choice(self._already_shot_lines)
            else:
                self._num_shots += 1
                if result == "hit":
                    message = choice(self._hit_lines)
                else:
                    message = choice(self._miss_lines)

        # Victory: draw the final board with the victory message under it
        victory_lines = [
            f"VICTORY! Every enemy ship rests on the bottom o' the sea! ({self._num_shots} shots)",
            f"The seas be ours, Captain! Ye did it in {self._num_shots} shots!",
        ]
        print("\n" * 30)
        print("~" * 30)
        self._board.draw()
        print("~" * 30)
        print()
        print(choice(victory_lines))
        print()