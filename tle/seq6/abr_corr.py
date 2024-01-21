
class ABR:
    def __init__(self, racine):
        self.racine = racine
        
    def affiche_abr(self):
        if self is None:
            representation = "L'arbre est vide !"
        else:
            representation = self.racine.affiche()
        return representation
    
    def recherche_abr(self, element):
        return self.racine.rechercher(element)
            
    def insere_abr(self, element):
        self.racine.inserer(element)
        
        

class Noeud:
    def __init__(self, valeur, fils_gauche, fils_droit):
        self.valeur = valeur
        self.fils_gauche = fils_gauche
        self.fils_droit = fils_droit
        
    def affiche(self, space = 0):
        spaces = "  "*space
        print(spaces, self.valeur)
        if self.fils_gauche:
            self.fils_gauche.affiche(space+1)
        if self.fils_droit:
            self.fils_droit.affiche(space+1)
            
    def rechercher(self, cle):
        if cle == self.valeur:
            return True
        elif cle < self.valeur:
            if self.fils_gauche == None:    # s'il n'y a rien à gauche, la clé n'est pas présente
                return False
            else:
                return self.fils_gauche.rechercher(cle)   # on continue de chercher à gauche
        elif cle > self.valeur:
            if self.fils_droit == None:     # s'il n'y a rien à droite, la clé n'est pas présente
                return False
            else:
                return self.fils_droit.rechercher(cle)    # on continue de chercher à droite
        
    def inserer(self, cle):
        if cle <= self.valeur:
            if self.fils_gauche == None:   # le fils est vide, on peut faire l'insertion ici
                self.fils_gauche = Noeud(cle, None, None)
            else:	# on cherche une place pour faire l'insertion à gauche
                self.fils_gauche.inserer(cle)
        elif cle > self.valeur:
            if self.fils_droit == None:    # le fils est vide, on peut faire l'insertion ici
                self.fils_droit = Noeud(cle, None, None)
            else:   # on cherche une place pour faire l'insertion à droite
                self.fils_droit.inserer(cle)
                
    

if __name__ == "__main__":    # ne s'exécute qu'en tant que fichier principal, pas si la classe est importée dans un autre fichier
    n19 = Noeud(19, None, None)
    n17 = Noeud(17, None, n19)
    n11 = Noeud(11, None, None)
    n13 = Noeud(13, n11, n17)
    n5 = Noeud(5, None, None)
    n2 = Noeud(2, None, None)
    n3 = Noeud (3, n2, n5)
    n9 = Noeud (9, n3, n13)
    a = ABR(n9)