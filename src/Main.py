"""Main file of game"""
import sys
from game import Game

def main():
    """Main entry point of game"""
    game = Game()
    game.run()

if __name__ == "__main__":
    sys.exit(main())