class Settings():
    """ A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings"""
        self.screen_width = 1100
        self.screen_height = 700
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_limit = 3

        #  Bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

        # Shield settings.
        self.shield_width = 60
        self.shield_height = 5
        self.shield_color = 17, 63, 129

        # Alien settings
        self.fleet_drop_speed = 10

        # How quickly the game speeds up.
        self.speedup_scale = 1.1
        # How quickly the alien speeds up
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that can change throughout the game."""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.shield_speed_factor = 1.5
        self.alien_speed_factor = 1

        # fleet direction of 1 represents right; -1 represents left
        self.fleet_direction = 1

        # Score settings.
        self.alien_points = 50

    def increase_speed(self):
        """Increase speed settings and alien point values."""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.shield_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)



