import pygame 

pygame.init()
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Jeu des Osselets")
clock = pygame.time.Clock()
running = True

x = 50
y = 50
width = 100
height = 900
vel = 5

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    screen.fill("white")
    pygame.draw.line(screen, "black", (100, 100), (1100, 700), 5)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()