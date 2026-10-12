# 🏴‍☠️ Pirate Battleship

A pirate-themed Battleship game for the terminal, written in Python.

Enemy ships are hidden somewhere in a 10×10 sea. Fire your cannons by entering coordinates, and try to sink every ship in as few shots as possible!

## How to play

- Enter the **row** and **column** you want to fire at, separated by a space, for example: `3 5`
- Type `q` to abandon ship and quit.
- The board uses these symbols:

| Symbol | Meaning |
|---|---|
| `~` | Open sea (not fired at yet) |
| `*` | Splash (miss) |
| `#` | Wreckage (hit) |

The enemy fleet has five ships, with lengths 5, 4, 3, 3 and 2. They can be placed horizontally or vertically, but never overlap.

## Files

| File | Contents |
|---|---|
| `cell.py` | `Cell` class: one square of sea |
| `board.py` | `Board` class: the grid, ship placement and shooting |
| `game.py` | `Game` class: the game loop and pirate dialogue |
| `main.py` | Starts the game |

## About

Made as a passion project to practice object-oriented programming in Python, inspired by the course IN1000 at the University of Oslo.
