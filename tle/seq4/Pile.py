
class Pile:
    ''' Définition d'une classe Pile
    une instance Pile est créée avec une liste Python '''
    
    def __init__(self):
        "Initialisation d'une pile vide"
        self.L = []
        
    def estVide(self):
        "Teste si la pile est vide"
        return self.L == []
    
    def depiler(self):
        "Dépile : enlève le dernier élément"
        assert( not(self.estVide()) ), "Pile vide !"
        return self.L.pop()
    
    def empiler(self,x):
        "Empile : ajoute un élément à la fin"
        self.L.append(x)
        
    def afficher(self):
        l = []
        for i in range(len(self.L)):
            l.append(self.L[i])
        return l
