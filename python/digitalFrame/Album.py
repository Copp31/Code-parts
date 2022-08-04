#Okay
import os

# document pour la lecture des ALBUMS 
# bouton 1 changement album

#definition de la classe album
class Album():
    def __init__(self, config):
        self.config = config
        self.albums = os.listdir(self.config.PATH)
        self.albumCourant = 0
    
    #configuration du path des albums photos
    def affiche(self):
        if os.path.exists(self.config.PATH):
            print ("Le répertoire album existe")
        else:
            print ("Le répertoire album n'existe pas")
            
        print(self.albums)
    
    #utilisation de l'album courant (versus next album)
    def getAlbumCourant(self):
        return self.config.PATH + self.albums[self.albumCourant]  + "/"
        

    # cette fonction est appelé avec le BOUTON ALBUM. Permet changer album photos
    def getNextAlbum(self):
        if self.albumCourant < (len(self.albums) - 1):
            self.albumCourant = self.albumCourant + 1
        else:
            self.albumCourant = 0
        
        return self.config.PATH + self.albums[self.albumCourant] + "/"   
        
    def getAlbumName(self):
        return (self.albums[self.albumCourant])
    

#MODULE DE TEST
if __name__ == "__main__":
    print ("Début du test\n")
    from Config import *

    config = Listeconfig()
    
    a = Album(config)
    a.affiche()
    print(a.getAlbumCourant())
    print(a.getNextAlbum())
    print("\nFin du test")
