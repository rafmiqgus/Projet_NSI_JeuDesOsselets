import pygame

pygame.init()
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Jeu des Osselets")

def init_display():
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

def add_dé(face_dé, x, y, joueur):
    dé = "images/dé_" + str(face_dé) + ".png"

    if joueur == "hibou":
        if x == 1 and y == 1:
            screen.blit(pygame.transform.scale_by(pygame.image.load(dé), 0.15), (420, 65))
        elif x == 1 and y == 2:
            screen.blit(pygame.transform.scale_by(pygame.image.load(dé), 0.15), (540, 65))
        elif x == 1 and y == 3:
            screen.blit(pygame.transform.scale_by(pygame.image.load(dé), 0.15), (665, 65))
        elif x == 2 and y == 1:
            screen.blit(pygame.transform.scale_by(pygame.image.load(dé), 0.15), (420, 155))
        elif x == 2 and y == 2:
            screen.blit(pygame.transform.scale_by(pygame.image.load(dé), 0.15), (540, 155))
        elif x == 2 and y == 3:
            screen.blit(pygame.transform.scale_by(pygame.image.load(dé), 0.15), (665, 155))
        elif x == 3 and y == 1:
            screen.blit(pygame.transform.scale_by(pygame.image.load(dé), 0.15), (420, 250))
        elif x == 3 and y == 2:
            screen.blit(pygame.transform.scale_by(pygame.image.load(dé), 0.15), (540, 250))
        elif x == 3 and y == 3:
            screen.blit(pygame.transform.scale_by(pygame.image.load(dé), 0.15), (665, 250))
    elif joueur == "blaireau":
        if x == 1 and y == 1:
            screen.blit(pygame.transform.scale_by(pygame.image.load(dé), 0.15), (420, 495))
        elif x == 1 and y == 2:
            screen.blit(pygame.transform.scale_by(pygame.image.load(dé), 0.15), (540, 495))
        elif x == 1 and y == 3:
            screen.blit(pygame.transform.scale_by(pygame.image.load(dé), 0.15), (665, 495))
        elif x == 2 and y == 1:
            screen.blit(pygame.transform.scale_by(pygame.image.load(dé), 0.15), (420, 587))
        elif x == 2 and y == 2:
            screen.blit(pygame.transform.scale_by(pygame.image.load(dé), 0.15), (540, 587))
        elif x == 2 and y == 3:
            screen.blit(pygame.transform.scale_by(pygame.image.load(dé), 0.15), (665, 587))
        elif x == 3 and y == 1:
            screen.blit(pygame.transform.scale_by(pygame.image.load(dé), 0.15), (420, 678))
        elif x == 3 and y == 2:
            screen.blit(pygame.transform.scale_by(pygame.image.load(dé), 0.15), (540, 678))
        elif x == 3 and y == 3:
            screen.blit(pygame.transform.scale_by(pygame.image.load(dé), 0.15), (665, 678))
