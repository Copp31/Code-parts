import random
import graphviz
from cellule import Cellule


class Labyrinthe:
    """
    Un labyrinthe est initialement une grille de cellules avec tous leurs murs
    
    """

    def __init__(self, largeur: int, hauteur: int, point_depart_x: int = 0, point_depart_y: int = 0):
        """
        Dans un labyrinthe, il y a largeur * hauteur (selon l'initialisation dans main.py)
        Le départ du labyrinthe se trouve à ix et iy (selon l'intialisation dans le main.py)

        """

        self.largeur: int = largeur
        self.hauteur: int = hauteur
        self.point_depart_x: int = point_depart_x
        self.point_depart_y: int = point_depart_y
        self.creation_grille: list = [[Cellule(x, y) for y in range(hauteur)] for x in range(largeur)]

    def position_cellule(self, position_x: int, position_y: int):
        """
        Information sur la position de la cellule concernée
        
        """

        return self.creation_grille[position_x][position_y]

    def recherche_voisin_valide(self, cellule: Cellule):
        """
        Méthode qui permet d'implémenter dans une liste les voisins de la cellule concernée qui n'ont pas encore 
        été visité (donc qui ont tous leurs murs).
        
        """

        situation: list = [('droite', (-1, 0)),
                           ('gauche', (1, 0)),
                           ('bas', (0, 1)),
                           ('haut', (0, -1))]

        voisins: list = []

        for direction, (direction_x, direction_y) in situation:

            voisin_x: int = cellule.x + direction_x
            voisin_y: int = cellule.y + direction_y

            if (0 <= voisin_x < self.largeur) and (0 <= voisin_y < self.hauteur):
                voisin: list = self.position_cellule(voisin_x, voisin_y)

                if voisin.aucune_porte_ouverte():
                    voisins.append((direction, voisin))

        return voisins

    def generate(self):
        """
        Génération du labyrinthe. La méthode generate roulera tant que le compteur n'indiquera pas que nous avons visité
        toutes les cellules de la grille. Elle permet aussi de créer la Dotstring pour imager notre labyrinthe.

        """

        nombre_grille_complete: int = self.largeur * self.hauteur
        compteur: int = 1

        file_cellules_visitees: list = []
        cellule_actuelle: Cellule = self.position_cellule(self.point_depart_x, self.point_depart_y)

        dot: str = """ graph AI2022 { \n"""
        dot += f""""({cellule_actuelle.x},{cellule_actuelle.y})" 
            [pos="{cellule_actuelle.x},-{cellule_actuelle.y}!"]\n"""

        while compteur < nombre_grille_complete:
            voisins: object = self.recherche_voisin_valide(cellule_actuelle)

            if not voisins:
                # C'est le moment du backtrack lorsqu'il n'y a plus de voisins valides
                cellule_actuelle: Cellule = file_cellules_visitees.pop()
                continue

            # Sélectionner une cellule voisine de manière aléatoire et se déplacer de cellule
            direction, cellule_suivante = random.choice(voisins)
            # direction, cellule_suivante = voisins[0]

            dot += f""""({cellule_suivante.x},{cellule_suivante.y})"
                [pos="{cellule_suivante.x},-{cellule_suivante.y}!"]\n"""
            dot += f""""({cellule_actuelle.x},{cellule_actuelle.y})" -- 
                "({cellule_suivante.x},{cellule_suivante.y})"\n"""

            cellule_actuelle.ouvrir_porte(cellule_suivante, direction)
            file_cellules_visitees.append(cellule_actuelle)
            cellule_actuelle: Cellule = cellule_suivante
            compteur += 1

        dot = dot + """} """
        print(dot + """} """)

        src = graphviz.Source(dot, engine='fdp')
        src.render('labyrinthe/graphe-labyrinthe.gv', view=True)
