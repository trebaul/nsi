class File:
    ''' Définition d'une classe File
    une instance File est crée avec une liste Python '''
    
    def __init__(self):
        "Initialisation d'une pile vide"
        self.L = []
        
    def estVide(self):
        "Teste si la file est vide"
        return self.L == []
    
    def defiler(self):
        "Défile : enlève le premier élément"
        assert( not(self.estVide()) ), "File vide !"
        return self.L.pop(0)
    
    def enfiler(self,x):
        "Enfile : ajoute un élément à la fin"
        self.L.append(x)
        
    def afficher(self):
        l = []
        for i in range(len(self.L)):
            l.append(self.L[i])
        return l
        
    def taille(self):
        return len(self.L)
    
    def sommet(self):
        return self.L[0]
    
