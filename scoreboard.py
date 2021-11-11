'''
@File        :scoreboard.py
@Description :
@Date        :2021/11/11 16:44:11
@Author      :Bo Sun
'''

import pygame.font

class Scoreboard:
    """
    display the score information
    """
    def __init__(self, ai_game):
        """
        initialization
        """
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        # set the size and other properties
        self.text_color = (30,30,30)
        self.font = pygame.font.SysFont(None, 48)

        # preprare the game image
        self.prep_score()
        self.prep_high_score()
        self.prep_level()

    def prep_score(self):
        """
        Render the score as an image
        """
        rounded_score = round(self.stats.score,-1)
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, 
            True, self.text_color, self.settings.bg_color)

        # dispaly the score in the northeast the screen
        self.score_image_rect = self.score_image.get_rect()
        self.score_image_rect.right = self.screen_rect.right - 20
        self.score_image_rect.top = 20

    def show_score(self):
        """
        display the score in the screen
        """
        self.screen.blit(self.score_image, self.score_image_rect)
        self.screen.blit(self.high_score_image, self.high_score_image_rect)
        self.screen.blit(self.level_image, self.level_image_rect)

    def prep_high_score(self):
        """
        Render the high score as an image
        """
        rounded_high_score = round(self.stats.high_score,-1)
        high_score_str = "{:,}".format(rounded_high_score)
        self.high_score_image = self.font.render(high_score_str, 
            True, self.text_color, self.settings.bg_color)

        # dispaly the score in the northeast the screen
        self.high_score_image_rect = self.high_score_image.get_rect()
        self.high_score_image_rect.centerx = self.screen_rect.centerx
        self.high_score_image_rect.top = self.screen_rect.top

    def check_high_score(self):
        """
        check whether it is the highest score
        """
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()

    def prep_level(self):
        """
        Render the level as an image
        """
        level_str = str(self.stats.level)
        self.level_image = self.font.render(level_str, 
            True, self.text_color, self.settings.bg_color)

        # dispaly the score in the northeast the screen
        self.level_image_rect = self.level_image.get_rect()
        self.level_image_rect.right = self.score_image_rect.right
        self.level_image_rect.top = self.score_image_rect.bottom+10