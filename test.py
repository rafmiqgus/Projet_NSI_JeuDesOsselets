import pygame 
from affichage import *

init_display(("rafael", "basile"))

running = True
clock = pygame.time.Clock()

add_dé(lancer_dé("joueur_1"), 1, 3, "joueur_1")

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit()