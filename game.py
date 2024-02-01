import pygame
import sys
import assets
from spieler import Spieler
 
pygame.init()
screen = pygame.display.set_mode([1200,595])
pygame.display.set_caption("Pygame Tutorial")

# Hinzufügen von Zustandsvariablen für Menü und Spiel
spiel_zustand = "menu"  # Kann 'menu', 'spiel', oder 'beenden' sein
menue_auswahl = 0  # 0 für Spiel Start, 1 für Beenden

spieler1 = None
zombies = []
kugeln = []
verloren = False
gewonnen = False
 
class kugel:
    def __init__(self,spX,spY,richtung,radius,farbe,geschw):
        self.x = spX
        self.y = spY
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
        pygame.draw.circle(screen, self.farbe, (self.x, self.y), self.radius, 0)
 
class zombie:
    def __init__(self,x,y,geschw,breite,hoehe,richtg,xMin,xMax):
        self.x = x
        self.y = y
        self.geschw = geschw
        self.breite = breite
        self.hoehe = hoehe
        self.richtg = richtg
        self.schritteRechts = 0
        self.schritteLinks = 0
        self.xMin = xMin
        self.xMax = xMax
        self.leben = 6
        self.linksListe = [pygame.image.load("Grafiken/l1.png"),pygame.image.load("Grafiken/l2.png"),pygame.image.load("Grafiken/l3.png"),pygame.image.load("Grafiken/l4.png"),pygame.image.load("Grafiken/l5.png"),pygame.image.load("Grafiken/l6.png"),pygame.image.load("Grafiken/l7.png"),pygame.image.load("Grafiken/l8.png")]
        self.rechtsListe = [pygame.image.load("Grafiken/r1.png"),pygame.image.load("Grafiken/r2.png"),pygame.image.load("Grafiken/r3.png"),pygame.image.load("Grafiken/r4.png"),pygame.image.load("Grafiken/r5.png"),pygame.image.load("Grafiken/r6.png"),pygame.image.load("Grafiken/r7.png"),pygame.image.load("Grafiken/r8.png")]
        self.ganz = pygame.image.load("Grafiken/voll.png")
        self.halb = pygame.image.load("Grafiken/halb.png")
        self.leer = pygame.image.load("Grafiken/leer.png")
    def herzen(self):
        if self.leben >= 2:
            screen.blit(self.ganz, (507,15))
        if self.leben >= 4:
            screen.blit(self.ganz, (569,15))
        if self.leben == 6:
            screen.blit(self.ganz, (631,15))
 
        if self.leben == 1:
            screen.blit(self.halb, (507,15))
        elif self.leben == 3:
            screen.blit(self.halb, (569,15))
        elif self.leben == 5:
            screen.blit(self.halb, (631,15))
 
        if self.leben <= 0:
            screen.blit(self.leer, (507,15))
        if self.leben <= 2:
            screen.blit(self.leer, (569,15))
        if self.leben <= 4:
            screen.blit(self.leer, (631,15))

    def zZeichnen(self):
        if self.schritteRechts == 63:
            self.schritteRechts = 0
        if self.schritteLinks == 63:
            self.schritteLinks = 0
 
        if self.richtg[0]:
            screen.blit(self.linksListe[self.schritteLinks//8], (self.x,self.y))
        if self.richtg[1]:
            screen.blit(self.rechtsListe[self.schritteRechts//8], (self.x,self.y))

    def Laufen(self):
        self.x += self.geschw
        if self.geschw > 0:
            self.richtg = [0,1]
            self.schritteRechts += 1
        if self.geschw < 0:
            self.richtg = [1,0]
            self.schritteLinks += 1
            
    def hinHer(self):
        if self.x > self.xMax:
            self.geschw *= -1
        elif self.x < self.xMin:
            self.geschw *= -1
        self.Laufen()

def init_spiel():
    global linkeWand, rechteWand, spieler1, zombies, verloren, gewonnen, kugeln
    linkeWand = pygame.draw.rect(screen, (255,255,255) , (0,0,2,600) , 0)
    rechteWand = pygame.draw.rect(screen, (0,0,0) , (1198,0,2,600) , 0)
    spieler1 = Spieler(300,393,4,96,128,-16,[0,0,1,0],0,0,screen)
    zombies = [zombie(600, 393, 5, 96, 128, [0, 0], 40, 1090),
            zombie(800, 393, 4, 96, 128, [0, 0], 40, 1090)]
    verloren = False
    gewonnen = False
    kugeln = []

def menu():
    global spiel_zustand, menue_auswahl
    screen.fill((0, 0, 0))  # Schwarzer Hintergrund fürs Menü
    if menue_auswahl == 0:
        screen.blit(assets.menu1, (0, 0))  # Zeigt menu1, wenn die Auswahl auf 'Spiel Start' ist
    else:
        screen.blit(assets.menu2, (0, 0))  # Zeigt menu2, wenn die Auswahl auf 'Beenden' ist
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                menue_auswahl = 1
            elif event.key == pygame.K_UP:
                menue_auswahl = 0
            elif event.key == pygame.K_RETURN:
                if menue_auswahl == 0:
                    spiel_zustand = "spiel"  # Startet das Spiel
                    init_spiel()
                else:
                    sys.exit()  # Beendet das Programm

def zeichnen():
    screen.blit(assets.hintergrund, (0,0))
    for k in kugeln:
        k.zeichnen()
    spieler1.spZeichnen()
    
    for z in zombies:  # Zeichne jeden Zombie in der Liste
        z.zZeichnen()
        z.herzen()  # Wenn jeder Zombie eigene Lebenspunkte hat
    pygame.display.update() 
 
def kugelHandler():
    global kugeln
    for k in kugeln:
        if k.x >= 0 and k.x <= 1200:
            k.bewegen()
        else:
            kugeln.remove(k)
 
def Kollision():
    global kugeln, verloren, gewonnen
    spielerRechteck = pygame.Rect(spieler1.x+18,spieler1.y+36,spieler1.breite-36,spieler1.hoehe-36)

    for z in zombies:
        zombieRechteck = pygame.Rect(z.x+18,z.y+24,z.breite-36,z.hoehe-24)
    
        for k in kugeln:
            kugelRechteck = pygame.Rect(k.x-k.radius,k.y-k.radius,k.radius*2,k.radius*2)
            if zombieRechteck.colliderect(kugelRechteck):
                kugeln.remove(k)
                z.leben -= 1
                if z.leben <= 0 and not verloren:
                    zombies.remove(z)
                    if not zombies:
                        gewonnen = True
                        pygame.mixer.Sound.play(assets.siegSound)
                     
    
        if zombieRechteck.colliderect(spielerRechteck):
            verloren = True
            gewonnen = False
            pygame.mixer.Sound.play(assets.verlorenSound)
            spiel_zustand = "menu"
            return
 
def spiel():
    global spiel_zustand, verloren, gewonnen, kugeln 
    init_spiel()

    while spiel_zustand == "spiel":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
    
        spielerRechteck = pygame.Rect(spieler1.x,spieler1.y,96,128)
        gedrueckt = pygame.key.get_pressed()
    
        if gedrueckt[pygame.K_RIGHT] and not spielerRechteck.colliderect(rechteWand):
            spieler1.laufen([0,1])
        elif gedrueckt[pygame.K_LEFT] and not spielerRechteck.colliderect(linkeWand):
            spieler1.laufen([1,0])
        else:
            spieler1.stehen()
    
        if gedrueckt[pygame.K_UP]:
            spieler1.sprungSetzen()
        spieler1.springen()
    
        if gedrueckt[pygame.K_SPACE]:
            if len(kugeln) <= 4 and spieler1.ok:
                kugeln.append(kugel(round(spieler1.x),round(spieler1.y),spieler1.last,8,(0,0,0),7))
            spieler1.ok = False
    
        if not gedrueckt[pygame.K_SPACE]:
            spieler1.ok = True
    
        kugelHandler()
        for z in zombies:
            z.hinHer()
    
        Kollision()
        zeichnen()
        clock.tick(60)

        if verloren or gewonnen: 
            if gewonnen:
                screen.blit(assets.siegBild, (0,0))
            else:
                screen.blit(assets.verlorenBild, (0,0))
            pygame.display.update()
            pygame.time.delay(2000)

            spiel_zustand = "menu"
 
while True:
    if spiel_zustand == "menu":
        menu()
    elif spiel_zustand == "spiel":
        spiel()
    clock = pygame.time.Clock()
    clock.tick(60)