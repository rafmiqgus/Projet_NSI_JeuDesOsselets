import pygame
import random
from button import Button

pygame.init()
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Jeu des Osselets")

def select_mode():
    """Fonction servant à selectionner le mode de jeu"""
    
    while True:
        SCREEN.blit(pygame.image.load("images/Background.png"), (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = pygame.font.Font(pygame.font.sysfont("Gabriola", 50), 50)
        Button(image=None, pos=(100, 100), text_input="PVP", font=pygame.font.SysFont("Gabriola", 50), base_color="White", hovering_color="Green")

def init_display(joueurs):
    """Fonction servant à initialiser l'affichage du jeu"""
    global rectangle_goblin, rectangle_guerrier

    joueur_1, joueur_2 = joueurs

    SCREEN.fill((245, 245, 220))

    GRID = pygame.image.load("images/grid.png")
    SCREEN.blit(GRID, (420, 60))
    SCREEN.blit(GRID, (420, 490))

    IMAGE_JOUEUR_1 = pygame.image.load("images/goblin.png")
    SCREEN.blit(pygame.transform.scale_by(IMAGE_JOUEUR_1, 0.4), (100, 550))

    IMAGE_JOUEUR_2 = pygame.image.load("images/guerrier.png")
    SCREEN.blit(pygame.transform.scale_by(IMAGE_JOUEUR_2, 0.4), (875.2, 30))

    FONT = pygame.font.SysFont("Gabriola", 40)

    nom_joueur_1 = FONT.render(joueur_1, True, "black")
    SCREEN.blit(nom_joueur_1, (35, 505))

    nom_joueur_2 = FONT.render(joueur_2, True, "black")
    nom_joueur_2_width = nom_joueur_2.get_width()
    nom_joueur_2_x = 1150 - nom_joueur_2_width
    SCREEN.blit(nom_joueur_2, (nom_joueur_2_x, 260))

    case_joueur_1 = pygame.draw.rect(SCREEN, (31, 142, 77), (35,300,340,190), 0)
    for i in range(4):
        pygame.draw.rect(SCREEN, (139, 69, 19), (35-i,300-i,345,195), 3)

    case_joueur_2 = pygame.draw.rect(SCREEN, (31, 142, 77), (810,300,340,190), 0)
    for i in range(4):
        pygame.draw.rect(SCREEN, (139, 69, 19), (810-i,300-i,345,195), 3)
    
    SCREEN.blit(pygame.transform.scale_by(pygame.image.load("images/carte.png"), 0.1), (5, 5))
    SCREEN.blit(pygame.transform.scale_by(pygame.image.load("images/carte.png"), 0.1), (1143.8, 743.2))

def add_de(face_dé, x, y, joueur):
    """Fonction servant à ajouter un dé sur l'affichage du jeu"""

    dé = "images/dé_" + str(face_dé) + ".png"
    
    if joueur == "joueur_2":
        if x == 1 and y == 1:
            SCREEN.blit(pygame.transform.scale_by(pygame.image.load(dé), 0.15), (420, 65))
        elif x == 2 and y == 1:
            SCREEN.blit(pygame.transform.scale_by(pygame.image.load(dé), 0.15), (540, 65))
        elif x == 3 and y == 1:
            SCREEN.blit(pygame.transform.scale_by(pygame.image.load(dé), 0.15), (665, 65))
        elif x == 1 and y == 2:
            SCREEN.blit(pygame.transform.scale_by(pygame.image.load(dé), 0.15), (420, 155))
        elif x == 2 and y == 2:
            SCREEN.blit(pygame.transform.scale_by(pygame.image.load(dé), 0.15), (540, 155))
        elif x == 3 and y == 2:
            SCREEN.blit(pygame.transform.scale_by(pygame.image.load(dé), 0.15), (665, 155))
        elif x == 1 and y == 3:
            SCREEN.blit(pygame.transform.scale_by(pygame.image.load(dé), 0.15), (420, 250))
        elif x == 2 and y == 3:
            SCREEN.blit(pygame.transform.scale_by(pygame.image.load(dé), 0.15), (540, 250))
        elif x == 3 and y == 3:
            SCREEN.blit(pygame.transform.scale_by(pygame.image.load(dé), 0.15), (665, 250))
    elif joueur == "joueur_1":
        if x == 1 and y == 1:
            SCREEN.blit(pygame.transform.scale_by(pygame.image.load(dé), 0.15), (420, 495))
        elif x == 2 and y == 1:
            SCREEN.blit(pygame.transform.scale_by(pygame.image.load(dé), 0.15), (540, 495))
        elif x == 3 and y == 1:
            SCREEN.blit(pygame.transform.scale_by(pygame.image.load(dé), 0.15), (665, 495))
        elif x == 1 and y == 2:
            SCREEN.blit(pygame.transform.scale_by(pygame.image.load(dé), 0.15), (420, 587))
        elif x == 2 and y == 2:
            SCREEN.blit(pygame.transform.scale_by(pygame.image.load(dé), 0.15), (560, 587))
        elif x == 3 and y == 2:
            SCREEN.blit(pygame.transform.scale_by(pygame.image.load(dé), 0.15), (665, 587))
        elif x == 1 and y == 3:
            SCREEN.blit(pygame.transform.scale_by(pygame.image.load(dé), 0.15), (420, 678))
        elif x == 2 and y == 3:
            SCREEN.blit(pygame.transform.scale_by(pygame.image.load(dé), 0.15), (540, 678))
        elif x == 3 and y == 3:
            SCREEN.blit(pygame.transform.scale_by(pygame.image.load(dé), 0.15), (665, 678))

def remove_de(joueur):
    """Fonction servant à supprimer un dé sur l'affichage du jeu"""
    
    if joueur == "joueur_1":
        pygame.draw.rect(SCREEN, (31, 142, 77), (35,300,340,190), 0)
        for i in range(4):
            pygame.draw.rect(SCREEN, (139, 69, 19), (35-i,300-i,345,195), 3)
    elif joueur == "joueur_2":
        pygame.draw.rect(SCREEN, (31, 142, 77), (810,300,340,190), 0)
        for i in range(4):
            pygame.draw.rect(SCREEN, (139, 69, 19), (810-i,300-i,345,195), 3)

def lancer_de(joueur):
    """Fonction servant à charger l'animation de lancé de dé"""

    clock = pygame.time.Clock()
    frames = [pygame.image.load(f"images/dé_{i}.png") for i in [4, 2, 5, 1, 6, 3, 5, 1, 3, 5, 2, 6, 5, 2]]
    frame = 0

    for frame in range(len(frames)):
        clock.tick(12)
        if frame >= len(frames):
            frame = 0

        image = frames[frame]

        if joueur == "joueur_1":
            pygame.draw.rect(SCREEN, (31, 142, 77), (35,300,340,190), 0)
            for i in range(4):
                pygame.draw.rect(SCREEN, (139, 69, 19), (35-i,300-i,345,195), 3)
            SCREEN.blit(pygame.transform.scale_by(image, 0.2), (153, 343))

        elif joueur == "joueur_2":
            pygame.draw.rect(SCREEN, (31, 142, 77), (810,300,340,190), 0)
            for i in range(4):
                pygame.draw.rect(SCREEN, (139, 69, 19), (810-i,300-i,345,195), 3)
            SCREEN.blit(pygame.transform.scale_by(image, 0.2), (930, 340))

        face_random = random.randint(1, 6)
        image = pygame.image.load(f"images/dé_{face_random}.png")
        
        if joueur == "joueur_1":
            pygame.draw.rect(SCREEN, (31, 142, 77), (35,300,340,190), 0)
            for i in range(4):
                pygame.draw.rect(SCREEN, (139, 69, 19), (35-i,300-i,345,195), 3)
            SCREEN.blit(pygame.transform.scale_by(image, 0.2), (153, 343))

        elif joueur == "joueur_2":
            pygame.draw.rect(SCREEN, (31, 142, 77), (810,300,340,190), 0)
            for i in range(4):
                pygame.draw.rect(SCREEN, (139, 69, 19), (810-i,300-i,345,195), 3)
            SCREEN.blit(pygame.transform.scale_by(image, 0.2), (930, 340))

        pygame.display.update()

    return face_random
        