'''
@File        :game_stats.py
@Description :
@Date        :2021/11/09 23:21:14
@Author      :Bo Sun
'''

class GameStats:
    """
    track the game statistics
    """
    def __init__(self, ai_game):
        """
        initialize statistics
        """
        self.settings = ai_game.settings
        self.reset_stats()

        self.game_active = False

        # high score
        self.high_score = 0

    def reset_stats(self):
        """
        initialize all statisitcs that can change during the game
        """
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 0