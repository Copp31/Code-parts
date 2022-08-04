'''

Fait par Coppélia LaRoche-Francoeur, July Dulac & Jean-Abraham Chery

Objectif: Réaliser un cadre numérique à haute résolution. Pour la réalisation du projet, 
nous devons utiliser un Raspberry Pi et pyGame.

'''

# Cadre_numerique_main.py
from Album import Album
from PIL import ExifTags
import pygame 
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS
from Liste_photos import *
import sys
import RPi.GPIO as GPIO 
from enum import Enum
import datetime, time
from time import sleep
import Config

#configuration des GPIO 
BTN_Album = 17
BTN_Veille = 22 

GPIO.setmode(GPIO.BCM)
GPIO.setup(BTN_Album, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(BTN_Veille, GPIO.IN, pull_up_down = GPIO.PUD_UP)

pygame.init()
print ("Lancement de l'activité") 


###################################################################
# Initialise toutes les variables selon le fichier YAML           #
# et Config Définition de la classe SETUP                         #
###################################################################

setup = Config.Listeconfig()
screen = pygame.display.set_mode([setup.SCREEN_WIDTH, setup.SCREEN_HEIGHT])
debut_affichage = 0

setup.affiche()
clock = pygame.time.Clock()
album = Album(setup)

#variable pour aller chercher l'album courant
albumpath = album.getAlbumCourant()

# liste affiche = remplis listephotos[] avec le nom de toutes les photos
la = ListePhotos(albumpath)

# temps d'affichage de chaque photo
delai_affichage = setup.getPeriod()    

def Delay(temps,debut):
    seconde = 1
    fin = time.time()     # Retourne 1 si delais dépassé
    seconde = fin - debut
    if fin - debut >= temps:
        return 1
    else:
        return 0

#creation des Etats pour changer le scénario selon les boutons appuyé et la veille à l'extérieur du wakeup et close
class Etat (Enum):
    boutonAllume = 1
    boutonVeille = 2


# le cadre est en etat allumé quand on débute
bouton_etat = Etat.boutonAllume
clock = pygame.time.Clock()


#-------- Boucle Principal --------#

running = True

while running:

    TimeNow = datetime.datetime.now().strftime('%H:%M:%S')
    print(TimeNow)
   
    # Continue la boucle tant que c'est en etat allume
    while bouton_etat == Etat.boutonAllume:
        
        for event in pygame.event.get():  

            if event.type == pygame.QUIT:

                print("Fin de l'activité") 
                running = False
                sys.exit()

         # Change d'album si bouton pressé
        if GPIO.input(BTN_Album) == 0 :

            albumpath = album.getNextAlbum()
            la = ListePhotos(albumpath)
            print (albumpath) 
            sleep(0.5)
            
        # Change l'etat à veille si bouton pressé ou s'il est temps de CLOSE
        if (GPIO.input(BTN_Veille) == 0) or ((TimeNow < setup.WAKEUP) and (TimeNow > setup.CLOSE)): 

            bouton_etat = Etat.boutonVeille
            print("veille")
            time.sleep(0.4)
            break

        # changement des images si elles ne répondent pas au format désiré 
        if Delay(delai_affichage,debut_affichage) == 1:   
                
                photo = la.getPhoto()
                rotation = int(getRotation(photo))

                #rotation contient les degré que la photo a été tournée            
                
                if rotation != 1 and rotation !=0:

                    img = pygame.transform.rotate(img, rotation)

                img = pygame.image.load(photo)
                aspectScale(photo,screen)
                img = pygame.image.load(photo)

                screen.blit(img, (0,0)) 
                debut_affichage = time.time()
                img = pygame.image.load(photo)

        pygame.display.flip()        


    # Continue la boucle tant que c'est en etat veille
    while bouton_etat == Etat.boutonVeille:

            print("allo2")

            for event in pygame.event.get():
                        
                if event.type == pygame.QUIT:

                    print("Fin de l'activité") 
                    running = False
                    sys.exit()

            # Change l'etat à Allume si bouton pressé ou s'il est temps de WAKEUP
            if (GPIO.input(BTN_Veille) == 0) or ((TimeNow > setup.WAKEUP) and (TimeNow < setup.CLOSE)):

                bouton_etat = Etat.boutonAllume
                time.sleep(0.4)
                screen.blit(img, (0,0))
                pygame.display.flip() 
                break

            screen.fill((0,0,0))
            pygame.display.flip() 

pygame.QUIT
