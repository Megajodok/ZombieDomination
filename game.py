import pygame
import sys
import assets
from spieler import Spieler
from zombie import Zombie
from kugel import Kugel
 
pygame.init()
screen = pygame.display.set_mode([1200,595])
hintergrund_pos_x = 0 #Startposition des Hintergrunds
pygame.display.set_caption("Pygame Tutorial")

spiel_zustand = "menu"  # Kann 'menu', 'spiel', oder 'beenden' sein
menue_auswahl = 0  # 0 für Spiel Start, 1 für Beenden

spieler1 = None
zombies = []
kugeln = []
verloren = False
gewonnen = False 
 
def init_spiel():
    global linkeWand, rechteWand, spieler1, zombies, verloren, gewonnen, kugeln
    linkeWand = pygame.draw.rect(screen, (255,255,255) , (0,0,2,600) , 0)
    rechteWand = pygame.draw.rect(screen, (0,0,0) , (4798,0,2,600) , 0)
    # x, y(boden), geschw, breite, höhe, sprungvar, richtg, schritteRechts, schritteLinks
    spieler1 = Spieler(300,393,12,96,128,-16,[0,0,1,0,0,0],0,0,screen)
    # x, y, geschw, breite, höhe, richtung, xmin, xmaxm, screen, startrichtung (0 links, 1 rechts)
    zombies = []
    #zombies = [Zombie(600, 393, 5, 96, 128, 4, 4800, screen, 1),
    #       Zombie(700, 393, 5, 96, 128, 4, 4800, screen, 0)]
    verloren = False
    gewonnen = False
    kugeln = []

def menu():
    global spiel_zustand, menue_auswahl

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
        if k.x >= 0 and k.x <= 1200:
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
            kugelRechteck = pygame.Rect(k.x - k.radius, k.y - k.radius, k.radius * 2, k.radius * 2)
            if zombieRechteck.colliderect(kugelRechteck):
                kugeln.remove(k)
                z.leben -= 1
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

    while spiel_zustand == "spiel":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
    
        pressed = pygame.key.get_pressed()
            
        if pressed[pygame.K_RIGHT]:
            # Wenn der Spieler sich bewegen kann, ohne dass der Hintergrund das Limit erreicht hat
            if spieler1.x < 800 and hintergrund_pos_x > -2400:
                spieler1.laufen([0, 1])
            # Wenn der Hintergrund sich noch bewegen kann
            elif hintergrund_pos_x > -3600:
                hintergrund_pos_x -= spieler1.geschw
                spieler1.laufenAufDerStelle([0,1])
            # Wenn der Hintergrund sein Limit erreicht hat und der Spieler am rechten Bildschirmrand ist
            # Verhindert, dass der Spieler über den rechten Rand hinausgeht
            elif hintergrund_pos_x <= -3600:
                if spieler1.x < 1200 - spieler1.breite:  # Begrenzt die x-Position des Spielers
                    spieler1.laufen([0, 1])
                else:
                    spieler1.x = 1200 - spieler1.breite  # Fixiert den Spieler am rechten Rand
                    
        if not pressed[pygame.K_RIGHT]:
            spieler1.stehen()

        if pressed[pygame.K_LEFT]:
            # Wenn der Spieler sich nach links bewegen kann, ohne dass der Hintergrund bewegt werden muss
            if spieler1.x > 0 and hintergrund_pos_x == 0:
                spieler1.laufen([1, 0])
            # Wenn der Hintergrund sich noch nach rechts bewegen kann
            elif hintergrund_pos_x < 0 and spieler1.x <= 300:
                hintergrund_pos_x += spieler1.geschw
                spieler1.laufenAufDerStelle([1,0])
            # Erlaubt dem Spieler, den linken Rand zu erreichen, wenn der Hintergrund am Limit ist
            elif spieler1.x > 0:
                spieler1.laufen([1, 0])

        if pressed[pygame.K_UP]:
            spieler1.sprungSetzen()
        spieler1.springen()
            
        if pressed[pygame.K_SPACE]:
            if len(kugeln) <= 4 and spieler1.ok:
                richtung = spieler1.last
                kugeln.append(Kugel(round(spieler1.x), round(spieler1.y), richtung, 8, (0,0,0), 7, screen))
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
        spieler1.spZeichnen()  # Aktualisiere die Animation des Spielers
        zeichnen()
        pygame.time.Clock().tick(60)

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