import pygame
import assets

class Spieler:

    def __init__(self,x,y,geschw,breite,hoehe,sprungvar,richtg,schritteRechts,schritteLinks, screen):
        self.x = x
        self.y = y
        self.geschw = geschw
        self.breite = breite
        self.hoehe = hoehe
        self.sprungvar = sprungvar
        self.richtg = richtg
        self.schritteRechts = schritteRechts
        self.schritteLinks = schritteLinks
        self.sprung = False
        self.last = [1,0]
        self.ok = True
        self.screen = screen

    def updateAngriffszustand(self):
        if self.imAngriff and self.angriffTimer > 0:
            self.angriffTimer -= 1
        elif self.angriffTimer <= 0:
            self.imAngriff = False

    def laufen(self,liste):
        if liste[0]:
            self.x -= self.geschw
            self.richtg = [1,0,0,0,0,0]
            self.schritteLinks += 1
        if liste[1]:
            self.x += self.geschw
            self.richtg = [0,1,0,0,0,0]
            self.schritteRechts += 1

    def laufenAufDerStelle(self,liste):
        # Aktualisiere nur die Animation, ohne die Position zu ändern
        if liste[0]:  # Laufen nach links auf der Stelle
            self.richtg = [1,0,0,0,0,0]
            self.schritteLinks += 1
            if self.schritteLinks == 63:
                self.schritteLinks = 0
        if liste[1]:  # Laufen nach rechts auf der Stelle
            self.richtg = [0,1,0,0,0,0]
            self.schritteRechts += 1
            if self.schritteRechts == 63:
                self.schritteRechts = 0

        self.spZeichnen()

    def resetSchritte(self):
        self.schritteLinks = 0
        self.schritteRechts = 0

    def stehen(self):
        self.richtg = [0,0,1,0,0,0]
        self.resetSchritte()

    def sprungSetzen(self):
        if self.sprungvar == -16:
            self.sprung = True
            self.sprungvar = 15
            pygame.mixer.Sound.play(assets.sprungSound)

    def springen(self):
        if self.sprung:
            self.richtg = [0,0,0,1,0,0]
            if self.sprungvar >= -15:
                n = 1
                if self.sprungvar < 0:
                    n = -1
                self.y -= (self.sprungvar**2)*0.17*n
                self.sprungvar -= 1
            else:
                self.sprung = False

    def spZeichnen(self):
        if self.schritteRechts == 63:
            self.schritteRechts = 0
        if self.schritteLinks == 63:
            self.schritteLinks = 0
 
        if self.richtg[0]:
            self.screen.blit(assets.linksGehen[self.schritteLinks//8], (self.x,self.y))
            self.last = [1,0]
 
        if self.richtg[1]:
            self.screen.blit(assets.rechtsGehen[self.schritteRechts//8], (self.x,self.y))
            self.last = [0,1]
 
        if self.richtg[2]:
            self.screen.blit(assets.stand, (self.x,self.y))
            
        if self.richtg[3]:
            self.screen.blit(assets.sprung, (self.x,self.y))

        if self.richtg[4]:
            self.screen.blit(assets.angriffLinks, (self.x, self.y))
      

        if self.richtg[5]:
            self.screen.blit(assets.angriffRechts, (self.x, self.y))
   
            