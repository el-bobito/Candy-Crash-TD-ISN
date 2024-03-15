# Main file of the project




def detecte_coordonnees_combinaison(grille, i, j):
    """
        Renvoie une liste contenant les coordonnées de tous les bonbons
        appartenant à la combinaison du bonbon (i, j).
    """
    valeur = grille[i][j]
    liste_coo = []
    longueur = len(grille)
    
    
    for l in range(longueur):
        for c in range(longueur):
            if grille[l][c] = valeur:
                liste_coo.append((l,c))
    
    return liste_coo
