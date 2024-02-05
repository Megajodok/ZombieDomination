import pygame

class Kugel:
    
    def __init__(self, spX, spY, richtung, bild, geschw, screen):
        self.x = spX
        self.y = spY
        self.screen = screen
        self.original_bild = bild  # Speichere das original Bild
        self.bild = bild  # Aktuelles Bild, das gezeichnet wird
        self.rotationswinkel = 0  # Startwinkel
        self.grav = 0.5  # Schwerkraft, beeinflusst die vertikale Geschw

        if richtung[0]:  # Links
            self.x += 5
            self.geschw = -1 * geschw
        elif richtung[1]:  # Rechts
            self.x += 92
            self.geschw = geschw

        self.y += 84
        self.vert_geschw = -10  # Startwert der vert. Geschw. für den Wurf

    def bewegen(self):
        self.x += self.geschw
        self.y += self.vert_geschw
        self.vert_geschw += self.grav
        # Eventuell Rotation aktualisieren
        self.rotationswinkel = (self.rotationswinkel + 5) % 360  # Rotiere um 5 Grad pro Aufruf
        self.bild = pygame.transform.rotate(self.original_bild, self.rotationswinkel)

    def zeichnen(self):
        # Bild zentrieren, indem die Bildgröße berücksichtigt wird
        bild_rect = self.bild.get_rect(center=(self.x, self.y))
        self.screen.blit(self.bild, bild_rect)

# Das Bild muss vorher geladen werden
  # Stelle sicher, dass 'torte.png' im Projektverzeichnis ist

# Beispiel, wie ein Kugel-Objekt jetzt erstellt wird:
# 
