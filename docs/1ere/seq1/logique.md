

<style>
body {
text-align: justify}
</style>

# **Séquence 1**
# I. La logique booléenne

## Cours

### Introduction

L'informatique est basée sur l'utilisation de `1` et de `0` : ils représentent le vrai et le faux, `True` et `False` en Python, et correspondent au type **booléen**. Nous avons vu que les **expressions booléennes** permettent de différencier différents cas dans un programme.

Nous avons vu des opérateurs qui permettent de comparer des nombres (`int` ou `float`), et renvoient des booléens (`bool`). Pour combiner ces expressions booléennes, on utilise des **opérateurs booléens**. 

Passons en revue ces opérateurs, en considérant le ***problème*** suivant :

![sphinx](img/sphinx_desert.jpg)

> Au milieu du désert, deux sphinx gardent chacun une porte. Une des deux portes continue dans le désert, l'autre mène vers une oasis. L'un des deux sphinx dit toujours la vérité, l'autre ment toujours. On veut savoir par où aller pour accéder à l'oasis.

---
### I.A. Le NON (NOT)

L'opérateur NON (NOT en anglais) inverse la valeur d'une **variable booléenne**. Si `A` vaut `False`, non(`A`) vaut `True` et réciproquement. On résume cela avec une table, dite **table de vérité** de l'opérateur NON :

| `A` | NON(`A`) |
| :--------------- | :--------------- |
| `False` | `True` |
| `True` | `False` |

La table de vérité d'une **expression booléenne** indique la valeur de l'expression pour chaque valeur possible de ses variables.

> Application au ***problème*** : On veut demander l'information, si l'on s'adresse à celui qui dit la vérité - donc à celui qui ne ment pas. On utilise une variable booléenne `menteur` qui vaut `True` si le sphinx auquel on s'adresse ment, `False` s'il dit la vérité :

```python
if not(menteur):
    print("Pouvez-vous m'indiquer l'oasis ?")
```


### I.B. Le ET (AND)

L'opérateur ET (AND en anglais) permet d'associer deux expressions booléennes de la manière suivante : A ET B est vrai si A est vraie et B est vraie. Cela donne la table de vérité suivante :

| `A` | `B` | `A` ET `B` |
| :---------------: |:---------------:|:---------------:|
| `False` | `False` | `False` |
| `True` | `False` | `False` |
| `False` | `True` | `False` |
| `True` | `True` | `True` |

> Application au ***problème*** : Si le sphinx auquel on s'adresse n'est pas un menteur *et* s'il nous dit qu'il se trouve devant la porte menant à l'oasis, on veut prendre ce chemin. On utilise une variable `porte` valant `True` si le sphinx dit qu'elle mène à l'oasis, `False` sinon :

```python
if not(menteur) and porte:
    print("Je prends ce chemin.")
```

### I.C. Le OU (OR)

L'opérateur OU (OR en anglais) permet d'associer deux expressions booléennes de la manière suivante : A OU B est vrai si A est vraie, B est vraie, ou bien les deux le sont. Cela donne la table de vérité suivante :

| `A` | `B` | `A` OU `B` |
| :---------------: |:---------------:|:---------------:|
| `False` | `False` | `False` |
| `True` | `False` | `True` |
| `False` | `True` | `True` |
| `True` | `True` | `True` |

> Application au ***problème*** : Si le sphinx auquel on s'adresse n'est pas un menteur et s'il nous dit qu'il se trouve devant la porte menant à l'oasis *ou* s'il est un menteur et qu'il nous dit que la porte continue dans le désert, on veut prendre ce chemin.

```python
if (not(menteur) and porte) or (menteur and not(porte)):
    print("Je prends ce chemin.")
```
<div style="page-break-after: always; visibility: hidden"> 
\pagebreak 
</div>

### I.D. Le OU exclusif (XOR)

L'opérateur OU EXCLUSIF (XOR en anglais) permet d'associer deux expressions booléennes de la manière suivante : A OU B est vrai si A est vraie ou bien B est vraie. Cela donne la table de vérité suivante :

| `A` | `B` | `A` OU `B` |
| :---------------: |:---------------:|:---------------:|
| `False` | `False` | `False` |
| `True` | `False` | `True` |
| `False` | `True` | `True` |
| `True` | `True`  | `False` |

