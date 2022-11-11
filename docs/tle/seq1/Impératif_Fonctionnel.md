<style>
body {
text-align: justify}
</style>

# **Séquence 1**
# I. Les paradigmes impératif et fonctionnel
---

## Cours
### A. Les éléments de base de la programmation

```python
l = [2, 6, 9]
s = 0
if l[0]%2 == 0:
    s = s + l[0]
if l[1]%2 == 0:
    s = s + l[1]
if l[2]%2 == 0:
    s = s + l[2]
```
- Dans l'exemple ci-dessus, quels sont les éléments de base de la programmation utilisés ?  
***On identifie des affectations, des instructions conditionnelles. L'ensemble est une séquence d'instructions.***
- Que fait ce programme ?  
***Il calcule la somme des éléments pairs d'une liste Python.***
- Proposer une autre manière d'écrire ce programme. Quel autre élément de programmation est-il pertinent d'utiliser ici ?  
***Il est pertinent d'utiliser une boucle bornée.***
- Ecrire ce programme en utilisant deux fonctions intermédiaires.

>Il y a donc plusieurs manière de programmer un même algorithme, en utilisant différemment les éléments de programmation à notre disposition. Un **paradigme de programmation** est une manière de programmer spécifique.

### B. Le paradigme impératif

Le **paradigme impératif** est le paradigme le plus courant, utilisé par de nombreux langages de programmation comme Python *(qui intègre aussi d'autres paradigmes !)*. Il consiste à décrire un programme sous la forme de séquences d'instructions à effectuer dans un ordre précis. Les caractéristiques de ce paradigme sont :
- importance de l'ordre des instructions,
- utilisation d'affectations de variables, d'expressions conditionnelles et de boucles.

Cette manière de programmer est proche du fonctionnement de la machine et peut sembler la plus intuitive. 

Pourquoi utiliser d'autres paradigmes ?  
***On peut préférer d'autres manières de programmer en fonction du champ d'application du programme, du problème spécifique qui est traité, ou tout simplement des goûts du programmeur.***



### C. Le paradigme fonctionnel

Le **paradigme fonctionnel** est un paradigme rigoureux, permettant de plus facilement tester, déboguer et optimiser les programmes.

#### C.1. Les fonctions

Rappeler la syntaxe de définition et d'appel d'une fonction en Python :
```python
def nom_de_la_fonction(entree1,entree2):
    #séquence d'instructions
    (return sortie)

resultat = nom_de_la_fonction(val1, val2)
```

Le paradigme fonctionnel est centré, comme son nom l'indique,  sur l'utilisation de fonctions. Plus précisément, on utilise des **fonctions dites "pures"** : des fonctions qui, étant donné des paramètres d'entrée, renvoient toujours la même sortie. Pour cela, il ne faut pas qu'elles créent d'**effets de bord**.

#### C.2. Les effets de bord

> Un **effet de bord** correspond à la modification par une fonction d'une ou plusieurs variable(s) définie(s) en dehors de cette fonction.

> Une variable définie en dehors d'une fonction est une **variable globale**, utilisable dans tout le programme. Une variable définie dans une fonction est par défaut **locale** : elle n'existe que dans cette fonction.

***Exemple :***
```python
l = [0,1,2,3]
def remplace(x):
    y = l[0]
    l[0] = x
    return y
```
- Que fait cette fonction ? En écrire la spécification (description des entrées et sorties).  
***Cette fonction remplace la valeur du premier élement de `l` par une valeur donnée en entrée.  
Entrée : entier x remplaçant la valeur du premier élément de l  
Sortie : l'entier y en première position de la liste l avant d'être remplacé***

- Que renvoie l'appel de `remplace(1)` ? Un deuxième appel de `remplace(1)` ?  
***Le premier appel renvoie `0`, alors que le deuxième renvoie `1`.***

- Que peut-on en conclure ?  
***Il y a modification d'une variable définie en dehors de `remplace` : elle crée un effet de bord. La fonction, appelée plusieurs fois avec le même paramètre ne renvoie pas la même valeur : ce n'est pas une fonction pure.***

- Proposer une fonction "pure" effectuant le même traitement que `remplace`.
```python
def remplace(x, l):
    y = l[0]
    l[0] = x
    return y
```

**N.B. :**  une fonction pure renvoie toujours une valeur (sinon, vu qu'elle n'a pas d'effet de bord, elle ne servirait pas à grand chose...).


#### C.3. Les caractéristiques du paradigme fonctionnel

- utilisation de **fonctions imbriquées** (cf partie A),
- utilisation de **fonctions pures** (donc pas d'effet de bord !),
- on évite **l'affectation** de valeurs à des variables (utilisation de fonctions à la place).

Ces caractéristiques rendent les programmes plus fiables : différentes *bonnes pratiques de programmation* s'inspirent de cette manière de programmer.


<br>

---


## Exercices

### Exercice 1 : *(sur feuille)*
Dans les exemples suivant, indiquer :
- s'il y a un effet de bord ou non,
- si la fonction est pure,
- s'il y a un effet de bord, proposer une autre version de la fonction qui l'élimine.

1.
```python
i = 5
def f():
    return i>5
```
2.
```python
def ajout(i,l):
    tab = l + [i]
    return tab
```
3.
```python
x = 11
l = [1,3,5,7,9]
def ajoute():
    if x>l[-1]:
        l.append(x)
    return l
```

### Exercice 2 : *(sur feuille)*
Identifier les caractéristiques se rapportant au paradigme impératif, et celles se rapportant au paradigme fonctionnel.
- autorise les effets de bord,
- l'ordre des instructions n'a pas toujours d'importance,
- utilise des affectations de variables,
- utilise des boucles,
- découpe un programme en fonctions.


### Exercice 3 : *(sur ordinateur)*

Les codes suivant correspondent à des algorithmes vus en première.
- Ecrire chacun sous la forme d'une fonction, dont on aura identifié les *paramètres d'entrée et de sortie* et dont on choisira le *nom* de manière adéquate. On veut des fonctions pures, n'utilisant pas de variables globales.
- Renommer les variables pour que l'on comprenne plus facilement leur rôle.
- Ajouter les spécifications des entrées et des sorties.

1.
```python
x = 0
y = 0
l = [6,8,7,1,0]
for i in range(len(l)):
    if l[i]>x:
        x = l[i]
        y = i
print(x, y)
```
2.
```python
o = 0
t = [6,2,4,8,2,1,3]
for e in t:
    if e == 2:
        o = o+1
print(o)
```

