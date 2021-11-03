'''
@File        :ship.py
@Description :
@Date        :2021/11/03 23:16:26
@Author      :Bo Sun
'''

import pygame

class Ship:
    """
    manage ships
    """

    def __init__(self, ai_game):
        """
        initilize the ship and set its initial position
        """

        # track the screen
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # load ship image and get its rectangle shape
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # locate the new ship at the center of screen bottom
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """
        plot the ship at the nomiated position by self.rect
        """
        self.screen.blit(self.image, self.rect)