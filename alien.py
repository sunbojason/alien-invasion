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

        # load alien image and get its rectangle shape
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # start each new alien near the top left of the scrren
        # top left = (0,0)
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exat horizontal position
        self.x = float(self.rect.x)

        