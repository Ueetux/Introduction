# pygame_drawing
# Author: Hector
# November 9 2021

# Get introduced to pygame and draw objects on screen

import pygame

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
WINDOW_TITLE = "Pygame Drawing"

def main() -> None:
    """Driver of the python script"""
    # Create the screen
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_mode(WINDOW_TITLE)

    # Create some local variables that describe the enviornment
    done = False
    clock = pygame.time.Clock()

    # Create the main loop
    while not done:

        # Make space for the event listener
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        # Change the environment
        # Draw the environment
        screen.fill(WHITE)
        # Update the screen
        pygame.display.flip
        # Tick the clock
        clock.yick(75)

if __name__ == "__main__":
    main()