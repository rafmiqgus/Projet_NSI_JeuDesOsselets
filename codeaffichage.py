import random, time
from assets.affichage import *
import pygame

def lancerde():
    return random.randint(1,6)

def add_list(list,joueur):
    for i in list:
        x = 1
        for k in i:
            y = 1
            de.add_grille(k,x,y,joueur)
            y += 1
        x += 1

def choixnom():
    a = str(input("Nom du joueur 1?"))
    b = str(input("Nom du joueur 2?"))
    while len(a) > 8 :
        print("Non valide, 8 lettres max")
        a = str(input("j1"))
    while len(b) > 8 :
        print("Non valide, 8 lettres max")
        b = str(input("j1"))
    return (a,b)

def precheck(j1,j2,colonne,roll):
    a = False
    if roll in j2[colonne-1] and j1[colonne-1][2] == 0:
        a = True 
    return a 

def check(desj1,desj2,colonne):
    a = False
    for k in desj1[colonne-1]:
        if k in desj2[colonne-1] and k != 0:
            a = True 
    return a 

def enleverdes(j2,placement,roll):
    nt = []
    for i in j2[placement-1]:
        if i != roll:
            nt.append(i)
    while len(nt)  < 3:
        nt.append(0)
    j2[placement-1] = nt
    return j2

def placementj1(j1,j2,placement,roll):
    while j1[placement-1][2] != 0:
        print("colonne remplie ! choisissez en une autre.")
        placement = int(input("Quelle colonne voulez vous choisir ?"))
    if placement == 1:
        if j1[0][0] == 0:
            j1[0][0]  = roll
        elif j1[0][1] == 0 and j1[0][0] != 0:
            j1[0][1]  = roll
        elif j1[0][2] == 0 and j1[0][1] != 0 and j1[0][0] != 0:
            j1[0][2]  = roll
    elif placement == 2:
        if j1[1][0] == 0:
            j1[1][0]  = roll
        elif j1[1][1] == 0 and j1[1][0] != 0:
            j1[1][1]  = roll
        elif j1[1][2] == 0 and j1[1][1] != 0 and j1[1][0] != 0:
            j1[1][2]  = roll
    elif placement == 3:
        if j1[2][0] == 0:
            j1[2][0]  = roll
        elif j1[2][1] == 0 and j1[2][0] != 0:
            j1[2][1]  = roll
        elif j1[2][2] == 0 and j1[2][1] != 0 and j1[2][0] != 0:
            j1[2][2]  = roll
    j2 = enleverdes(j2,placement,roll)

    return (j1,j2)

def checkover(j1,j2):
    over = False
    if j1[0][2] != 0 and j1[1][2] != 0 and j1[2][2] != 0:
        over = True 
    elif j2[0][2] != 0 and j2[1][2] != 0 and j2[2][2] != 0:
        over = True
    return over
def sumdes(des):
    result = []
    for k in des:
        sum = 0
        occ = []
        nbr = 0
        for i in k: 
            if i not in occ : 
                occ.append(i)
            elif i in occ :
                nbr = i 
        if occ == []:
            sum = 0
        elif len(occ) == 1:
            sum = nbr * 9
        elif len(occ) == 2:
            if nbr == occ[0]:
                sum = occ[0]*4 + occ[1]
            elif nbr == occ[1]:
                sum = occ[1]*4 + occ[0]
        else:
            sum = k[0] + k[1] + k[2]
        result.append(sum) 
    return result

def sumdestotal(j1):
    return sumdes(j1)[0] + sumdes(j1)[1] + sumdes(j1)[2]

def verifplacement():
    placement = input("Ou voulez vous placer le dé , Colonne 1,2, ou 3?")
    while placement not in ["1","2","3"]:
        print("Cet entrée n'est pas valide. Entrez 1,2 ou 3.")
        placement = input("Quelle colonne voulez vous choisir ?")
    return int(placement)

def calcplus(ap,av,roll):
    return ap - av - roll

def choixpeter(bot,roll):
    temp = bot
    a = 0
    col = random.randint(1,3)
    max = 0
    t1 = sumdestotal(bot)

    if bot[0][2] == 0:
        a = calcplus(sumdestotal([[bot[0][0],bot[0][1],roll],bot[1],bot[2]]),t1,roll)
        if  a> max:
            max = a
            col = 1
                
    if bot[1][2] == 0:
        a = calcplus(sumdestotal([bot[0],[bot[1][0],bot[1][1],roll],bot[2]]),t1,roll)
        if a > max:
            max = a
            col = 2
                
    if bot[2][2] == 0:
        a  = calcplus(sumdestotal([bot[0],bot[1],[bot[2][0],bot[2][1],roll]]),t1,roll)
        if a > max:
            max = a
            col = 3
    while bot[col-1][2] != 0:
        col = random.randint(1,3)
    
    return (col,max)

