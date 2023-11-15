def listeCree():
    return None

def listeEstVide(l):
    return l == None

def listeAjoute(x,l):
    return (x,l)

def listeTete(l):
    return l[0]

def listeQueue(l):
    return l[1]

def elementiListe(L, i):
    if i == 1:
        return listeTete(L)
    else:
        return elementiListe(listeQueue(L),i-1)
    
def listeAffiche(L):
    if listeEstVide(L):
        print("")
    else:
        print(listeTete(L))
        listeAffiche(listeQueue(L))
    
def listeCompte(L):
    if listeEstVide(L):
        return 0
    else:
        return 1+listeCompte(listeQueue(L))
    
# Question 1
L = listeCree()
assert listeEstVide(L) == True
for i in range(1,5):
    L = listeAjoute(i, L)
assert listeEstVide(L) == False

# Question 4
L = listeAjoute(5, L)
print("Nombre d'éléments :", listeCompte(L))
listeAffiche(L)
L = listeQueue(L)
print("Nombre d'éléments :", listeCompte(L))
listeAffiche(L)

