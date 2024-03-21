import pygame 
from affichage import *

init_display("rafael", "justin")

running = True
clock = pygame.time.Clock()

lancer_dé("joueur_1")

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit()

for font in pygame.font.get_fonts():
    print(font)