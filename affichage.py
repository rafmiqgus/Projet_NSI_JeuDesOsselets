import pygame
import random

pygame.init()
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Jeu des Osselets")

def init_display(joueur_1, joueur_2):
    """Fonction servant à initialiser l'affichage du jeu"""
    global rectangle_goblin, rectangle_guerrier

    screen.fill((245, 245, 220))

    grid = pygame.image.load("images/grid.png")
    screen.blit(grid, (420, 60))
    screen.blit(grid, (420, 490))

    image_joueur_1 = pygame.image.load("images/goblin.png")
    screen.blit(pygame.transform.scale_by(image_joueur_1, 0.4), (100, 500))

    image_joueur_2 = pygame.image.load("images/guerrier.png")
    screen.blit(pygame.transform.scale_by(image_joueur_2, 0.4), (875.2, 30))

    font = pygame.font.SysFont("Gabriola", 40)
    nom_joueur_1 = font.render(joueur_1, True, "black")
    screen.blit(nom_joueur_1, (165, 685))
    nom_joueur_2 = font.render(joueur_2, True, "black")
    screen.blit(nom_joueur_2, (935, 245))

    rectangle_goblin = pygame.draw.rect(screen, (31, 142, 77), (35,300,340,190), 0)
    for i in range(4):
        pygame.draw.rect(screen, (139, 69, 19), (35-i,300-i,345,195), 3)

    rectangle_guerrier = pygame.draw.rect(screen, (31, 142, 77), (810,300,340,190), 0)
    for i in range(4):
        pygame.draw.rect(screen, (139, 69, 19), (810-i,300-i,345,195), 3)

def add_dé(face_dé, x, y, joueur):
    """Fonction servant à ajouter un dé sur l'affichage du jeu"""

    dé = "images/dé_" + str(face_dé) + ".png"
    
    if joueur == "hibou":
        if x == 1 and y == 1:
            screen.blit(pygame.transform.scale_by(pygame.image.load(dé), 0.15), (420, 65))
        elif x == 2 and y == 1:
            screen.blit(pygame.transform.scale_by(pygame.image.load(dé), 0.15), (540, 65))
        elif x == 3 and y == 1:
            screen.blit(pygame.transform.scale_by(pygame.image.load(dé), 0.15), (665, 65))
        elif x == 1 and y == 2:
            screen.blit(pygame.transform.scale_by(pygame.image.load(dé), 0.15), (420, 155))
        elif x == 2 and y == 2:
            screen.blit(pygame.transform.scale_by(pygame.image.load(dé), 0.15), (540, 155))
        elif x == 3 and y == 2:
            screen.blit(pygame.transform.scale_by(pygame.image.load(dé), 0.15), (665, 155))
        elif x == 1 and y == 3:
            screen.blit(pygame.transform.scale_by(pygame.image.load(dé), 0.15), (420, 250))
        elif x == 2 and y == 3:
            screen.blit(pygame.transform.scale_by(pygame.image.load(dé), 0.15), (540, 250))
        elif x == 3 and y == 3:
            screen.blit(pygame.transform.scale_by(pygame.image.load(dé), 0.15), (665, 250))
    elif joueur == "blaireau":
        if x == 1 and y == 1:
            screen.blit(pygame.transform.scale_by(pygame.image.load(dé), 0.15), (420, 495))
        elif x == 2 and y == 1:
            screen.blit(pygame.transform.scale_by(pygame.image.load(dé), 0.15), (540, 495))
        elif x == 3 and y == 1:
            screen.blit(pygame.transform.scale_by(pygame.image.load(dé), 0.15), (665, 495))
        elif x == 1 and y == 2:
            screen.blit(pygame.transform.scale_by(pygame.image.load(dé), 0.15), (420, 587))
        elif x == 2 and y == 2:
            screen.blit(pygame.transform.scale_by(pygame.image.load(dé), 0.15), (540, 587))
        elif x == 3 and y == 2:
            screen.blit(pygame.transform.scale_by(pygame.image.load(dé), 0.15), (665, 587))
        elif x == 1 and y == 3:
            screen.blit(pygame.transform.scale_by(pygame.image.load(dé), 0.15), (420, 678))
        elif x == 2 and y == 3:
            screen.blit(pygame.transform.scale_by(pygame.image.load(dé), 0.15), (540, 678))
        elif x == 3 and y == 3:
            screen.blit(pygame.transform.scale_by(pygame.image.load(dé), 0.15), (665, 678))

def lancer_dé(joueur):
    """Fonction servant à charger l'animation de lancé de dé"""

    clock = pygame.time.Clock()
    frames = [pygame.image.load(f"images/dé_{i}.png") for i in [4, 2, 5, 1, 6, 3, 5]]
    frame = 0

    for frame in range(len(frames)):
        clock.tick(10)
        if frame >= len(frames):
            frame = 0

        image = frames[frame]

        if joueur == "joueur_1":
            pygame.draw.rect(screen, (31, 142, 77), (35,300,340,190), 0)
            for i in range(4):
                pygame.draw.rect(screen, (139, 69, 19), (35-i,300-i,345,195), 3)
            screen.blit(pygame.transform.scale_by(image, 0.2), (153, 343))

        elif joueur == "joueur_2":
            pygame.draw.rect(screen, (31, 142, 77), (810,300,340,190), 0)
            for i in range(4):
                pygame.draw.rect(screen, (139, 69, 19), (810-i,300-i,345,195), 3)
            screen.blit(pygame.transform.scale_by(image, 0.2), (930, 340))

        face_random = random.randint(1, 6)
        image = pygame.image.load(f"images/dé_{face_random}.png")
        
        if joueur == "joueur_1":
            pygame.draw.rect(screen, (31, 142, 77), (35,300,340,190), 0)
            for i in range(4):
                pygame.draw.rect(screen, (139, 69, 19), (35-i,300-i,345,195), 3)
            screen.blit(pygame.transform.scale_by(image, 0.2), (153, 343))

        elif joueur == "joueur_2":
            pygame.draw.rect(screen, (31, 142, 77), (810,300,340,190), 0)
            for i in range(4):
                pygame.draw.rect(screen, (139, 69, 19), (810-i,300-i,345,195), 3)
            screen.blit(pygame.transform.scale_by(image, 0.2), (930, 340))
        pygame.display.update()

        return face_random
        