import pygame


class Shield():
    """A class to manage the shield in front of the ship."""

    def __init__(self, ai_settings, screen, ship):
        self.screen = screen
        self.ai_settings = ai_settings

        # Create a rect at 0, 0 and then set its correct position.
        self.rect = pygame.Rect(0, 0, ai_settings.shield_width, ai_settings.shield_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top - 10
        self.screen_rect = self.screen.get_rect()

        # Store the bullet's position as a decimal value.
        self.center = float(self.rect.centerx)

        self.color = ai_settings.shield_color

        # Movement flags
        self.s_moving_right = False
        self.s_moving_left = False

    def update(self):
        """Update the shield's position based on the movement of the flag."""
        # Update the shield's center value. not the rect.
        if self.s_moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.shield_speed_factor
        if self.s_moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.shield_speed_factor

        # Update rect object from self.center
        self.rect.centerx = self.center

    def draw_shield(self):
        """Draw the shield to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)

    def center_shield(self):
        """Center the ship on the screen."""
        self.center = self.screen_rect.centerx



