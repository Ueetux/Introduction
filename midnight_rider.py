# midnight rider

import midnight

import midnight_rider_text

# a text based game of intrigue and illusion

class Game:
    """Represent our game engine

    """
    def introduction(self) -> None:
        """print the introduction text"""
        print(midnight_rider_text.INTRODUCTION)

def main() -> None:
    game = Game()       #starting game
    game.introduction()

    pass

if __name__ == "__main__":
    main()