import pygame
import random
from button import Button

pygame.init()
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Jeu des Osselets")

def get_font(taille): 
    """Fonction servant à selectionner la police de caractères"""
    return pygame.font.Font("assets/font.ttf", taille)

def follow_prompt():
    """Fonction servant à afficher la page 'suivez le promp' """

    SCREEN.blit(pygame.image.load("assets/Background.png"), (0, 0))

    FOLLOW_PROMPT_TEXT = get_font(70).render("Suivez le Prompt", True, "White")
    FOLLOW_PROMPT_RECT = FOLLOW_PROMPT_TEXT.get_rect(center=(600, 400))
    SCREEN.blit(FOLLOW_PROMPT_TEXT, FOLLOW_PROMPT_RECT)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    pygame.display.update()

def select_mode():
    """Fonction servant à selectionner le mode de jeu"""
    
    running = True
    while running:
        SCREEN.blit(pygame.image.load("assets/Background.png"), (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(70).render("Menu Principal", True, (245, 245, 220))
        MENU_RECT = MENU_TEXT.get_rect(center=(600, 200))
        SCREEN.blit(MENU_TEXT, MENU_RECT)

        PVP_BUTTON = Button(image=pygame.image.load("assets/Rect.png"), pos=(600, 380), text_input="PvP", font=get_font(40), base_color="White", hovering_color="Green")
        PVP_BUTTON.changeColor(MENU_MOUSE_POS)
        PVP_BUTTON.update(SCREEN)

        BOT_TARAK_BUTTON = Button(image=pygame.image.load("assets/Rect.png"), pos=(600, 460), text_input="Tarak", font=get_font(40), base_color="White", hovering_color="Green")
        BOT_TARAK_BUTTON.changeColor(MENU_MOUSE_POS)
        BOT_TARAK_BUTTON.update(SCREEN)

        BOT_DIANTHEA_BUTTON = Button(image=pygame.image.load("assets/Rect.png"), pos=(600, 540), text_input="Dianthea", font=get_font(40), base_color="White", hovering_color="Green")
        BOT_DIANTHEA_BUTTON.changeColor(MENU_MOUSE_POS)
        BOT_DIANTHEA_BUTTON.update(SCREEN)

        BOT_PETER_BUTTON = Button(image=pygame.image.load("assets/Rect.png"), pos=(600, 620), text_input="Peter", font=get_font(40), base_color="White", hovering_color="Green")
        BOT_PETER_BUTTON.changeColor(MENU_MOUSE_POS)
        BOT_PETER_BUTTON.update(SCREEN)

        BOT_CYNTHIA_BUTTON = Button(image=pygame.image.load("assets/Rect.png"), pos=(600, 700), text_input="Cynthia", font=get_font(40), base_color="White", hovering_color="Green")
        BOT_CYNTHIA_BUTTON.changeColor(MENU_MOUSE_POS)
        BOT_CYNTHIA_BUTTON.update(SCREEN)

        for button in [PVP_BUTTON, BOT_TARAK_BUTTON, BOT_DIANTHEA_BUTTON, BOT_PETER_BUTTON, BOT_CYNTHIA_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PVP_BUTTON.checkForInput(MENU_MOUSE_POS):
                    running = False 
                    return "pvp"
                if BOT_TARAK_BUTTON.checkForInput(MENU_MOUSE_POS):
                    running = False 
                    return "tarak"
                if BOT_DIANTHEA_BUTTON.checkForInput(MENU_MOUSE_POS):
                    running = False 
                    return "dianthea"
                if BOT_PETER_BUTTON.checkForInput(MENU_MOUSE_POS):
                    running = False 
                    return "peter"
                if BOT_CYNTHIA_BUTTON.checkForInput(MENU_MOUSE_POS):
                    running = False 
                    return "cynthia"

        pygame.display.update()

def init_display(joueurs):
    """Fonction servant à initialiser l'affichage du jeu"""
    global rectangle_goblin, rectangle_guerrier

    joueur_1, joueur_2 = joueurs

    SCREEN.fill((245, 245, 220))

    GRID = pygame.image.load("assets/grid.png")
    SCREEN.blit(GRID, (420, 60))
    SCREEN.blit(GRID, (420, 490))

    IMAGE_JOUEUR_1 = pygame.image.load("assets/goblin.png")
    SCREEN.blit(pygame.transform.scale_by(IMAGE_JOUEUR_1, 0.4), (100, 550))

    IMAGE_JOUEUR_2 = pygame.image.load("assets/guerrier.png")
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
    
    SCREEN.blit(pygame.transform.scale_by(pygame.image.load("assets/carte.png"), 0.1), (5, 5))
    SCREEN.blit(pygame.transform.scale_by(pygame.image.load("assets/carte.png"), 0.1), (1143.8, 743.2))

def add_de(face_dé, x, y, joueur):
    """Fonction servant à ajouter un dé sur l'affichage du jeu"""

    dé = "assets/dé_" + str(face_dé) + ".png"
    
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
    frames = [pygame.image.load(f"assets/dé_{i}.png") for i in [4, 2, 5, 1, 6, 3, 5, 1, 3, 5, 2, 6, 5, 2]]
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
        image = pygame.image.load(f"assets/dé_{face_random}.png")
        
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
        