<style>
body {
text-align: justify}
</style>

# **Séquence 4**
# III. Les dictionnaires

---

## Cours


### A. Définition

> Les **dictionnaires** ou **tableaux associatifs** sont des structures de données non-linéaires, où des **valeurs** sont associées à des **clés**. 

![](img/dico_extrait.jpg)

### B. Type abstrait

Les opérations primitives pouvant être faites sur les dictionnaires sont les suivantes :  
- *ajout* d'une nouvelle valeur à une nouvelle clé,  
- *modification* de la valeur associée à une clé existante,  
- *suppression* d'une clé et de la valeur associée,  
- *recherche* de la valeur associée à une clé.   

Ils sont implémentés directement en Python avec le type `dict`. 

***Rappels :*** 

1. Comment vous pouvez effectuer les opérations primitives sur un dictionnaire Python, noté `d` ? Commencer par créer un dictionnaire vide.
```python
d = {}
d[cle] = v1   #ajout d'une nouvelle valeur à une nouvelle clé
d[cle] = v2   #modification de la valeur associée à cle
d.pop(cle)  #supprime cle et sa valeur associée
print(d['cle'])  #recherche de la valeur associée à cle
```

2. Avec quelle méthode accède-t-on à la liste des clés de `d` ? A la liste de ses valeurs ?  
***`d.keys()` et `d.values()` donnent respectivement la liste des clés et des valeurs.***

3. Comment peut-on afficher l'ensemble des clés et des valeurs associées, en parcourant `d` ?
```python
for cle in d:
    print(cle, d[cle])

d.items()  #donne la liste des couples
```

### C. Accès à un élément

L'**accès à un élément** dans un tableau associatif s'effectue, comme dans un tableau, en **temps constant**. Il est indépendant de la taille de la structure. 

L'implémentation  d'un dictionnaire est en effet faite grâce à une table de hachage *(hors programme)* qui associe à chaque couple clé-valeur un indice du tableau.

<br>

***Exercice :*** 

1) Écrire en Python une fonction `tabToDict` qui prend en paramètre d’entrée une liste Python de la forme [clé1, valeur1, clé2, valeur2,…] et retourne un dictionnaire correspondant de la forme { clé1 : valeur1, clé2 : valeur2,…}.

***Correction :***
```python
def tabToDict(t):
    d = {}
    for i in range(0, len(t), 2):
        d[t[i]] = t[i+1]
    return d
```

2) Réciproquement, écrire une fonction en Python `dictToTab` qui permet de passer d'un dictionnaire à une liste.

***Correction :***
```python
def dictToTab(d):
    l = []
    for c in d.keys():
        l.append(c)
        l.append(d[c])
    return l
```