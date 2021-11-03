'''
@File        :settings.py
@Description :
@Date        :2021/11/03 22:56:03
@Author      :Bo Sun
'''

class Settings:
    """
    store all settings of the game
    """

    def __init__(self) -> None:
        """
        initialisation
        """
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)