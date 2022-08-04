import logging
from ruamel.yaml import YAML

# Permet de lire les éléments qui font parties des configurations du fichier YAML
# L'interprétation de la configuration permet de de savoir la période de chaque photo, leur fichier 
# source et l'ouverture/ fermeture de l'affichage du cadre. 


#-------- Logging Setup --------#

logging.basicConfig(
    filename="D:\AEC-Cours\BLOC2\Systeme embarqué\CadreNumerique\debug.log",
    datefmt="%c",
    level=logging.DEBUG,
    format= "%(asctime)s       LINE: %(lineno)d       %(levelname)s: %(message)s")


class Listeconfig():
    def __init__(self):
        
        # récupération de l'information losqu'il y a un problem
        #self.LOG_LEVEL = logging.DEBUG                  
        

        # Lecture du fichi de configuration  config_cadre.yaml
        #et initialisation de la classe listeconfig
        
        self.CONFIG_FILE_NAME = "D:\AEC-Cours\BLOC2\Systeme embarqué\CadreNumerique\config_cadre.yaml"                  
        
        yaml=YAML(typ="safe") 
        #lecture et chargement des fichier configuré quelques lignes plus haut
        fichier = open(self.CONFIG_FILE_NAME, "r")
        listeconfig = yaml.load(fichier)

        # lecture des information dans le fichier config_cadre.yaml     
        self.WAKEUP = listeconfig['wakeup']
        self.CLOSE = listeconfig['close']
        self.PERIOD = listeconfig['period']
        self.PATH = listeconfig['path']       
 
        #configuration de la largeur et hauteur des images (frame du cadre numérique) 
        self.SCREEN_WIDTH = listeconfig['screen_width']
        self.SCREEN_HEIGHT = listeconfig['screen_height']
        self.SCREEN_SIZE = (self.SCREEN_WIDTH, self.SCREEN_HEIGHT)
        self.FPS = 100
        fichier.close()

    # Permet de debug des variables spécifiques
    def log(self, debug):

        logging.debug(debug)
 
        
    def affiche(self):
        # Le module logging permet de tracker les événements qui surviennent 
        # quand le programme roule. Affichage a l'écran de ces informations  

        logging.debug("Affichage de la configuration:")                        
        logging.debug(self.WAKEUP) 
        logging.debug(self.CLOSE) 
        logging.debug(self.PERIOD) 
        logging.debug(self.PATH) 
        
        logging.debug(self.SCREEN_WIDTH)
        logging.debug(self.SCREEN_HEIGHT) 
        logging.debug(self.SCREEN_SIZE) 
        logging.debug(self.FPS) 

    # retourne un format date transformé en float.
    def getPeriod(self):
        chaine = self.PERIOD 
        heure,minute,seconde = map(int, chaine.split(':'))
        return (heure * 3600 + minute * 60 + seconde)


#MODULE DE TEST
if __name__ == "__main__":
    print ("Début du test\n")
    
    a = Listeconfig()
    a.affiche()
    print(a.getPeriod())
    
    print("\nFin du test")
