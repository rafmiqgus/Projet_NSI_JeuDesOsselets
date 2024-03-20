import pygame 
from affichage import *

init_display()

running = True
clock = pygame.time.Clock()

lancer_dé()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit()