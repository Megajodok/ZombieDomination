import pygame

class Textelement():
    """Represents heading and sub of menu"""
    def __init__(self, screen, text, color, font_size, x_position, y_position):
        self.screen = screen
        self.font_color = color
        self.x_position = x_position
        self.y_position = y_position
        self.text = text
        self.font_size = font_size
        self.font = pygame.font.SysFont('anotherdangerdemo', self.font_size)
    
    def _draw_element(self):
        text = self.font.render(self.text, True, self.font_color)
        self.screen.blit(
             text, 
             (self.x_position, self.y_position))