def verif_rempli(j1):
    a = random.randint(1,3)
    while j1[a-1][2] != 0:
        a = random.randint(1,3)
    return a

def duel():
    j1 = [[0,0,0],[0,0,0],[0,0,0]]
    j2 = [[0,0,0],[0,0,0],[0,0,0]]
    win = False
    print("Bienvenue ! Vous avez choisi le mode duel (1 contre 1).")
    p = choixnom()
    init_display(p)

    running = True
    while running :
        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                running = False
                pygame.quit()

        print("Au tour de" ,p[0], " .")
        roll = lancerde()
        print("Vous avez eu un " , roll, " .")
        placement = verifplacement()
        a = placementj1(j1,j2,placement,roll)
        j1 = a[0]
        j2 = a[1]
        if checkover(j1,j2):
            win = True
        clear_grille("joueur_1")
        add_list(j1,"joueur_1")
        print("Au tour de" ,p[1], " .")
        roll = lancerde()
        print("Vous avez eu un " , roll, " .")
        placement = verifplacement()
        a = placementj1(j2,j1,placement,roll)
        j2 = a[0]
        j1 = a[1]
        if checkover(j2,j1):
            win = True
        clear_grille("joueur_2")
        add_list(j2,"joueur_2")

    print("Jeu terminé.")
    somme1 = sumdestotal(j1)
    somme2 = sumdestotal(j2) 
    print("Score final de ",p[0]," : ", somme1)
    print("Score final de ",p[1]," : ", somme2)

def tarak():
    j1 = [[0,0,0],[0,0,0],[0,0,0]]
    j2 = [[0,0,0],[0,0,0],[0,0,0]]
    win = False
    print("Bienvenue ! Vous avez choisi le mode contre le bot Tarak.")
    a = input("Quel est votre nom?")
    p = (a,"Tarak")
    while not win :
        print("Au tour de" ,p[0], " .")
        roll = lancerde()
        print("Vous avez eu un " , roll, " .")
        placement = verifplacement()
        a = placementj1(j1,j2,placement,roll)
        j1 = a[0]
        j2 = a[1]
        if checkover(j1,j2):
            win = True
        
        print("Au tour de Tarak .")
        clear_grille("joueur_1")
        add_list(j1,"joueur_1")
        time.sleep(1)
        roll = lancerde()
        print("Bot tarak a eu un " , roll, " .")
        time.sleep(1)
        placement = verif_rempli(j1)
        a = placementj1(j2,j1,placement,roll)
        j2 = a[0]
        j1 = a[1]
        if checkover(j2,j1):
            win = True
        clear_grille("joueur_2")
        add_list(j2,"joueur_2")
    print("Jeu terminé.")
    somme1 = sumdestotal(j1)
    somme2 = sumdestotal(j2) 
    print("Score final de ",p[0]," : ", somme1)
    print("Score final de Tarak : ", somme2)

def dianthea():
    j1 = [[0,0,0],[0,0,0],[0,0,0]]
    bot = [[0,0,0],[0,0,0],[0,0,0]]
    win = False
    print("Bienvenue ! Vous avez choisi le mode duel contre le bot Dianthéa.")
    nom = input("Quel est votre nom ? ")
    p = (nom,"Dianthéa")
    while not win : 
        print("Au tour de" ,p[0], " .")
        roll = lancerde()
        print("Vous avez eu un " , roll, " .")
        placement = verifplacement()
        a = placementj1(j1,bot,placement,roll)
        j1 = a[0]
        bot = a[1]
        if checkover(j1,bot):
            win = True
        clear_grille("joueur_1")
        add_list(j1,"joueur_1")
        print("Au tour de Dianthéa.")   
        roll = lancerde()
        time.sleep(1)
        print("Dianthéa a obtenu un ", roll, " .")
        time.sleep(1)
        placement = choixdianthea(j1,bot,roll)[0]
        a = placementj1(bot,j1,placement,roll)
        bot = a[0]
        j1 = a[1]
        if checkover(bot,j1):
            win = True
        clear_grille("joueur_2")
        add_list(bot,"joueur_2")
    print("Jeu terminé.")
    somme1 = sumdestotal(j1)
    somme2 = sumdestotal(bot) 
    print("Score final de ",p[0]," : ", somme1)
    print("Score final de ",p[1]," : ", somme2)

