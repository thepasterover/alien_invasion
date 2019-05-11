"""

Author : the_paste_rover aka Boobalan Shettiyar.
This is the main file run this so you can run your game.

"""

import pygame
from pygame.sprite import Group

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
from alien_shield import Shield
import game_functions as gf


def run_game():
    # Initialize the game and create a screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,
                                      ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Create sound to play when hit and bullet fired.
    bullet_sound = pygame.mixer.Sound('sounds/bullet.wav')
    hit_sound = pygame.mixer.Sound('sounds/hit.wav')
    music = pygame.mixer.music.load("sounds/music.wav")
    pygame.mixer.music.play(-1)


    # Make the play button,
    play_button = Button(ai_settings, screen, "Play")

    # Create an instance to store game statistics and create a scoreboard.
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    # Make a ship, a group of bullets and group of aliens and a shield.
    ship = Ship(ai_settings, screen)
    shield = Shield(ai_settings, screen, ship)
    bullets = Group()
    aliens = Group()

    # Create the fleet of the aliens
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Start the main loop for the game
    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, shield, bullets, bullet_sound)

        if stats.game_active:
            ship.update()
            shield.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, sb, ship, aliens, bullets, shield, hit_sound)

        gf.update_screen(ai_settings, screen, stats, shield, sb, ship, aliens, bullets,
                         play_button)


run_game()
