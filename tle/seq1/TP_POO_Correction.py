from random import randint


# Définition des classes

class Personnage:
    def __init__(self, n, v, e):
        self.nom = n
        self.vie = v
        self.exp = e

    def perd_vie(self, pts_perdus):
        if pts_perdus < self.vie:
            self.vie = self.vie - pts_perdus
        else:
            self.vie = 0

    def donne_etat(self): 
        return self.vie
    
    def gagne_exp(self, e):
        self.exp = self.exp + e
        
    def donne_exp(self):
        return self.exp

    

# Programme principal

geralt = Personnage("geralt",40,42)
monstre = Personnage("monstre",40,11)
attaquant = geralt
defenseur = monstre

while attaquant.vie>0 and defenseur.vie>0:
    
    if attaquant.donne_exp() > 40:
        perte_infligee = randint(5,10)
    else:
        perte_infligee = randint(0,5)
    defenseur.perd_vie(perte_infligee)
    
    tmp = attaquant
    attaquant = defenseur
    defenseur = attaquant
    
if attaquant.donne_etat()<=0:
    print(defenseur.nom + " a gagné !")
else:
    print(attaquant.nom + " a gagné !")

