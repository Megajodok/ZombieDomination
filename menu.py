import pygame
from pathlib import Path

from Button import Button
from Text_Element import Textelement

class Menu:
    """Represents game menu"""
    def __init__(self, screen):
        #Screen
        self_background_image = pygame.image.load(Path("Grafiken/menu.png"))
        self_background_image = pygame.transform.scale(self_background_image, (1200, 595))
        self.title = "Zombie Domination"
        self.copyright = "© 2024 - Made with love from zombies for robots"
        self.width = 1200
        self.height = 595
        screen.blit(self_background_image, (0, 0))

        #Buttons
        self.start_button = Button(screen, "Start", (101,123,80), 34, 500, 200)
        self.start_button._draw_element()
        self.trophy_button = Button(screen, "Trophies", (101,123,80), 34, 500, 280)
        self.trophy_button._draw_element()
        self.stats_button = Button(screen, "Stats", (101,123,80), 34, 500, 360)
        self.stats_button._draw_element()
        self.quit_button = Button(screen, "Quit", (101,123,80), 34, 500, 440)
        self.quit_button._draw_element()

        #Text Elements
        #self.header = Textelement(screen, self.title, (124,2,0), 78, self.width/4, 10)._draw_element()
        self.header = Textelement(screen, self.copyright, (255,255,255), 18, self.width/3, self.height-50)._draw_element()

        pygame.display.update()  


