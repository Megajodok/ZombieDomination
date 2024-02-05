import pygame

from Text_Element import Textelement

class Button(Textelement):
    """Represents the menu Buttons"""
    def __init__(self, screen, text, color, font_size, x_position, y_position):
        super().__init__(screen, text, color, font_size, x_position, y_position)
        self.button_width = 230
        self.button_height = 80
    
    def _draw_element(self):
        """Displays Button on screen"""
        mouse = pygame.mouse.get_pos() 
        button_text = self.font.render(self.text, True, self.font_color)
        self.rect = pygame.draw.rect(
                self.screen, 
                (47,47,47),
                [self.x_position, self.y_position, self.button_width, self.button_height])
        if self.rect.collidepoint(mouse):
            self.rect = pygame.draw.rect(
                self.screen, 
                (124,2,0),
                [self.x_position, self.y_position, self.button_width, self.button_height])
        self.screen.blit(
             button_text, 
             (self.button_width *0.1, self.y_position+10))
        