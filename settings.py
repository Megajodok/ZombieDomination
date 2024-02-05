import pygame
from pathlib import Path

class Settings():
    def __init__(self):
        """Initializes Settings class""" 
        # Game Settings
        self.caption = "Zombie Domination 🤖"
        self.icon = pygame.image.load(Path("Grafiken/sprung.png"))

        # Screen Setting
        self.screen_width = 1200
        self.screen_height = 595
        self.x_background_image = 0
