import pygame

class Kugel:
    
    def __init__(self,spX,spY,richtung,radius,farbe,geschw, screen):
        self.x = spX
        self.y = spY
        self.screen = screen
        if richtung[0]:
            self.x += 5
            self.geschw = -1 * geschw

        elif richtung[1]:
            self.x += 92
            self.geschw = geschw
        self.y += 84
        self.radius = radius
        self.farbe = farbe

    def bewegen(self):
        self.x += self.geschw

    def zeichnen(self):
        pygame.draw.circle(self.screen, self.farbe, (self.x, self.y), self.radius, 0)