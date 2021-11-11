'''
@File        :button.py
@Description :
@Date        :2021/11/11 00:23:42
@Author      :Bo Sun
'''

import pygame.font

class Button:
    def __init__(self, ai_game, msg):
        """
        initialize properties of the button
        """
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # set the size and other properties
        self.width, self.height = 200, 50
        self.button_color = (255, 0, 0)
        self.text_color = (255,255,255)
        self.font = pygame.font.SysFont(None, 48)

        # create the rect objective of the button, center it
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # create the button label only once
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """
        Render the Msg as an image and center it on the button
        """
        self.msg_image = self.font.render(msg, 
            True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """
        draw a button filled by color and draw the text
        """
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)