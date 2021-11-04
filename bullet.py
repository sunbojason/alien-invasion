'''
@File        :bullet.py
@Description :
@Date        :2021/11/04 22:46:52
@Author      :Bo Sun
'''

import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """
    manage the bullet shot by the ship
    """

    def __init__(self, ai_game) -> None:
        """
        creat a bullet objective at the current ship position
        """
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # build a rectangle representing the bullet at (0,0)
        # then set the correct position
        self.rect = pygame.Rect(0, 0, 
        self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # store the bullet position with float
        self.y = float(self.rect.y)

    def update(self):
        """
        move the bullet upward
        """
        # update the float value representing the bullet position
        self.y -= self.settings.bullet_speed
        # update the rect position representing the bullet
        self.rect.y = self.y

    def draw_bullet(self):
        """
        draw the bullet on the screen
        """
        pygame.draw.rect(self.screen, self.color, self.rect)