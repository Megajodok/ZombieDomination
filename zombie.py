import pygame
import assets

class Zombie:
    
    def __init__(self,welt_x,y,geschw,breite,hoehe,xMin,xMax, screen, startrichtung):
        self.welt_x = welt_x
        self.y = y
        self.geschw = geschw
        self.breite = breite
        self.hoehe = hoehe
        self.schritteRechts = 0
        self.schritteLinks = 0
        self.xMin = xMin
        self.xMax = xMax
        self.screen = screen
        self.leben = 6
        self.linksGehen = assets.ZombieLinksGehen
        self.rechtsGehen = assets.ZombieRechtsGehen
        self.ganz = assets.ganz
        self.halb = assets.halb
        self.leer = assets.leer

        if startrichtung == 0:
            self.geschw = -abs(self.geschw)
        elif startrichtung == 1:
            self.geschw = abs(self.geschw)
    
    def herzen(self):
        if self.leben >= 2:
            self.screen.blit(self.ganz, (507,15))
        if self.leben >= 4:
            self.screen.blit(self.ganz, (569,15))
        if self.leben == 6:
            self.screen.blit(self.ganz, (631,15))
 
        if self.leben == 1:
            self.screen.blit(self.halb, (507,15))
        elif self.leben == 3:
            self.screen.blit(self.halb, (569,15))
        elif self.leben == 5:
            self.screen.blit(self.halb, (631,15))
 
        if self.leben <= 0:
            self.screen.blit(self.leer, (507,15))
        if self.leben <= 2:
            self.screen.blit(self.leer, (569,15))
        if self.leben <= 4:
            self.screen.blit(self.leer, (631,15))

    def Laufen(self):
        # Bewegung aktualisieren
        self.welt_x += self.geschw

        # Animationsframes aktualisieren
        if self.geschw > 0:  # Bewegt sich nach rechts
            self.schritteRechts += 1
            self.schritteRechts %= len(self.rechtsGehen)  # Zyklisch durchlaufen
        elif self.geschw < 0:  # Bewegt sich nach links
            self.schritteLinks += 1
            self.schritteLinks %= len(self.linksGehen)  # Zyklisch durchlaufen

    def zZeichnen(self, hintergrund_pos_x):
        bildschirm_x = self.welt_x + hintergrund_pos_x
        if -self.breite <= bildschirm_x <= 1200:  # Im sichtbaren Bereich
            bild = None
            if self.geschw > 0:  # Geht nach rechts
                bild = self.rechtsGehen[self.schritteRechts]
            elif self.geschw < 0:  # Geht nach links
                bild = self.linksGehen[self.schritteLinks]
            if bild:
                self.screen.blit(bild, (bildschirm_x, self.y))
              
    def hinHer(self):
        # Aktualisiere welt_x statt nur x
        self.welt_x += self.geschw

        # Wenn der Zombie den rechten Bildschirmrand erreicht, ändere seine Richtung
        if self.welt_x > self.xMax:
            self.geschw = -self.geschw
            self.welt_x = self.xMax  # Setze ihn auf den rechten Rand

        # Wenn der Zombie den linken Bildschirmrand erreicht, ändere seine Richtung
        if self.welt_x < self.xMin:
            self.geschw = -self.geschw
            self.welt_x = self.xMin  # Setze ihn auf den linken Rand







