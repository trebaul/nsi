"""
Résolution du problème des tours de Hanoï.
Adapté de Stephan Van Zuijlen, isn-icn-ljm.pagesperso-orange.fr
@author: Trebaul-NSI
"""

def affichage(tours):
    d = len(tours['départ'])
    i = len(tours['intermédiaire'])
    a = len(tours['arrivée'])
    hauteur = max(d, i, a)
    
    for h in range(hauteur, 0, -1):
        if d >= h:
            print( tours['départ'][h-1], end = ' ')
        else:
            print(' ', end = ' ')
        if i >= h:
            print( tours['intermédiaire'][h-1], end = ' ')
        else:
            print(' ', end = ' ')
        if a >= h:
            print( tours['arrivée'][h-1])
        else:
            print( ' ')
            
    print('\u2AE0 \u2AE0 \u2AE0')
    print('-------------------------------')
    
    
def Hanoi(n, dep = 'départ', inter = 'intermédiaire', arr='arrivée'):
    """ Spécification à écrire """
    if n == 0:
        return None
    else:
        #à compléter : 1ere étape
        #à compléter : 2ème étape
        anneau_deplace = tours[dep].pop()
        tours[arr].append(anneau_deplace)
        affichage(tours)
        #à compléter : 3ème étape
        
        
n = 5
tours = dict()
tours['départ'] = [j for j in range(n,0,-1)]
tours['intermédiaire'] = []
tours['arrivée'] = []
Hanoi(n)