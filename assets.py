import pygame
pygame.init()

hintergrund = pygame.image.load("Grafiken/hintergrund.png")
menu1 = pygame.image.load("Grafiken/menue1.png")
menu2 = pygame.image.load("Grafiken/menue2.png")
siegBild = pygame.image.load("Grafiken/sieg.png")
verlorenBild = pygame.image.load("Grafiken/verloren.png")

angriffLinks = pygame.image.load("Grafiken/angriffLinks.png")
angriffRechts = pygame.image.load("Grafiken/angriffRechts.png")
stand = pygame.image.load("Grafiken/stand.png")
sprung = pygame.image.load("Grafiken/sprung.png")
rechtsGehen = [pygame.image.load("Grafiken/rechts1.png"),pygame.image.load("Grafiken/rechts2.png"),pygame.image.load("Grafiken/rechts3.png"),pygame.image.load("Grafiken/rechts4.png"),pygame.image.load("Grafiken/rechts5.png"),pygame.image.load("Grafiken/rechts6.png"),pygame.image.load("Grafiken/rechts7.png"),pygame.image.load("Grafiken/rechts8.png")]
linksGehen = [pygame.image.load("Grafiken/links1.png"),pygame.image.load("Grafiken/links2.png"),pygame.image.load("Grafiken/links3.png"),pygame.image.load("Grafiken/links4.png"),pygame.image.load("Grafiken/links5.png"),pygame.image.load("Grafiken/links6.png"),pygame.image.load("Grafiken/links7.png"),pygame.image.load("Grafiken/links8.png")]

sprungSound = pygame.mixer.Sound("Sounds/sprung.wav")
siegSound = pygame.mixer.Sound("Sounds/robosieg.wav")
verlorenSound = pygame.mixer.Sound("Sounds/robotod.wav")

ZombieLinksGehen = [pygame.image.load("Grafiken/l1.png"),pygame.image.load("Grafiken/l2.png"),pygame.image.load("Grafiken/l3.png"),pygame.image.load("Grafiken/l4.png"),pygame.image.load("Grafiken/l5.png"),pygame.image.load("Grafiken/l6.png"),pygame.image.load("Grafiken/l7.png"),pygame.image.load("Grafiken/l8.png")]
ZombieRechtsGehen = [pygame.image.load("Grafiken/r1.png"),pygame.image.load("Grafiken/r2.png"),pygame.image.load("Grafiken/r3.png"),pygame.image.load("Grafiken/r4.png"),pygame.image.load("Grafiken/r5.png"),pygame.image.load("Grafiken/r6.png"),pygame.image.load("Grafiken/r7.png"),pygame.image.load("Grafiken/r8.png")]
ganz = pygame.image.load("Grafiken/voll.png")
halb = pygame.image.load("Grafiken/halb.png")
leer = pygame.image.load("Grafiken/leer.png")

print(hintergrund.get_width())
print(hintergrund.get_height())


