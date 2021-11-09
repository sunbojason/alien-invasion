'''
@File        :alien.py
@Description :
@Date        :2021/11/06 11:10:04
@Author      :Bo Sun
'''

import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """
    Represent a signle alien in the fleet.
    """
    def __init__(self, ai_game) -> None:
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        # load alien image and get its rectangle shape
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # start each new alien near the top left of the scrren
        # top left = (0,0)
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exat horizontal position
        self.x = float(self.rect.x)

    def update(self):
        """
        moven aliens
        """
        self.x += (self.settings.alien_speed*self.settings.fleet_direction)
        self.rect.x = self.x

    def check_edge(self):
        """"
        If alien reaches the edge, return True
        """
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

        