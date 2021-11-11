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

        # ship settings
        self.ship_limit = 3

        # bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 3

        # alien settings
        self.fleet_drop_speed = 10 # the speed to drop when reach the edge


        # accelerate the game
        self.sppedup_scale = 1.1
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """
        initialize the settings changing with the game
        """
        self.ship_speed = 1.2
        self.bullet_speed = 3.0
        self.alien_speed = 0.8

        self.fleet_direction = 1
    
    def increase_speed(self):
        """
        increase speed
        """
        self.ship_speed *= self.sppedup_scale
        self.bullet_speed *= self.sppedup_scale
        self.alien_speed *= self.sppedup_scale