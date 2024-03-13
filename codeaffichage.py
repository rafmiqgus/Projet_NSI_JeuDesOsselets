import random
def de():
    return random.randint(1,6)

def affichage(p):
    tempa = (8 - len(p[0]) )* " "
    tempb = (8 - len(p[1]) )* " "
    print("__________________________________________________________________________________________")
    print("|                                                                                        |")
    print("|  ",p[0],tempa,"                         | | | | | |                                       |")
    print("|   score :                             ‾   ‾   ‾                                        |")
    print("|                                      | | | | | |                                       |")
    print("|                                       ‾   ‾   ‾                                        |")
    print("|                                      | | | | | |                                       |")
    print("|                                       ‾   ‾   ‾                                        |")
    print("|                                                                                        |")
    print("|                                                                                        |")
    print("|                                                                                        |")
    print("|  ",p[1],tempb,"                         | | | | | |                                       |")
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
    print("Bienvenue ! Vous avez choisi le mode duel (1 contre 1).")
    p = choixnom()
    
    
duel()

    