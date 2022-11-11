<style>
body {
text-align: justify}
</style>

# **Séquence 2**
# III. Les flottants

---

## Cours


En informatique, les nombres réels sont représentés par des **flottants**. Pourquoi ne pas utiliser le même nom, comme pour les entiers ? Nous allons voir que ces deux ensembles ne sont pas tout à fait équivalents... 

### Introduction

- Que doit, a priori, renvoyer le test `0.1 + 0.2 == 0.3` ?  ***Il devrait renvoyer `True`.***  
- Que renvoie-t-il en fait ? ***Il renvoie `False`.***  
- Quelle est en fait la valeur de `0.1 + 0.2` ? ***Sa valeur est `3.0000...00004`***  
Comprenons ce qu'il s'est passé...

### A. Décomposition et conversion de la base 2 à la base 10

Prenons le nombre $3.375$. On sait écrire sa partie avant la virgule en binaire (qui vaut $11_2$). Sa partie après la virgule, on peut la décomposer dans la base 10, comme on l'a fait pour la partie entière :

$0.375 = 3*10^{-1} + 7*10^{-2} + 5*10^{-3}$

Les rangs des puissances de 10 sont ici négatifs (-1, -2 et -3).
De la même façon, un nombre à virgule écrit en binaire se décompose en fonction de 2 à la puissance son rang :

$10.011_2 = 1*2^1+1*2^{-2}+2^{-3} = 2+0.25+0.125 = 2.380$

### B. Conversion de la base 10 à la base 2

> Conversion de la **partie décimale** d'un nombre réel de la base 10 à la base 2
> 1. On multiplie cette partie par 2. 
> 2. La partie entière de ce produit donne le premier coefficient après la virgule.
> 2. On garde la partie décimale du produit. On réitère l'algorithme avec cette valeur, jusqu'à ce qu'elle devienne **nulle**.

***Exemples :*** 
- Remplir le tableau suivant, pour obtenir la conversion de $0.375$. $3.375_{10} = 11.011_2$

| Multiplication par 2 de la partie décimale | Partie entière du produit | Partie décimale du produit |
| :-----: | :-----: | :-----: |
| $0.375*2=0.750$ | $0$ | $0.750$|
| $0.750*2=1.500$ | $1$ | $0.5$ |
| $0.5*2=1$ | $1$ | $0$ |

- Trouver la représentation binaire de $0.25_{10}$.

| Multiplication par 2 de la partie décimale | Partie entière du produit | Partie décimale du produit |
| :-----: | :-----: | :-----: |
| $0.25*2=0.5$ | $0$ | $0.5$ |
| $0.5*2=1$ | $1$ | $0$ |

- Que se passe-t-il lorsque l'on veut convertir la fraction $1/3$, qui a une écriture infinie en décimal ? ***L'algorithme ne se termine pas.***

| Multiplication par 2 de la partie décimale | Partie entière du produit | Partie décimale du produit |
| :-----: | :-----: | :-----: |
| $1/3*2=2/3$ | $0$ | $2/3$ |
| $2/3*2=4/3$ | $1$ | $1/3$ |

- Ecrire les 5 premières étapes de la conversion de $0.1_{10}$.

| Multiplication par 2 de la partie décimale | Partie entière du produit | Partie décimale du produit |
| :-----: | :-----: | :-----: |
| $0.1*2=0.2$ | $0$ | $0.2$ |
| $0.2*2=0.4$ | $0$ | $0.4$ |
| $0.4*2=0.8$ | $0$ | $0.8$ |
| $0.8*2=1.6$ | $1$ | $0.6$ |
| $0.6*2=1.2$ | $1$ | $0.2$ |

Que se passe-t-il ? Que peut-on en déduire sur la représentation de $0.1_{10}$ dans la machine ? Pourquoi le test `0.1 + 0.2 == 0.3` renvoie-t-il `False` ?  
***L'algorithme ne s'arrête pas. 0.1 ne peut pas être représenté de manière exacte, donc 0.1+0.2 ne fait pas exactement 0.3 avec la représentation de la machine.***


### D. La norme IEEE 754 *(son détail n'est pas à retenir)*

Le terme `flottant` vient du fait que l'on représente ces nombres avec une **virgule flottante**. La norme IEEE 754 est la plus employée pour représenter ces nombres. On utilise soit 32 *(version utilisée ici pour l'exemple)*, soit 64 bits pour stocker ces nombres. Le nombre est mis sous la forme : $signe*mantisse*base^{exposant}$, et on stocke :
- son **signe** *(1 bit)*,
- un **exposant** *(8 bits)*,
- une **mantisse** *(23 bits)*.

***Exemple :*** $4,3125_{10}=100,0101_2$, qui doit être transformé pour correspondre à cette norme, en $1,000101.2^2$.  
Il est stocké sous la forme : $signe = 0$ (nombre positif), $exposant = 10000001$ (l'exposant est décalé), $mantisse = 0001010000000000000000$



### Conclusion

En programmation, est-il pertinent de tester l'égalité entre deux flottants ? Comment peut-on faire alors ?  
***Ce n'est pas pertinent, car on peut avoir des erreurs dues à l'approximation de la représentation, contrainte par un nombre de bits donnés. On peut, à la place, tester si ces nombres sont suffisamment proches.***

