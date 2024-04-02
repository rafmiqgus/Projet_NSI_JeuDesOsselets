import pygame 
from affichage import *

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    choix = init_main_menu()

    if choix == "pvp":
        init_display(("joueur_1", "pvp"))
    elif choix == "tarak":
        init_display(("joueur_1", "tarak"))
    elif choix == "dianthea":
        init_display(("joueur_1", "dianthea"))
    elif choix == "peter":
        init_display(("joueur_1", "peter"))
    elif choix == "cynthia":
        init_display(("joueur_1", "cynthia"))

    pygame.time.delay(2000)

    init_end_game("joueur_1", "joueur_1", choix)

    pygame.display.flip()

pygame.quit()