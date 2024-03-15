découpage...
Algorithme de fonctionnement du jeu :
Créer une grille 2D avec des bonbons placés aléatoirement, mais qui permette un mouvement. 
Afficher la grille 2D 
Répéter jusqu'a ce qu'aucun mouvement ne puisse faire disparaitre des bonbons ( i.e. l'échange des bonbons est possible ) :
  Demander au joueur les positions des bonbons qu'il veut échanger
  Echanger les position des bonbons
  Répéter jusqu'à ce que les positions des bonbons ne respectent plus les règles de disparition des bonbons :
    Faire disparître les bonbons alignés. 
    Actualiser la grille 
    Afficher la grille  

Découpage fonctionnel :
def detecte_coordonnees_combinaison(grille, i, j):
"""
Renvoie une liste contenant les coordonnées de tous les bonbons
appartenant à la combinaison du bonbon (i, j).
"""


def affichage_grille(grille, nb_type_bonbons):
"""
Affiche la grille de jeu "grille" contenant au
maximum "nb_type_bonbons" couleurs de bonbons différentes.
"""
plt.imshow(grille, vmin=0, vmax=nb_type_bonbons−1, cmap=’jet’)
plt.pause(0.1)
plt.draw()
plt.pause(0.1)
""" 

def test_detecte_coordonnees_combinaison():
"""
Test la fonction detecte_coordonnees_combinaison(grille, i, j).
Pour chaque cas de test, affiche True si le test passe,
False sinon
"""
