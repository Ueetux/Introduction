import sys
import textwrap
import time
import midnight_rider_text

# a text based game of intrigue and illusion

class Game:
    """Represent our game engine

    Attribute:
        done: describes the game is finished or not
    """

    def __init__(self):
        self.done = False

    def introduction(self) -> None:
        """print the introduction text"""
        print(midnight_rider_text.INTRODUCTION)
        self.typewritter_effect(midnight_rider_text.INTRODUCTION)

    def typewritter_effect(selfself, text: str)->None:
        """Print out to console with a typewritter effect."""
        for char in textwrap.dedent(text):
            time.sleep(0.05)
            sys.stdout.write(char)
            sys.stdout.flush()

    def show_coices(self): -> None
        """Show the user their choices"""
        time.sleep(1)
        print(midnight_rider_text.CHOICES)
        time.sleep(1)

    def get_choice(self) -> None:
        """"Get's users choice and changes the enviornment"""
        # Get the users response
        user_choice = input().strip(",.?!").lower()

        # Based on their choice, change the attributes
        # of the class
        if user_choice == "q":
            self.done = True


def main() -> None:
    game = Game()       #starting game
    game.introduction()

    # Main Loop:
    while not game.done:
        # TODO: Display the choices to the player
        game.show_choices()
        # TODO: ask the player what they want to do
        # TODO: change the state of the enviornment
        game.get_choice()
        # TODO: check win/lose conditions


    pass

if __name__ == "__main__":
    main()