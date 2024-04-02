import pygame 
from affichage import *

a = init_main_menu()
init_display(("joueur_1", "joueur_2"))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()

pygame.quit()