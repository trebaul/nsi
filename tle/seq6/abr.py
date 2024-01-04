
class ABR:
    def __init__(self, racine):
        self.racine = racine
    
    def affiche_abr(self):
        if self is None:
            representation = "L'arbre est vide !"
        else:
            representation = self.racine.affiche()
        return representation
        

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
        