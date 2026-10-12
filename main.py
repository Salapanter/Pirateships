# main.py
# Starts the pirate battle with a title screen, and lets the captain play again.
# Run this file with: python3 main.py

from game import Game, clear_screen


def show_title():
    # Shows the title screen and waits for the player to press Enter
    clear_screen()
    print()
    print("        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print()
    print("              PIRATE  BATTLESHIP")
    print()
    print("                   |    |    |")
    print("                  )_)  )_)  )_)")
    print("                 )___))___))___)")
    print("               ____|____|____|____")
    print("               \\                 /")
    print("        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print()
    print("     Sink the enemy fleet in as few shots as ye can!")
    print()
    input("            Press Enter to set sail...")


def main():
    show_title()
    play_again = "y"
    while play_again == "y":
        game = Game()
        game.play()
        play_again = input("Another voyage, Captain? (y/n): ").strip().lower()
    print()
    print("Fair winds and followin' seas, Captain!")
    print()
    input("Press Enter to close the game...")


main()