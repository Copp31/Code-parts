from gestionLivre import GestionLivre

gestionLivre = GestionLivre()


def main():
    """
    Le module main permet d'assurer le roulement des journées.
    """

    JOUR: int = 1

    while True:
        print(f"\n Bienvenue au JOUR {JOUR} des réservations de la bibliothèque \n")
        gestionLivre.gestion_retour()
        gestionLivre.creation_dictio_client_livre()
        gestionLivre.disponibilite_livre()
        JOUR += 1


if __name__ == "__main__":
    main()
