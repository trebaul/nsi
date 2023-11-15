from File import File


def croisement(f1,f2):
    '''
    Entrées :
        f1 : structure de file contenant des 0 ou des 1, représentant la présence ou non d'une voiture sur la route R1.
        f2 : structure de file contenant des 0 ou des 2, représentant la présence ou non d'une voiture sur la route R2.
        
    Sortie :
        f3 : structure de file contenant des 0, des 1 ou des 2, représentant l'origine des voitures sur la route R3.
    '''
    
    f3 = File()
    
    while (not(f1.estVide()) and not(f2.estVide())):
        if f1.sommet() == 0 and f2.sommet() == 0:
            f3.enfiler(f1.defiler())
            f2.defiler()
        elif f1.sommet() == 1 and f2.sommet() == 2:
            f3.enfiler(f1.defiler())
        elif f1.sommet() == 1 and f2.sommet() == 0:
            f3.enfiler(f1.defiler())
            f2.defiler()
        elif f1.sommet() == 0 and f2.sommet() == 2:
            f3.enfiler(f2.defiler())
            f1.defiler()
        else:
            print("Chiffre non valide.")
            
    if f1.estVide():
        while not(f2.estVide()):
            f3.enfiler(f2.defiler())
    else:
        while not(f1.estVide()):
            f3.enfiler(f1.defiler())
            
    return f3
            
            
f1=File()
f1.enfiler(0)
f1.enfiler(1)
f1.enfiler(1)
f1.enfiler(0)
f1.enfiler(1)
print(f1.afficher())

f2=File()
f2.enfiler(0)
f2.enfiler(0)
f2.enfiler(2)
f2.enfiler(2)
f2.enfiler(2)
f2.enfiler(0)
f2.enfiler(2)
f2.enfiler(0)
print(f2.afficher())

f3 = croisement(f1,f2)
print(f3.afficher())