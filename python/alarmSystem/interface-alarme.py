#from tkinter.constants import TRUE
import pygame
import math
import requests 
import pprint
import time
import sys
from enum import Enum
import RPi.GPIO as GPIO 
from time import sleep

BTN_PIN = 17
PORTE_PIN = 22 
DEL_PINRouge = 18 
DEL_PINSirene = 23

GPIO.setmode(GPIO.BCM)
GPIO.setup(DEL_PINRouge,GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(DEL_PINSirene,GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(PORTE_PIN, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(BTN_PIN, GPIO.IN, pull_up_down = GPIO.PUD_UP)

pygame.init()
print ("Lancement de l'activité") 
#pygame.display.set_caption("systeme ON")
screen = pygame.display.set_mode([500, 350])

# Définir les polices
def police():
    sysfont = pygame.font.get_default_font()
    fontH2 = pygame.font.SysFont("pibotolt",18)
    fontH1 = pygame.font.SysFont("pibotolt",25, bold = True)
    fontH3 = pygame.font.SysFont("pibotolt",25)    
    return fontH2,fontH1, fontH3
fontH2, fontH1, FontH3 = police()  

# Définir les couleurs (RGB) 
def couleur():
    bleuUNE = (25,46,64)
    bleurDEUX = (62,110,140)
    bleuTROIS = (160,195,217)
    bleuQUATRE = (70,139,166)
    bleuCINQ = (201,231,242)
    jaune = (255,217,88)
    saumon = (250,128,114)
    return bleuUNE,bleurDEUX,bleuTROIS, bleuQUATRE, bleuCINQ, jaune, saumon
bleuUNE, bleurDEUX, bleuTROIS, bleuQUATRE, bleuCINQ, jaune, saumon = couleur()

# Obtenir l'heure et la date locale
now = time.localtime(time.time())

#Obtenir la météo via la clé api
def meteo():
    api_key = '2e46433c4d7e9005f9fd174f963b9922'; 
    url = 'http://api.openweathermap.org/data/2.5/weather?q=Montreal,ca&lang=fr&units=metric&appid=' + api_key; 
    reponse = requests.get(url) 
    data = reponse.json()  
 
    pp = pprint.PrettyPrinter(indent = 2) 
    pp.pprint(data)  
    return data
data = meteo()  

#Création du bouton DÉSARMÉ 
class objBouton(): 

    def __init__(self, couleur, x, y, rayon, texte=''): 
        self.couleur = couleur 
        self.x = x 
        self.y = y 
        self.rayon = rayon 
        self.texte = texte 

    def dessiner(self, screen):   
        pygame.draw.circle(screen, self.couleur, (self.x, self.y), self.rayon) 
        txtBtn = fontH1.render(self.texte, True, (0, 0, 0)) 
        rectBtn = txtBtn.get_rect() 
        rectBtn.center = (self.x, self.y) 
        screen.blit(txtBtn, rectBtn) 
 
    def isOverBouton(self, posSouris): 
        xSouris = posSouris[0] 
        ySouris = posSouris[1] 

        absX = (self.x-xSouris)**2 
        absY = (self.y-ySouris)**2 

        return (math.sqrt(absX+absY) < self.rayon) 

class Etat (Enum):
    armé = 1
    désarmé = 2
    panic = 3


#Interface du systeme DÉSARMÉ
def systeme_desarme():

  while True:
    print("\nÉTAT:  désarmé")


    screen.fill(bleuCINQ) 

    #ENTETE
    pygame.draw.rect(screen, bleuUNE, (0, 0, 500, 50), 0)
    img = fontH2.render("Le système est présentement DÉSARMÉ", True, bleuCINQ)
    screen.blit(img, (10,10))   

    #HEURE
    imgheure = fontH2.render(time.strftime("%y/%m/%d %H:%M", now), True, bleuCINQ)
    screen.blit(imgheure, (370,10))   

    #BOUTON pour ARMER
    btn = objBouton(bleuTROIS, 350, 200, 75, "ARMER",) 
    btn.dessiner(screen)

    #INFO TEMPÉRATURE
    infoMETEO = fontH1.render((str(int(round(data['main']['temp']))) + u"°C" ), True, bleuUNE)
    screen.blit(infoMETEO, (120, 205))
    infoMETEOdeux = fontH2.render(data['weather'][0]['description'] , True, bleurDEUX)
    screen.blit(infoMETEOdeux, (115, 235))


    #ICONE TEMPERATURE
    iconeMETEO = pygame.image.load(str(data['weather'][0]['icon'])+".png")
    iconeMETEO.convert()
    iconeMETEO = pygame.transform.rotozoom(iconeMETEO, 0, 1.3)
    screen.blit(iconeMETEO, (80,100))

    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            print("Fin de l'activité") 
            pygame.quit() 
            sys.exit()
    

        elif event.type == pygame.MOUSEBUTTONDOWN: 
            xSouris,ySouris = pygame.mouse.get_pos() 
                               
            if btn.isOverBouton((xSouris,ySouris)): 
              
              GPIO.output(DEL_PINRouge, GPIO.LOW)
              print("\n               **ARMÉ**   DelRougeON ")
              sleep(0.5)
              systeme_armee()

        pygame.display.flip()

#Interface du systeme ARMÉ
def systeme_armee():
  saisie= ""

  while True:
    print("\nÉTAT:  armé")

    
    screen.fill(bleuCINQ) 

    #ENTETE
    pygame.draw.rect(screen, bleuUNE, (0, 0, 500, 50), 0)
    img = fontH2.render("Le système est présentement ARMÉ", True, bleuCINQ)
    screen.blit(img, (10,10))   

    #HEURE
    imgheure = fontH2.render(time.strftime("%y/%m/%d %H:%M", now), True, bleuCINQ)
    screen.blit(imgheure, (370,10))   

    #BOUTON pour ARMER
    btn = objBouton(bleuTROIS, 125, 200, 70, "DÉSARMER") 
    btn.dessiner(screen)

    #BOUTON clavier
    btnUN = objBouton(bleuQUATRE, 330, 170, 20, "1",) 
    btnUN.dessiner(screen)
    btnDEUX = objBouton(bleuQUATRE, 380, 170, 20, "2",) 
    btnDEUX.dessiner(screen)
    btnTROIS = objBouton(bleuQUATRE, 430, 170, 20, "3",) 
    btnTROIS.dessiner(screen)

    btnEffacer = objBouton(saumon, 380, 240, 30, "",) 
    btnEffacer.dessiner(screen)

    #RECTANGLE code
    pygame.draw.rect(screen, bleuUNE, (280, 90, 205, 50), 0)
    code = FontH3.render(saisie, True, saumon)
    screen.blit(code, (300,100))  


    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            print("Fin de l'activité") 
            pygame.quit() 
            sys.exit()

        elif GPIO.input(PORTE_PIN) == 1:
          print ("\n               **PANIC**   DelJauneON ")
          return systeme_panic()

        elif event.type == pygame.MOUSEBUTTONDOWN: 
            xSouris,ySouris = pygame.mouse.get_pos() 

            if btn.isOverBouton((xSouris,ySouris)): 
              if saisie in ["123"]: 
                GPIO.output(DEL_PINRouge, GPIO.HIGH)   
                print ( "\n               **DÉSARMÉ**   DelRougeOff" )
                systeme_desarme()

              else:
                print("code invalide") 
                saisie = "    INVALIDE"

            elif btnUN.isOverBouton((xSouris,ySouris)): 
              print("bouton1")
              saisie = saisie + "1"
              print(saisie)

            elif btnDEUX.isOverBouton((xSouris,ySouris)): 
              print("bouton2")
              saisie = saisie + "2"  
              print(saisie)

            elif btnTROIS.isOverBouton((xSouris,ySouris)): 
              print("bouton3")
              saisie = saisie + "3"
              print(saisie)

            elif btnEffacer.isOverBouton((xSouris,ySouris)): 
                saisie = ""
        
    
    pygame.display.flip()

#Interface PANIC
def systeme_panic():
  GPIO.output(DEL_PINSirene,GPIO.LOW)
  saisie= ""


  while True:
    print("\nÉTAT:  PANIC")

    
    screen.fill(bleuCINQ) 

    #ENTETE
    pygame.draw.rect(screen, bleuUNE, (0, 0, 500, 50), 0)
    img = fontH2.render("PANIC   PANIC   PANIC   PANIC", True, jaune)
    screen.blit(img, (10,10))   

    #HEURE
    imgheure = fontH2.render(time.strftime("%y/%m/%d %H:%M", now), True, bleuCINQ)
    screen.blit(imgheure, (370,10))   

    #BOUTON pour ARMER
    btn = objBouton(jaune, 125, 200, 70, "DÉSARMER") 
    btn.dessiner(screen)

    #RECTANGLE code
    pygame.draw.rect(screen, bleuUNE, (280, 90, 205, 50), 0)
    code = FontH3.render(saisie, True, jaune)
    screen.blit(code, (300,100))  

    #BOUTON clavier
    btnUN = objBouton(bleuQUATRE, 330, 170, 20, "1",) 
    btnUN.dessiner(screen)
    btnDEUX = objBouton(bleuQUATRE, 380, 170, 20, "2",) 
    btnDEUX.dessiner(screen)
    btnTROIS = objBouton(bleuQUATRE, 430, 170, 20, "3",) 
    btnTROIS.dessiner(screen)

    btnEffacer = objBouton(saumon, 380, 240, 30, "",) 
    btnEffacer.dessiner(screen)


    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            print("Fin de l'activité") 
            pygame.quit() 
            sys.exit()


        elif event.type == pygame.MOUSEBUTTONDOWN: 
            xSouris,ySouris = pygame.mouse.get_pos() 
                               
            if btn.isOverBouton((xSouris,ySouris)): 
              if saisie in ["123"]:
                GPIO.output(DEL_PINSirene,GPIO.HIGH)  
                GPIO.output(DEL_PINRouge, GPIO.HIGH)     
                print ( "\n               **DÉSARMÉ**   DelRougeOff" )         
                systeme_desarme()

              else:
                print("code invalide") 
                saisie = "    INVALIDE"

            elif btnUN.isOverBouton((xSouris,ySouris)): 
              print("bouton1")
              saisie = saisie + "1"
              print(saisie)

            elif btnDEUX.isOverBouton((xSouris,ySouris)): 
              print("bouton2")
              saisie = saisie + "2"  
              print(saisie)

            elif btnTROIS.isOverBouton((xSouris,ySouris)): 
              print("bouton3")
              saisie = saisie + "3"
              print(saisie)

                          
            elif btnEffacer.isOverBouton((xSouris,ySouris)): 
                saisie = ""




        pygame.display.flip()


systeme_desarme()
