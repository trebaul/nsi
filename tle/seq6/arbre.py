class ArbreBinaire:
    def __init__(self, racine, agauche, adroit):
        self.racine = racine
        self.gauche = agauche
        self.droit = adroit
        
    def affiche(self, space = 0):
        spaces = "  "*space
        print(spaces, self.racine)
        if self.gauche:
            self.gauche.affiche(space+1)
        if self.droit:
            self.droit.affiche(space+1)
            
    def getRacine(self):
        return self.racine
    
    def getABGauche(self):
        return self.gauche
    
    def getABDroit(self):
        return self.droit
    
    def setRacine(self,r):
        self.racine = r
        
    def setABGauche(self,fg):
        self.gauche = fg
        
    def setABDroit(self,fd):
        self.droit = fd