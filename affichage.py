import pygame

pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Jeu des Osselets")
clock = pygame.time.Clock()

def init_display():
    pygame.init()
    SCREEN_WIDTH = 1200
    SCREEN_HEIGHT = 800
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Jeu des Osselets")

    screen.fill("white")

    grid = pygame.image.load("images/grid.png")
    screen.blit(grid, (400, 60))
    screen.blit(grid, (400, 490))

    blaireau = pygame.image.load("images/blaireau.png")
    screen.blit(pygame.transform.scale_by(blaireau, 0.3), (125, 540))

    hibou = pygame.image.load("images/hibou.png")
    screen.blit(pygame.transform.scale_by(hibou, 0.3), (910, 90))

    font = pygame.font.SysFont("rubikbold", 30)
    nom_blaireau = font.render("Blaireau", True, (80, 227, 194))
    screen.blit(nom_blaireau, (138, 690))
    nom_hibou = font.render("Hibou", True, (184, 233, 134))
    screen.blit(nom_hibou, (935, 250))
    