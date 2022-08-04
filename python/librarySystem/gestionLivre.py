class GestionLivre:

    def __init__(self):
        self.dictio_ClientLivre: dict = {}
        self.dictio_LivreJour: dict = {}

    def gestion_retour(self):
        """
        Ce module permet la gestion des retour des livres et l'actualisation du dictionnaire des livres loués.
        Lorsqu'un livre a été loué durant 7 jours, il sort de ce dictionnaire et devient à nouveau disponible
        à la location.
        """

        for key, value in list(self.dictio_LivreJour.items()):
            if value == 0:
                self.dictio_LivreJour.pop(key, value)
                print(f"---------------------->     Le livre {key} est maintenant disponible")

        for key, value in self.dictio_LivreJour.items():
            self.dictio_LivreJour[key] = self.dictio_LivreJour[key] - 1

    def creation_dictio_client_livre(self):
        """
        Ce module permet de prendre les informations Clients et Indices du livre sélectionné puis de les insérer dans
        2 dictionnaires distincts. Le premier, Client et indice de location, se renouvelle tous les jours.
        Le second, Indices de location et nombre de jours restant à la location, se renouvelle quotidiennement, mais
        concerve chaque donnée durant 7 jours seulement.
        """

        NBR_LIVRES: int = 10

        while True:
            try:
                nbr_client: int = int(input("* Prière d\'inscrire seulement des nombres entiers positifs * \n"
                                            "Combien de client.e(s) aujourd\'hui : "))
                if nbr_client <= 0:
                    print("Le nombre de client.e(s) doit être plus grand que 0...")
                    raise ValueError
                else:
                    break
            except ValueError:
                print("Recommencez...")

        compteur_client: int = 0

        while compteur_client != nbr_client:
            while True:
                try:
                    indice_livre: int = int(input(" * Veuillez saisir l\'indice du livre * \n"
                                                  f"Client.e {compteur_client}: quel est l\'indice du livre réservé? "))
                    if indice_livre >= NBR_LIVRES:
                        print("L\'indice du livre doit être en 0 et 9...")
                        raise ValueError

                    if indice_livre < 0:
                        print("L\'indice du livre doit être en 0 et 9 donc, un entier positif...")
                        raise ValueError

                    else:
                        self.dictio_ClientLivre.update({compteur_client: indice_livre})
                        compteur_client += 1
                        break

                except ValueError:
                    print("Recommencez...")

    def disponibilite_livre(self):
        """
        Ce module permet de valider si le livre désiré par un client est disponible ou non. Si le livre est disponible,
        il rentre dans le dictionnaire des livres loués avec une valeur de 7 jours. Le module affiche ensuite la liste
        des indices de livres qui sont loués et leur retour est prévu.
        """

        DUREE_LOC: int = 7

        for key, value in self.dictio_ClientLivre.items():
            if value in self.dictio_LivreJour.keys():
                print(f"Client.e {key}: le livre {value} n\'est pas disponible. ")

            else:
                print(f"Client.e {key}: le livre {value} vous est réservé pour 7 jours")
                self.dictio_LivreJour.update({value: DUREE_LOC})

        for key, value in self.dictio_LivreJour.items():
            print(f"---> Disponibilité: livre {key}, disponible dans {value} jour(s).")
