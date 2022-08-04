#!/usr/bin/env python
# coding: utf-8

import pymongo

class Database:
    def __init__(self, uri):
        self.client = pymongo.MongoClient(uri)
        self.database = self.client['serre_database']
        self.arduino_data = self.database['arduino_data']
        self.user_data = self.database['user_data']
        print(f"Client connected( {uri} )")

    def add_data(self, document: dict):
        """
        modele de données: {'_id': ObjectId('6202cf04d8458e40321e957a'),
                            'date': datetime.datetime(2022, 2, 8, 15, 13, 56, 597000),
                            'temperature': 200,
                            'reservoir': 0,
                            'humidite1': 500,
                            'humidite2': 500,
                            'humidite3': 500,
                            'humidite4': 500,
                            'pompe1': 0,
                            'pompe2': 0,
                            'pompe3': 0,
                            'pompe4': 0}
        """
        self.arduino_data.insert_one(document)
        print(f"Add {document}")


    def read_data(self, query: dict, limit: int = 1):
        """ Retourne un dictionnaire ou une liste de dictionnaires selon le nombre de documents trouvés."""
        response = self.arduino_data.find(query).sort("_id", -1).limit(limit)
        results = []
        for i in response:
            results.append(i)
            # print(i)

        print(f"Found {len(results)} document using filter: {query}" if len(results) <= 1 \
                  else f"Found {len(results)} documents using filter: {query}")
        return results

    def wipe_data(self):
        """Effacer l'historique des données d'états du Arduino"""
        self.arduino_data.drop()

    def add_user(self, document: dict):
        """
        Modele de données: {"username": username,
                            "password": Hashed.password,
                            "styles": "styles_1.css",
                            "plantes": ["Plante 1","Plante 2","Plante 3","Plante 4"],
                            "auto_humidité": {"minimum": [15,15,55,55], "duree": [15,15,55,55]}
                            "auto_journalier": {"début": [[7,15],[7,15],[19,0],[22,0]], "duree": [10,10,55,55]}
                            "auto_suggestion": {"parametre1: [0,1,2,3], "parametre2: [a,b,c,d]}
                            }
        """
        self.user_data.insert_one(document)
        print(f"Add {document}")

    def read_user(self, query: dict, limit: int = 1):
        """Retourne un dictionnaire ou une liste de dictionnaires"""
        response = self.user_data.find(query).limit(limit)
        results = []
        for i in response:
            results.append(i)
            # print(i)
        return results[0] if len(results) == 1 else results

    def update_user(self, query: dict, new_data: dict ):
        self.user_data.update_one(query, {"$set": new_data})
        print("Updated ")

    def delete_user(self, query):
        self.user_data.delete_one(query)




if __name__ == "__main__":


    URI = "mongodb://localhost:27017/"
    DB_NAME = "serre_database_test"