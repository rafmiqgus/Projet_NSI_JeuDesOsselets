import random
def de():
    return random.randint(1,6)

def affichage(p,de1,de2,j1,j2,s1,s2):
    tempa = (8 - len(p[0]) )* " "
    tempb = (8 - len(p[1]) )* " "
    t1 = s1[0]+s1[1]+s1[2]
    te1 = (3 - len(str(t1))) * " "
    se1 = (3 - len(str(s1))) * " "
    t2 = s2[0]+s2[1]+s2[2]
    te2 = (3- len(str(t2))) * " "
    se2 = (3 - len(str(s2))) * " "
    print("__________________________________________________________________________________________")
    print("|                                                                                        |")
    print("|  ",p[0],tempa,"                         |",j1[0][2],"||",j1[1][2],"||",j1[2][2],"|               ",de1,"                 |")
    print("|   score :                              ‾    ‾    ‾                                     |")
    print("|    ",t1,te1,"                            |",j1[0][1],"||",j1[1][1],"||",j1[2][1],"|                                   |")
    print("|                                        ‾    ‾    ‾                                     |")
    print("|                                      |",j1[0][0],"||",j1[1][0],"||",j1[2][0],"|                                   |")
    print("|                                        ‾    ‾    ‾                                     |")
    print("|                                       ",s1[0],"  ",s1[1],"  ",s1[2],"                                    |")
    print("|                                                                                        |")
    print("|                                                                                        |")
    print("|  ",p[1],tempb,"                         |",j2[0][2],"||",j2[1][2],"||",j2[2][2],"|               ",de2,"                 |")
    print("|   score :                              ‾    ‾    ‾                                     |")
    print("|    ",t2,te2,"                            |",j2[0][1],"||",j2[1][1],"||",j2[2][1],"|                                   |")
    print("|                                        ‾    ‾    ‾                                     |")
    print("|                                      |",j2[0][0],"||",j2[1][0],"||",j2[2][0],"|                                   |")
    print("|                                        ‾    ‾    ‾                                     |")
    print("|                                       ",s2[0],"  ",s2[1],"  ",s2[2],"                                    |")
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
def check(desj1,desj2,colonne):
    a = False
    for k in desj1[colonne-1]:
        if k in desj2[colonne-1]:
            a = True 
    return a 
def placementj1(j1,j2,placement,roll):
    while j1[placement-1][2] != 0:
        print("colonne remplie ! choisissez en une autre.")
        placement = int(input("Quelle colonne voulez vous choisir ?"))
    while placement not in [1,2,3]:
        print("Cet entrée n'est pas valide. Entrez 1,2 ou 3.")
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
    if check(j1,j2,placement):
        nt = []
        for i in j2[placement-1]:
            if i != roll:
                nt.append(i)
        while len(nt)  < 3:
            nt.append(0)
        j2[placement-1] = nt
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
        print(occ)
        if occ == []:
            sum = 0
        elif len(occ) == 1:
            sum = nbr**3
        elif len(occ) == 2:
            if nbr == occ[0]:
                sum = occ[0]**2 + occ[1]
            elif nbr == occ[1]:
                sum = occ[1]**2 + occ[0]
        else:
            sum = k[0] + k[1] + k[2]
        result.append(sum)
        
    
    return result


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
        if checkover(j1,j2):
            win = True
        affichage(p,roll,0,j1,j2,sumdes(j1),sumdes(j2))
        print("Au tour de" ,p[1], " .")
        roll = de()
        print("Vous avez eu un " , roll, " .")
        placement = int(input("Ou voulez vous placer le dé , Colonne 1,2, ou 3?"))
        a = placementj1(j2,j1,placement,roll)
        j2 = a[0]
        j1 = a[1]
        if checkover(j2,j1):
            win = True
        affichage(p,0,roll,j1,j2,sumdes(j1),sumdes(j2))
    print("Jeu terminé.")
        
duel()
    



    