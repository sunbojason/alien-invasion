'''
@File        :ship.py
@Description :
@Date        :2021/11/03 23:16:26
@Author      :Bo Sun
'''

import pygame
from pygame.sprite import Sprite
class Ship(Sprite):
    """
    manage ships
    """

    def __init__(self, ai_game):
        """
        initilize the ship and set its initial position
        """
        super().__init__()

        # track the screen
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

   
        # load ship image and get its rectangle shape
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # locate the new ship at the center of screen bottom
        self.rect.midbottom = self.screen_rect.midbottom

        # store float value
        self.x = float(self.rect.x)

        # motion flag
        self.moving_right = False
        self.moving_left = False


    
    def update(self):
        """
        adjust the ship position based on the motion flag
        """
        if self.moving_right and (self.rect.right < self.screen_rect.right):
            self.x += self.settings.ship_speed
        if self.moving_left and (self.rect.left > 0 ): # self.screen_rect.left = 0
            self.x -= self.settings.ship_speed

        # update rect based on self.x
        self.rect.x = self.x

    def blitme(self):
        """
        plot the ship at the nomiated position by self.rect
        """
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """
        put the ship to the original position
        """
        # locate the new ship at the center of screen bottom
        self.rect.midbottom = self.screen_rect.midbottom

        # store float value
        self.x = float(self.rect.x)