def choixdianthea(j1,bot,roll):
    temp = 0
    n = 0
    col = 0 
    if precheck(bot,j1,1,roll):
        a = sumdes(j1)[0]
        enleverdes(j1,0,roll)
        b = sumdes(j1)[0]
        temp = a - b
        if temp >= n:
            n = temp
            col = 1
    if precheck(bot,j1,2,roll):
        a = sumdes(j1)[1]
        enleverdes(j1,1,roll)
        b = sumdes(j1)[1]
        temp = a - b
        if temp >= n:
            n = temp
            col = 2
    if precheck(bot,j1,3,roll):
        a = sumdes(j1)[2]
        enleverdes(j1,2,roll)
        b = sumdes(j1)[2]
        temp = a - b
        if temp >= n:
            n = temp
            col = 3
    
    if precheck(bot,j1,1,roll) == False and precheck(bot,j1,2,roll) == False and precheck(bot,j1,3,roll) == False:
        col = random.randint(1,3)
        while bot[col-1][2] != 0:
            col = random.randint(1,3)
    return (col,n)

def peter():
    j1 = [[0,0,0],[0,0,0],[0,0,0]]
    bot = [[0,0,0],[0,0,0],[0,0,0]]
    win = False
    print("Bienvenue ! Vous avez choisi le mode duel contre le bot Peter.")
    nom = input("Quel est votre nom ? ")
    p = (nom,"Peter")
    while not win : 
        print("Au tour de" ,p[0], " .")
        roll = lancerde()
        print("Vous avez eu un " , roll, " .")
        placement = verifplacement()
        a = placementj1(j1,bot,placement,roll)
        j1 = a[0]
        bot = a[1]
        if checkover(j1,bot):
            win = True
        clear_grille("joueur_1")
        add_list(j1,"joueur_1")
        print("Au tour de Peter.")   
        roll = lancerde()
        time.sleep(1)
        print("Peter a obtenu un ", roll, " .")
        time.sleep(1)
        placement = choixpeter(bot,roll)[0]
        a = placementj1(bot,j1,placement,roll)
        bot = a[0]
        j1 = a[1]
        if checkover(bot,j1):
            win = True
        clear_grille("joueur_2")
        add_list(bot,"joueur_2")
    print("Jeu terminé.")
    somme1 = sumdestotal(j1)
    somme2 = sumdestotal(bot) 
    print("Score final de ",p[0]," : ", somme1)
    print("Score final de ",p[1]," : ", somme2)

def cynthia():
    j1 = [[0,0,0],[0,0,0],[0,0,0]]
    bot = [[0,0,0],[0,0,0],[0,0,0]]
    win = False
    print("Bienvenue ! Vous avez choisi le mode duel contre le bot Cynthia.")
    nom = input("Quel est votre nom ? ")
    p = (nom,"Cynthia")
    while not win : 
        print("Au tour de" ,p[0], " .")
        roll = lancerde()
        print("Vous avez eu un " , roll, " .")
        placement = verifplacement()
        a = placementj1(j1,bot,placement,roll)
        j1 = a[0]
        bot = a[1]
        if checkover(j1,bot):
            win = True
        clear_grille("joueur_1")
        add_list(j1,"joueur_1")
        print("Au tour de Cynthia.")   
        roll = lancerde()
        time.sleep(1)
        print("Cynthia a obtenu un ", roll, " .")
        time.sleep(1)
        placement = choixcynthia(bot,j1,roll)
        a = placementj1(bot,j1,placement,roll)
        bot = a[0]
        j1 = a[1]
        if checkover(bot,j1):
            win = True
        
        clear_grille("joueur_2")
        add_list(bot,"joueur_2")
    print("Jeu terminé.")
    somme1 = sumdestotal(j1)
    somme2 = sumdestotal(bot) 
    print("Score final de ",p[0]," : ", somme1)
    print("Score final de ",p[1]," : ", somme2)

def choixcynthia(bot,j2,roll):
    a = choixdianthea(j2,bot,roll)
    b = choixpeter(bot,roll)
    col = random.randint(1,3)
    if a[1] >= b[1]:
        col = a[0]
    elif b[1] > a[1]:
        col = b[0]
    else:
        print("t")
    return col   

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    

    choix = init_main_menu()
    follow_prompt()

    if choix == "pvp":
        duel()
    elif choix == "tarak":
        tarak()
    elif choix == "dianthea":
        dianthea()
    elif choix == "peter":
        peter()
    elif choix == "cynthia":
        cynthia()
    
    init_end_game()

    pygame.display.flip()
    clock.tick(60)
  
pygame.quit()