import random
import sys
import textwrap
import time
import midnight_rider_text

# a text based game of intrigue and illusion
# CONSTANTS

MAX_TOFU = 3
MAX_FUEL = 50

class Game:
    """Represent our game engine

    Attribute:
        done: describes the game is finished or not
        distance traveled: describe the distance traveled that we've traveled so far this game in km
        amount_of_tofu: in our inventory
        agents_distance: describes the distance between the agent and the player
        fuel: describes the amount of fuel remaining starts off at 50
    """

    def __init__(self):
        self.done = False
        self.distance_traveled = 0
        self.amount_tofu = MAX_TOFU
        self.agents_distance = -20
        self.fuel = MAX_FUEL

    def introduction(self) -> None:
        """Print the introduction text"""
        self.typewriter_effect(midnight_rider_text.INTRODUCTION)

    def typewriter_effect(self, text: str) -> None:
        """Print out to console with a typewriter effect."""
        for char in textwrap.dedent(text):
            time.sleep(0.05)
            sys.stdout.write(char)
            sys.stdout.flush()

    def show_choices(self) -> None:
        """Show the user their choices"""
        time.sleep(1)
        print(midnight_rider_text.CHOICES)
        time.sleep(1)

    def get_choice(self) -> None:
        """Gets the user's choice and changes the environment"""
        # Get the user's response
        user_choice = input().strip(",.?!").lower()

        agents_distance_now = random.randrange(7, 15)

        player_distance_now = random.randrange(10, 16)

        # Based on their choice, change the attributes
        # of the class
        if user_choice == "b":
            # move the player
            player_distance_now = random.randrange(8, 12)
            self.distance_traveled += player_distance_now
            # move the agents
            self.agents_distance += agents_distance_now - player_distance_now
            # burn fuel
            self.fuel -= random.randrange(3, 9)
            # give the player feedback
            print(f"\n------VROOOOOOOOOOOOOM")
            print(f"------You traveled {self.distance_traveled}kms")
            # Decide how far the agents go
            self.agents_distance += random.randrange(4, 12)
            time.sleep(1)


        if user_choice == "c":
            # move the player
            player_distance_now = random.randrange(10, 16)
            self.distance_traveled += player_distance_now
            # move the agents
            self.agents_distance += agents_distance_now - player_distance_now
            # burn fuel
            self.fuel -= random.randrange(5, 11)
            # give the player feedback
            print(f"\n------ZOOOOOOOOOM")
            print(f"------You traveled {self.distance_traveled}kms")
            print(f"------Extra fuel was used to power the speed boost. Your fuel is now {self.fuel}\n")
            # Decide how far the agents go
            self.agents_distance += random.randrange(7, 15)
            time.sleep(1)

        if user_choice == "d":
            self.fuel = MAX_FUEL
            print(midnight_rider_text.REFUEL)
            time.sleep(1)

        if user_choice == "e":
            print("---Status Check---")
            print(f"Distance Traveled: {self.distance_traveled} kms")
            print(f"Fuel remaining: {self.fuel} L")
            print(f"Tofu Pieces Left: {self.amount_tofu}")
            print(f"Agent's Distance: {abs(self.agents_distance)} kms behind")
            print("------")
            time.sleep(1)

        elif user_choice == "q":
            self.done = True


def main() -> None:
    game = Game()  # starting a new game
    # game.introduction()

    while not game.done:
        game.show_choices()
        game.get_choice()
        # TODO: Check win/lose conditions


if __name__ == "__main__":
    main()