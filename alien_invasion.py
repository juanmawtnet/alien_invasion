import sys

import pygame
from settings import Settings


class AlienInvasion:
    """ overall class to manage game assets and behavior. """

    def __init__(self):
        """ initialize the game, and greate game resources. """
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width,
            self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        # Set background color

    def run_game(self):
        """ Start the main loop for the game """
        while True:
            # Watch for keyboard and mouse events
            for event in pygame.event.get():
                print('event!')
                if event.type == pygame.QUIT:
                    sys.exit()

            # Redraw the screen during each pass through the loop
            print("fill:")
            self.screen.fill(self.settings.bg_color)

            # Make the most recently drawn screen visible
            print("display.flip:")
            pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance, and run the run_game
    ai = AlienInvasion()
    ai.run_game()
