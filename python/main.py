from labyrinthe import Labyrinthe

"""
Voici mon projet labyrinthe. Il fonctionne et produit un graph très bien. 

La grosse lacune de mon projet est la section test... j'y ai laissé un commentaire. 

Forte inspiration du projet : https://scipython.com/blog/making-a-maze/

    Coppélia

"""

# Initialisation du nombre de colonnes et de rangées
largeur: int = 8
hauteur: int = 8

# Initialisation de la position de départ
point_depart_x: int = 0
point_depart_y: int = 0

labyrinthe = Labyrinthe(largeur, hauteur, point_depart_x, point_depart_y)
labyrinthe.generate()

print(labyrinthe)
