import pygame 
from affichage import *

init_display(("joueur_1", "joueur_2"))

running = True
clock = pygame.time.Clock()

add_score_colonne(30, "joueur_1", 3)
remove_score_colonne("joueur_1", 3)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit()