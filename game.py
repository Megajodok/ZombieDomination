import pygame
import time
import sys
import assets
from spieler import Spieler
from zombie import Zombie
from kugel import Kugel

from settings import Settings
from menu import Menu
from Button import Button
 
pygame.init()
screen = pygame.display.set_mode([1200,595])
pygame.display.set_caption("Pygame Tutorial")

def init_spiel():
    global linkeWand, rechteWand, spieler1, zombies, verloren, gewonnen, kugeln, hintergrund_pos_x
    linkeWand = pygame.draw.rect(screen, (255,255,255) , (0,0,2,600) , 0)
    rechteWand = pygame.draw.rect(screen, (0,0,0) , (4798,0,2,600) , 0)
    # x, y(boden), geschw, breite, höhe, sprungvar, richtg, schritteRechts, schritteLinks
    spieler1 = Spieler(300,393,12,96,128,-16,[0,0,1,0,0,0],0,0,screen)
    # x, y, geschw, breite, höhe, richtung, xmin, xmaxm, screen, startrichtung (0 links, 1 rechts)
    zombies = []
    zombies = [Zombie(600, 393, 0.5, 96, 128, 4, 4800, screen, 1),
               Zombie(700, 393, 0.5, 96, 128, 4, 4800, screen, 0)]
               
    verloren = False
    gewonnen = False
    kugeln = []
    hintergrund_pos_x = 0

def menu(): 
    global spiel_zustand
    menu = Menu(screen)
    mouse = pygame.mouse.get_pos() 
    for event in pygame.event.get():    
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if menu.start_button.rect.collidepoint(mouse):
                spiel_zustand = "spiel"
                init_spiel()
            if menu.quit_button.rect.collidepoint(mouse):
                sys.exit()
            if menu.stats_button.rect.collidepoint(mouse):
                pass
            if menu.trophy_button.rect.collidepoint(mouse):
                pass
    

def zeichnen():
    screen.blit(assets.hintergrund, (hintergrund_pos_x,0))
    for k in kugeln:
        k.zeichnen()
    spieler1.spZeichnen()
    
    for z in zombies:  # Zeichne jeden Zombie in der Liste
        z.zZeichnen(hintergrund_pos_x)
        z.herzen()  # Wenn jeder Zombie eigene Lebenspunkte hat
    pygame.display.update() 
 
def kugelHandler():
    global kugeln
    for k in kugeln:
        if k.x >= 0 and k.x <= 1200 and k.y <= 595:
            k.bewegen()
        else:
            kugeln.remove(k)
 
def Kollision():
    global kugeln, verloren, gewonnen
    spielerRechteck = pygame.Rect(spieler1.x + 18, spieler1.y + 36, spieler1.breite - 36, spieler1.hoehe - 36)

    for z in zombies:
        # Berechne die tatsächliche Bildschirmposition des Zombies
        zombieBildschirmX = z.welt_x + hintergrund_pos_x
        zombieRechteck = pygame.Rect(zombieBildschirmX + 18, z.y + 24, z.breite - 36, z.hoehe - 24)

        for k in kugeln:
            # Anpassung an das Bild statt Kreis für die Kollision
            kugelBildRect = k.bild.get_rect(center=(k.x, k.y))
            if zombieRechteck.colliderect(kugelBildRect):
                kugeln.remove(k)
                z.leben -= 1
                z.getroffen = True
                z.blink_timer = 10
                if z.leben <= 0 and not verloren:
                    zombies.remove(z)
                    if not zombies:
                        gewonnen = True
                        pygame.mixer.Sound.play(assets.siegSound)

        # Überprüfe die Kollision zwischen dem Spieler und dem Zombie
        if spielerRechteck.colliderect(zombieRechteck):
            verloren = True
            gewonnen = False
            pygame.mixer.Sound.play(assets.verlorenSound)
            spiel_zustand = "menu"
            return
 
def spiel():
    global spiel_zustand, verloren, gewonnen, kugeln, hintergrund_pos_x
    # init_spiel() sollte nur einmal aufgerufen werden, daher entfernen wir es hier aus der spiel-Schleife

    init_spiel()

    while spiel_zustand == "spiel":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
    
        pressed = pygame.key.get_pressed()
            
        if pressed[pygame.K_RIGHT]:
            if spieler1.x < 800: # Wenn der Spieler sich bewegen kann, ohne dass der Hintergrund das Limit erreicht hat
                spieler1.laufen([0, 1])          
            elif hintergrund_pos_x > -3600: # Wenn der Hintergrund sich noch bewegen kann
                hintergrund_pos_x -= spieler1.geschw
                spieler1.laufenAufDerStelle([0,1])        
            elif hintergrund_pos_x <= -3600:  # Wenn der Hintergrund sein Limit erreicht hat und der Spieler am rechten Bildschirmrand ist
                if spieler1.x < 1200 - spieler1.breite:  # Begrenzt die x-Position des Spielers
                    spieler1.laufen([0, 1])
                    
        if not pressed[pygame.K_RIGHT]:
            spieler1.richtg = [0,0,1,0,0,0]

        if pressed[pygame.K_LEFT]:
            if spieler1.x > 0 and hintergrund_pos_x == 0: # Wenn der Spieler sich nach links bewegen kann, ohne dass der Hintergrund bewegt werden muss
                spieler1.laufen([1, 0])
            elif hintergrund_pos_x < 0 and spieler1.x <= 300:   # Wenn der Hintergrund sich noch nach rechts bewegen kann
                hintergrund_pos_x += spieler1.geschw
                spieler1.laufenAufDerStelle([1,0])
            elif spieler1.x > 0:             # Erlaubt dem Spieler, den linken Rand zu erreichen, wenn der Hintergrund am Limit ist
                spieler1.laufen([1, 0])

        if pressed[pygame.K_UP]:
            spieler1.sprungSetzen()
        spieler1.springen()
            
        if pressed[pygame.K_SPACE]:
            spieler1.angriff()
            if len(kugeln) <= 4 and spieler1.ok:
                richtung = spieler1.last 
                kugeln.append(Kugel(round(spieler1.x), round(spieler1.y), richtung, assets.tortenbild, 7, screen))
                spieler1.ok = False
                # Setze den Angriffszustand basierend auf der letzten Bewegungsrichtung
                if richtung[0]:  # Links
                    spieler1.richtg = [0, 0, 0, 0, 1, 0]  # Setze Angriff nach links        
                    
                elif richtung[1]:  # Rechts
                    spieler1.richtg = [0, 0, 0, 0, 0, 1]  # Setze Angriff nach rechts                
        else:
            spieler1.ok = True

        kugelHandler()

        for z in zombies:
            z.hinHer()
            z.Laufen()
    
        Kollision()
        #spieler1.spZeichnen()  # Aktualisiere die Animation des Spielers
        zeichnen()
  

        if verloren or gewonnen:
            if gewonnen:
                screen.blit(assets.siegBild, (0,0))
            else:
                screen.blit(assets.verlorenBild, (0,0))
            pygame.display.update()
            pygame.time.delay(2000)
            spiel_zustand = "menu"
 
spiel_zustand = "menu" 
menue_auswahl = 0  

while True:
    if spiel_zustand == "menu":
        menu()
    elif spiel_zustand == "spiel":
        spiel()

    clock = pygame.time.Clock()
    clock.tick(60)