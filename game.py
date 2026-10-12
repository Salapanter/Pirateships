# game.py
# A Game runs one pirate battle.
# It holds a Board, places the enemy ships, reads orders from the captain,
# counts the cannon shots and shows random pirate dialogue under the board.

import os
from random import choice
from board import Board


def clear_screen():
    # Clears the terminal window, including the scroll history.
    if os.name == "nt":
        # Windows: "cls" also clears the scroll history
        os.system("cls")
    else:
        # Mac/Linux: escape codes that the terminal reads as commands
        # \033[H  = move the cursor to the top left corner
        # \033[2J = clear the visible screen
        # \033[3J = clear the scroll history
        print("\033[H\033[2J\033[3J", end="")


class Game:
    def __init__(self):
        # Create a 10x10 sea and hide the enemy ships in it
        self._board = Board(10, 10)
        self._num_shots = 0
        self._ship_lengths = [5, 4, 3, 3, 2]
        for length in self._ship_lengths:
            self._board.place_ship(length)

        # Dialogue: one list per event, one line is picked at random with choice()
        self._welcome_lines = [
            "Ahoy, Captain! Enemy ships be hidin' in these waters. Sink 'em all!",
            "Welcome aboard! Load the cannons and find those scurvy ships!",
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
            "Shiver me timbers, we hit somethin'!",
            "Ha! That'll leave a mark on their hull!",
            "Hit! Their crew be swimmin' for it!",
        ]
        self._miss_lines = [
            "Splash! Nothin' but fish down there.",
            "Missed! The sea swallowed our cannonball.",
            "Bah! Only seagulls were harmed.",
            "A miss! The enemy be laughin' at us, Captain...",
        ]
        self._quit_lines = [
            "Abandon ship! We'll fight another day...",
            "Ye turn tail and flee? Very well, Captain...",
        ]

    def _draw_screen(self, message):
        # Clears the terminal and draws the board, with the message underneath.
        clear_screen()
        print()
        print("~" * 36)
        print()
        self._board.draw()
        print()
        print("~" * 36)
        print()
        print("  " + message)
        print()
        print("\tCannonballs fired:", self._num_shots)
        print("\t~ = open sea   * = splash   # = wreckage")
        print()

    def _read_coordinate(self):
        # Asks the captain where to fire.
        # Returns:
        #   "quit"      if the captain typed q
        #   None        if the input was invalid
        #   (row, col)  if the input was two numbers
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
        # Runs the battle until all enemy ships are sunk or the captain quits.
        # The message to show under the board in the next round
        message = choice(self._welcome_lines)

        while not self._board.all_ships_sunk():
            self._draw_screen(message)

            coordinate = self._read_coordinate()

            if coordinate == "quit":
                print()
                print(choice(self._quit_lines))
                print()
                return

            if coordinate is None:
                message = choice(self._invalid_lines)
                continue

            row, col = coordinate
            result = self._board.shoot(row, col)

            # Save the message instead of printing it,
            # so it is shown under the board in the next round
            if result == "invalid":
                message = choice(self._outside_lines)
            elif result == "already shot":
                message = choice(self._already_shot_lines)
            else:
                # Only valid, new shots are counted
                self._num_shots += 1
                if result == "hit":
                    message = choice(self._hit_lines)
                else:
                    message = choice(self._miss_lines)

        # These lines are made here, not in the constructor,
        # because they need the final number of shots
        victory_lines = [
            f"VICTORY! Every enemy ship rests on the bottom o' the sea! ({self._num_shots} shots)",
            f"The seas be ours, Captain! Ye did it in {self._num_shots} shots!",
        ]
        self._draw_screen(choice(victory_lines))