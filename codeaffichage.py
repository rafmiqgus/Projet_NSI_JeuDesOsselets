import random
def de():
    return random.randint(1,6)

def affichage(p,de1,de2,j1,j2):
    tempa = (8 - len(p[0]) )* " "
    tempb = (8 - len(p[1]) )* " "
    print("__________________________________________________________________________________________")
    print("|                                                                                        |")
    print("|  ",p[0],tempa,"                         |",j1[0][2],"| | | | |               ",de1,"                     |")
    print("|   score :                             ‾   ‾   ‾                                        |")
    print("|                                      |",j1[0][1],"| | | | |                                       |")
    print("|                                       ‾   ‾   ‾                                        |")
    print("|                                      |",j1[0][0],"| | | | |                                       |")
    print("|                                       ‾   ‾   ‾                                        |")
    print("|                                                                                        |")
    print("|                                                                                        |")
    print("|                                                                                        |")
    print("|  ",p[1],tempb,"                         | | | | | |               ",de2,"                     |")
    print("|   score :                             ‾   ‾   ‾                                        |")
    print("|                                      | | | | | |                                       |")
    print("|                                       ‾   ‾   ‾                                        |")
    print("|                                      | | | | | |                                       |")
    print("|                                       ‾   ‾   ‾                                        |")
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




def duel():
    j1 = [[0,0,0],[0,0,0],[0,0,0]]
    j2 = [[0,0,0],[0,0,0],[0,0,0]]
    print("Bienvenue ! Vous avez choisi le mode duel (1 contre 1).")
    p = choixnom()
    print("Au tour de" ,p[0], " .")
    roll = de()
    print("Vous avez eu un " , roll, " .")
    placement = str(input("Ou voulez vous placer le dé , Colonne 1,2, ou 3?"))
    if placement == 1:
        if j1[0][0] == 0:
            j1[0][0]  = roll
        elif j1[0][1] == 0 and j1[0][0] != 0:
            j1[0][1]  = roll
        elif j1[0][2] == 0 and j1[0][1] != 0 and j1[0][0] != 0:
            j1[0][1]  = roll
    affichage(p,roll,0)





duel()
    



    