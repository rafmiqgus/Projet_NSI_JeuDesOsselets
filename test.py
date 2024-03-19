import pygame 
from affichage import *

init_display()

running = True
clock = pygame.time.Clock()

add_dé(6, 2, 2, "hibou")

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit()

fonts = pygame.font.get_fonts()
print(len(fonts))
for font in fonts:
    print(font)