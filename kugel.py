import pygame

class Kugel:
    
    def __init__(self,spX,spY,richtung,radius,farbe,geschw, screen):
        self.x = spX
        self.y = spY
        self.screen = screen
        self.radius = radius
        self.farbe = farbe
        self.grav = 0.5 # Schwerkraft, beeinflusst die vertikale Geschw

        if richtung[0]: #Links
            self.x += 5
            self.geschw = -1 * geschw

        elif richtung[1]: #Rechts
            self.x += 92
            self.geschw = geschw

        self.y += 84
        self.vert_geschw= -10 #Startwert der vert. Geschw. für den Wurf

    def bewegen(self):
        self.x += self.geschw
        self.y += self.vert_geschw
        self.vert_geschw += self.grav #Schwerkraft wirkt auf vertik. geschw

    def zeichnen(self):
        pygame.draw.circle(self.screen, self.farbe, (self.x, self.y), self.radius, 0)

    