class Cellule:
    
    def __init__(self, tete, queue):
        self.t = tete
        self.q = queue
        
class Liste:
    
    def __init__(self, c):
        # crée une liste
        self.cellule = c
        
    def estVide(self):
        # teste si la liste est vide ou non
        return self.cellule is None
    
    def car(self):
        # renvoie la tête de la liste
        assert(not(self.cellule is None)), 'Liste vide'
        return self.cellule.t
    
    def cdr(self):
        # renvoie la queue de la liste
        assert(not(self.cellule is None))
        return self.cellule.q 
    
    def cons(self, e):
        # ajoute un élément en tête de la liste
        return Liste(Cellule(e, self))
    

def lengthList(L):
    if L.estVide():
        return 0
    else:
        return 1 + lengthList(L.cdr())

def displayList(L):
    if L.estVide():
        return None
    else:
        print(L.car())
        return displayList(L.cdr())

def removeList(L):
    return (L.car(),L.cdr())


if __name__ == "__main__":  #utiliser cette syntaxe pour que le code qui suit ne s'exécute que quand ce fichier est le fichier principal
    nil = Liste(None)
    L = nil.cons(5).cons(4).cons(3).cons(2).cons(1)
    
    print(L.estVide())
    print("Premier élément :", L.car())
    print("Deuxième élément :", L.cdr().car())
    print("Troisième élément :", L.cdr().cdr().car())
    print("Dernier élément :", L.cdr().cdr().cdr().cdr().car())
    
    print("------------------")
    print("Longueur de la liste :", lengthList(L))
    print("Contenu de la liste :")
    displayList(L)
    
    print("------------------")
    t,L = removeList(L)
    print("Elément supprimé :", t)
    print("Ce qu'il reste dans la liste :")
    displayList(L)