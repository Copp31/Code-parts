from labyrinthe import Labyrinthe


# Initialisation du nombre de colonnes et de rangées
largeur: int = 8
hauteur: int = 8

# Initialisation de la position de départ
point_depart_x: int = 0
point_depart_y: int = 0

labyrinthe = Labyrinthe(largeur, hauteur, point_depart_x, point_depart_y)
labyrinthe.generate()

print(labyrinthe)
