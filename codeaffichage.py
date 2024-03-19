import random
def de():
    return random.randint(1,6)

def affichage(p,de1,de2,j1,j2):
    tempa = (8 - len(p[0]) )* " "
    tempb = (8 - len(p[1]) )* " "
    print("__________________________________________________________________________________________")
    print("|                                                                                        |")
    print("|  ",p[0],tempa,"                         |",j1[0][2],"||",j1[1][2],"||",j1[2][2],"|               ",de1,"                 |")
    print("|   score :                              ‾    ‾    ‾                                     |")
    print("|                                      |",j1[0][1],"||",j1[1][1],"||",j1[2][1],"|                                   |")
    print("|                                        ‾    ‾    ‾                                     |")
    print("|                                      |",j1[0][0],"||",j1[1][0],"||",j1[2][0],"|                                   |")
    print("|                                        ‾    ‾    ‾                                     |")
    print("|                                                                                        |")
    print("|                                                                                        |")
    print("|                                                                                        |")
    print("|  ",p[1],tempb,"                         |",j2[0][2],"||",j2[1][2],"||",j2[2][2],"|               ",de2,"                 |")
    print("|   score :                              ‾    ‾    ‾                                     |")
    print("|                                      |",j2[0][1],"||",j2[1][1],"||",j2[2][1],"|                                   |")
    print("|                                        ‾    ‾    ‾                                     |")
    print("|                                      |",j2[0][0],"||",j2[1][0],"||",j2[2][0],"|                                   |")
    print("|                                        ‾    ‾    ‾                                     |")
    print("|                                                                                        |")
    print("|________________________________________________________________________________________|")
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
def check():
    return True

def placementj1(j1,j2,placement,roll):
    while j1[placement-1][2] != 0:
        print("colonne remplie ! choisissez en une autre.")
        placement = int(input("Quelle colonne voulez vous choisir ?"))
    if check():
        for i in j2[placement-1]:
            nt = []
            if i != roll:
                nt.append(i)
            while len(nt)  < 3:
                nt.append(0)
        j2[placement-1] = nt
        
    
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

    return (j1,j2)

    




def duel():
    j1 = [[0,0,0],[0,0,0],[0,0,0]]
    j2 = [[0,0,0],[0,0,0],[0,0,0]]
    win = False
    print("Bienvenue ! Vous avez choisi le mode duel (1 contre 1).")
    p = choixnom()
    while not win : 
        print("Au tour de" ,p[0], " .")
        roll = de()
        print("Vous avez eu un " , roll, " .")
        placement = int(input("Ou voulez vous placer le dé , Colonne 1,2, ou 3?"))
        a = placementj1(j1,j2,placement,roll)
        j1 = a[0]
        j2 = a[1]
        
        affichage(p,roll,0,j1,j2)
        print("Au tour de" ,p[1], " .")
        roll = de()
        print("Vous avez eu un " , roll, " .")
        placement = int(input("Ou voulez vous placer le dé , Colonne 1,2, ou 3?"))
        a = placementj1(j2,j1,placement,roll)
        j2 = a[0]
        j1 = a[1]
        affichage(p,0,roll,j1,j2)

        





duel()
    



    