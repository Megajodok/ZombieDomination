import pygame

# Lade das Sprite-Sheet
sprite_sheet = pygame.image.load("Grafiken/spritesheet.png")

# Definiere die Positionen und Größen der einzelnen Bilder im Sprite-Sheet


frame_rectangles = [(0, 0, 32, 32), (32, 0, 32, 32), (64, 0, 32, 32),
                    (0, 32, 32, 32), (32, 32, 32, 32), (64, 32, 32, 32),
                    (0, 64, 32, 32), (32, 64, 32, 32), (64, 64, 32, 32),
                    (0, 96, 32, 32), (32, 96, 32, 32), (64, 96, 32, 32),
                    ]

# Lade die einzelnen Bilder in eine Liste
frames = []
for rect in frame_rectangles:
    frame = sprite_sheet.subsurface(pygame.Rect(rect))
    frames.append(frame)

# Animation logik (Hier: Zeigt die Bilder nacheinander an)
frame_index = 0
frame_delay = 100  # Millisekunden (langsamer)
current_time = pygame.time.get_ticks()

x = 100  # X-Position, an der du das Frame zeichnen möchtest
y = 100  # Y-Position, an der du das Frame zeichnen möchtest

# Initialisiere Pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Aktualisiere die Animation
    if pygame.time.get_ticks() - current_time >= frame_delay:
        current_time = pygame.time.get_ticks()
        frame_index = (frame_index + 1) % len(frames)
    
    # Hol das aktuelle Frame
    current_frame = frames[frame_index]

    # Zeige das aktuelle Frame auf dem Bildschirm
    screen.fill((0, 0, 0))  # Lösche den Bildschirm
    screen.blit(current_frame, (x, y))  # Zeige das Frame
    pygame.display.flip()

pygame.quit()
