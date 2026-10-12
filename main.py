# main.py
# starts the pirate battle, and lets the captain play again.


from game import Game

def main():
    play_again = "y"
    while play_again == "y":
        game = Game()
        game.play()
        play_again = input("Another voyage, Captain? (y/n): ").strip().lower()
    print("Fair winds and followin' seas, Captain!")


main()