> Application au ***problème*** : Si le sphinx auquel on s'adresse est un menteur *ou (exclusif)* s'il nous dit qu'il ne se trouve pas devant la porte menant à l'oasis (et donc qu'il ne ment pas), on ne veut pas prendre ce chemin.

```python
from operator import xor

if xor(menteur,not(porte)):
    print("Je ne prends pas ce chemin.")
```
**N.B.** : L'utilisation de cette fonction n'est pas à apprendre par coeur. 


### Conclusion

Une bonne utilisation des opérateurs booléens permet notamment de mieux gérer les différentes conditions traitées dans les programmes. La logique booléenne trouve aussi des applications dans la conception de circuits électroniques.

> Nous ne savons en fait pas quel sphinx ment et lequel dit la vérité. Nous n'avons le droit de ne poser qu'une question à un des deux sphinx pour savoir où aller. Laquelle devons-nous choisir pour aller à coup sûr vers l'oasis ?

![sphinx](img/sphinx_statue.jpg)

<br>

---

## Exercices : les expressions booléennes 

### Exercice 0 *(amélioration du TP sur les fonctions)* :
On dispose d'une fonction `pair(n)`, renvoyant si un entier `n` est pair ou non :
```python
def pair(n):
    return n%2 == 0
```
On considère une variable `m` représentant un mois de l'année.

1. Quelle instruction écrire pour tester "m est-t-il impair" ?

2. Ecrire le programme Python traduisant l'algorithme suivant :
```python
Si n est impair et qu il est un mois de la fin de l année
	nb_jours vaut 30
```
3. Faire la même chose avec l'algorithme suivant :
```python
Si n est pair et qu il est un mois du début de l année
	nb_jours vaut 30
```
4. Comment combiner les conditions des questions 2 et 3 ?

5. Compléter la fonction suivante, permettant de tester tous les mois de l'année :
```python
def nombre_jours(m):
    if m == 2:
        nb = 28
    elif ...
        nb = 30
    ...

    return nb
```


### Exercice 1 : Vrai ou Faux

1. Si `a` vaut `True` et `b` vaut `False`, `not(a or b)` s'évalue à `True`.

2. L'expression `not(a or b)` a la même valeur que l'expression `(not a) or (not b)`.

3. Si `a` vaut `True` et `b` vaut `True`, `not(a and b)` s'évalue à `True`.

4. L'expression `not(a and b)` a la même valeur que l'expression `not(a) or not(b)`.

### Exercice 2 : 
Sélectionner la(les) bonne(s) réponse(s) parmi les différentes propositions.

1. L'expression booléenne `a or not(b)` s'évalue à `True`. Quelles peuvent être les valeurs de `a` et de `b` ?
    - `a` vaut `True` et `b` vaut `True`
    - `a` vaut `True` et `b` vaut `False`
    - `a` vaut `False` et `b` vaut `True`
    - `a` vaut `False` et `b` vaut `False`

2. Parmi les expressions suivantes, laquelle s'évalue en `True` ?
    - `True and (False and True)`
    - `True or (False and True)`
    - `False and (False and True)`
    - `False or (False and True)`


### Exercice 3 :
1. On considère l'expression `a and b` où `a` et `b` sont deux expressions booléennes. Si `a` vaut `False`, quelle sera la valeur de l'expression, en fonction de la valeur de `b` ? Que pouvez-vous en déduire ?
<br><br><br>

2. On considère l'expression `a or b` où `a` et `b` sont deux expressions booléennes. Si `a` vaut `True`, quelle sera la valeur de l'expression, en fonction de la valeur de `b` ? Que pouvez-vous en déduire ?
<br><br><br>

**Conclusion** ***(à retenir)*** : 

<br>

---

## TD : Qui faut-il croire ?

### A. Un village perdu

Vous voyagez dans un endroit que vous ne connaissez pas, et demandez votre chemin à deux locaux que vous croisez. Vous souhaitez savoir où se trouve le village qui est votre objectif. Ils décident de jouer à un jeu avec vous : ils vont vous donner des informations, et soit toutes ces informations seront vraies, soit elles seront toutes fausses. 

![village](img/village.jpg)

En appliquant la logique booléenne, vous devez être capable d'obtenir l'information que vous recherchez.

Voici leurs propos :

> X : "Le village se trouve dans la vallée."  
Y : "Non, il ne s’y trouve pas."  
X : "Ou alors dans les collines."

On modélise le problème avec les variables suivantes : 
- `V` et `C` qui valent `True` si, respectivement, le village se trouve dans la vallée ou dans les collines, et `False` sinon, 
- `X` et `Y` qui valent `True` si respectivement les affirmations de X et de Y sont vraies, et `False` sinon.

1. Traduire `X` et `Y` en fonction de `V`, `C`, et des opérateurs booléens qui conviennent.
2. Compléter la table de vérité suivante (on part du principe que le village ne peut être que soit dans la vallée, soit dans la colline) :

| `V` | `C` | `X` | `Y` |
| :---------------: |:---------------:| :---------------:| :---------------:|
| `False` |  `True` | | |
| `True` | `False` |

3. En déduire où se trouve le village.

---
<div style="page-break-after: always; visibility: hidden"> 
\pagebreak 
</div>

### B. Au tribunal
Vous êtes dans le jury d'un tribunal et écoutez les témoins d'une enquête. On sait que chacun des témoins soit toujours dit la vérité, soit ment toujours. Notre but est d'identifier ceux qui mentent et ceux qui ne mentent pas pour prononcer le verdict le plus juste possible.

![juge.jpg](img/juge.jpg)


Les trois témoins s'expriment :  
> Ap : "Personne ne doit croire C."  
Bp : "A et C disent toujours la vérité."  
Cp : "B dit la vérité."

On modélise le problème avec les variables suivantes : `A`, `B` et `C` qui valent `True` si, respectivement, les témoins A, B et C disent la vérité, et `False` sinon.

1. Traduire Ap, Bp et Cp sous la forme d'expressions booléennes en utilisant les opérateurs appropriés.
2. Compléter la table de vérité suivante :

| `A` | `B` | `C` | `Ap` | `Bp` | `Cp` |
| :---------------: |:---------------:|:---------------:|:---------------:| :---------------:| :---------------:|
| `False` | `False` | `False` | | |
| `False` | `False` | `True` | | |
| `False` | `True` | `False` | | |
| `False` | `True` | `True` | | |
| `True` | `False` | `False` | | |
| `True` | `False` | `True` | | |
| `True` | `True` | `False` | | |
| `True` | `True` | `True` | | |

3. Comment pouvez-vous en déduire qui dit la vérité et qui ment ? 