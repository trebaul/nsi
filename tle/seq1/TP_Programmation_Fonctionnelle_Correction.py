# TP Programmation Fonctionnelle

from functools import reduce

# Partie A.1. la fonction map

# question 2
liste_int = [0, 147, 1369874]
liste_str = list(map(str, liste_int))

# question 3 
liste_int = []
for e in liste_str:
    liste_int.append(int(e))
    
# Partie A.1. la fonction reduce

def minimum(a,b):
    if a<b:
        return a
    else:
        return b
    
mini = reduce(minimum,[0, 147, 1369874])

def mini_liste(l):
    mini = l[0]
    
    for i in range(len(l)):
        if l[i]<mini:
            mini = l[i]
    return mini

# Partie B Les fonctions anonymes

s = reduce(lambda x, y: x+y, [1,2,3,4,5,6,7,8,9])
