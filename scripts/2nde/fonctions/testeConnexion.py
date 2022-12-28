def testeConnexion(identifiant, motDePasse):
        if identifiant == "eleveSNT" and motDePasse == "Mprx24$":
            autorisee = True
        else:
            autorisee = False
        return autorisee
    
resultat1 = testeConnexion("eleveSNT", "mot")
resultat2 = testeConnexion("SNT", "Mprx24$")
resultat3 = testeConnexion("eleveSNT", "Mprx24$")
print("Premier test :", resultat1)
print("Deuxième test :", resultat2)
print("Troisième test :", resultat3)