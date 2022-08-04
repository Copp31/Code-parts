import os
from PIL import ExifTags
from PIL import Image
import piexif


# document pour lectures des photos 

def getRotation(fichier):
#--------------------------------      Extraire l'information EXIF de rotation de l'image

    exif_dict = piexif.load(fichier)

    if piexif.ImageIFD.Orientation in exif_dict["0th"]:
        orientation = exif_dict["0th"][piexif.ImageIFD.Orientation]
        if orientation == 3:
            return 180
     
        
        elif orientation == 6:
            return 90
           
        
        elif orientation == 8:
            return 270
           
        
        else:
            return 0
    else:
        return 0


def aspectScale(img, tailleEcran):
#--------------------------------      Mettre a l'echelle l'image 'img' pour s'ajuster à 'tailleEcran'.
#--------------------------------      Respecter les proportion de l'image originale
# à changer selon ce qu'on souhaite précisément (je dois travailler sur le recadrage à l'échelle *
  
    fichierImg = img  #image test pour transformation
    
    nomFichier, extensionFichier = os.path.splitext(fichierImg) 
    print(nomFichier, extensionFichier) 

    try: 
        img = Image.open(fichierImg) 
        rgbImg = img.convert('RGB') 
        rgbImg = rgbImg.resize((400, 300)) 
        rgbImg.save(nomFichier + extensionFichier, "JPEG")

    except OSError: 
        print("Impossible de convertir", fichierImg) 


class ListePhotos(): 

    def __init__(self, path):

        extensions = ['.png', '.jpg', '.jpeg', '.gif', '.bmp']
        self.listePhotos = []
        listeTmp = os.listdir(path)

        for photo in listeTmp:
            filename, ext = os.path.splitext(photo)
            e = ext.lower()

            if e in extensions:
                self.listePhotos.append(path + photo)

        self.photoCourante = 0
        self.noImage = "no-image.png"
    
    
    # Sélectionne la photo courante de l'album
    def getPhoto(self):

        if len(self.listePhotos) == 0:
            photo = self.noImage
            return(photo)
        
        photo = self.listePhotos[self.photoCourante]
        
        if self.photoCourante < (len(self.listePhotos) - 1):
            self.photoCourante = self.photoCourante + 1

        else:
            self.photoCourante = 0                               
            
        if len(self.listePhotos) == 0:
            photo = self.noImage
                       
        return(photo)
        

#MODULE DE TEST
if __name__ == "__main__":

    print ("Début du test\n")
    from Config import *

    config = Listeconfig()
    
    a = ListePhotos(config.PATH)


    print("\nFin du test")
