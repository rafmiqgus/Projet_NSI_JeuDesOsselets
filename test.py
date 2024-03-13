import pygame 

pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Jeu des Osselets")
clock = pygame.time.Clock()
running = True

x = 50
y = 50
width = 100
height = 100
vel = 5

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    keys = pygame.key.get_pressed()

    if (keys[pygame.K_LEFT] or keys[pygame.K_q]) and x > 0:
        x -= vel
    if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and x < SCREEN_WIDTH - width:
        x += vel
    if (keys[pygame.K_UP] or keys[pygame.K_z]) and y > 0:
        y -= vel
    if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and y < SCREEN_HEIGHT - height:
        y += vel

    screen.fill("white")
    pygame.draw.rect(screen, (0, 255, 0), (x, y, width, height))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()


prout
