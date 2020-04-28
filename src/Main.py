# Library imports
import pygame

# Local imports
# (None)

# Logger import
from Logger.Logger import logger

# Initialize pygame
pygame.init()

# Screen size constants
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

# Set up the drawing window
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

if __name__ == "__main__":
    logger.debug("Start")

    running = True

    # Main Loop
    while running:

        # Loop through the event queue
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Flip the display
        pygame.display.flip()

    pygame.quit()