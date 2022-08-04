class Cellule:
    """
    Un labyrinthe est formé d'un nombre de cellules déterminé par l'utilisatrice-teur

    Avant la formation du labyrinthe, au moment de l'initialisation de la grille, on prend en compte que chaque mur
        interne appartient aussi à une cellule.

    """

    duo_murs: dict = {'haut': 'bas', 'bas': 'haut', 'gauche': 'droite', 'droite': 'gauche'}

    def __init__(self, x: int, y: int):
        """
        Initialisation de la cellule à la position x et y.
            Au moment de l'initialisation, il n'y a aucune porte à chaque direction de la cellule (True)

        """

        self.x: int = x
        self.y: int = y
        self.pas_de_porte: dict = {'haut': True, 'bas': True, 'gauche': True, 'droite': True}

    def aucune_porte_ouverte(self):
        """
        Vérification qu'il n'y aucune porte/ouverture dans une cellule.

        """

        return all(self.pas_de_porte.values())

    def ouvrir_porte(self, mur_adjacent, aucune_porte: str):
        """
        Création de lien, imagé par des portes, entre les cellules pour créer le labyrinthe.

        """

        self.pas_de_porte[aucune_porte] = False
        mur_adjacent.pas_de_porte[Cellule.duo_murs[aucune_porte]] = False
