import pygame 
from affichage import *

init_main_menu()
init_display(("joueur_1", "joueur_2"))

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit()