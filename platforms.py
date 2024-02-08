import pygame

class Platform:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = (0, 128, 128) #Türkis

    @staticmethod
    def drawPlatforms(screen, platforms, hintergrund_pos_x):
        for plattform in platforms:
            # Berechne die Bildschirmposition der Plattform basierend auf hintergrund_pos_x
            plattform_bildschirm_x = plattform.rect.x + hintergrund_pos_x
            # Erstelle ein neues Rect für die Plattform mit der aktualisierten X-Position
            plattform_bildschirm_rect = pygame.Rect(plattform_bildschirm_x, plattform.rect.y, plattform.rect.width, plattform.rect.height)
            pygame.draw.rect(screen, plattform.color, plattform_bildschirm_rect)

    @staticmethod
    def pruefePlattformKollision(spielerRect, plattform):
        # Prüfe, ob der untere Teil des Spielers mit der Oberseite der Plattform kollidiert
        if spielerRect.bottom >= plattform.rect.top and spielerRect.right >= plattform.rect.left and spielerRect.left <= plattform.rect.right:
            return True
        return False

    @staticmethod
    def aktualisiereSpielerPosition(screen, spieler1, platforms, hintergrund_pos_x):
        # Berechne die Weltkoordinaten von spieler1 für die Kollisionsüberprüfung
        spielerWeltX = spieler1.x + abs(hintergrund_pos_x)
        spielerRect = pygame.Rect(spielerWeltX, spieler1.y, spieler1.breite, spieler1.hoehe)
        
        aufPlattform = False
        for plattform in platforms:
            if spieler1.sprung:
                # Wenn der Spieler springt, prüfe, ob der untere Teil des Spielers die Oberseite der Plattform berührt
                if Platform.pruefePlattformKollision(spielerRect, plattform):
                    spieler1.y = plattform.rect.top - spieler1.hoehe
                    spieler1.sprung = False
                    spieler1.sprungvar = -16  # Setzt die Sprungvariable zurück
                    aufPlattform = True

            if not aufPlattform and spieler1.y < 393 and not spieler1.sprung:
                spieler1.sprung = True
                if spieler1.sprungvar > -16:
                    spieler1.sprungvar = -1

            if spieler1.y >= 393 and not aufPlattform:
                spieler1.y = 393
                spieler1.sprung = False
                spieler1.sprungvar = -16