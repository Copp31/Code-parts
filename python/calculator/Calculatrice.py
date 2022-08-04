from tkinter import* 
import math
from tkinter import scrolledtext


class calculatrice:

    def __init__(self):
        self.saisie = "0"
        self.expression = "0"
        self.resultat = 0.0
        self.resultats = []
        self.erreur = "Erreur : "
        self.erreurMessageType = []
        
    def evalue(self):
        try:
            self.transformeSaisie()
            self.resultat = float(eval(self.expression))
            self.resultat= str(round (self.resultat,7))
            self.resultats.append(self.expression)
            self.resultats.append(self.resultat)

            zoneSortie.insert(1.0, self.resultat + "\n", "font_reponse")
            zoneSortie.insert(1.0, self.expression + "    =     ", "font_normale")


        except ZeroDivisionError:
            self.resultats.append(self.erreur + "division par zéro")
            self.resultats.append(self.expression)
            self.erreurMessageType.append("problème /0 ()")
            
            zoneSortie.insert(1.0, self.erreur +"\n" + self.expression +"    "+ "Impossible de divisier par 0" + "\n", "font_erreur")


        except:
            self.resultat = str(self.resultat)
            self.resultats.append(self.erreur + "eval()")            
            self.resultats.append(self.expression)
            self.erreurMessageType.append("problème eval()")

            zoneSortie.insert(1.0, self.erreur +"\n" + self.expression + "  N'est pas valide" + "\n", "font_erreur")



    def reset(self):
        self.saisie = "0"
        self.expression = "0"
        self.resultat = 0.0
        # self.resultat = []
        self.erreur = "Erreur :"


    def transformeSaisie(self):
        self.expression = self.saisie
        # if "carr" in self.expression: 
        self.expression = self.expression.replace("carr", "**2" )

        # if "%" in self.expression:
        self.expression = self.expression.replace("%","/100")

        # if "√" in self.expression: 
        for i in range (0, len(self.expression)-1):
            if self.expression[i] == "√":
                x = self.expression[i+1]
                self.expression = self.expression.replace("√" + x, "math.sqrt("+ x +")")
       
        



from tkinter import*
# from calculatrice import* 
from math import *
from tkinter import scrolledtext

c = calculatrice()


# -------------------------------Fonctions


def entrée(x):
    if c.saisie == "0":
        c.saisie = x
        aff.set(c.saisie)

    else: 
        c.saisie = c.saisie + x
        aff.set(c.saisie)

def clear():
    c.reset()
    aff.set(c.saisie)

def egal():
    c.evalue()

def EffacerHistorique():
    zoneSortie.delete("1.0","end")


#---------------------------Variable de graphisme

hauteurBouton = 1
largeurBouton = 9
CouleurBoutChiffre = "khaki2"
CouleurBoutSpecial = "light cyan2"
backGround = "mint cream"

def changement(event):
    if choixCouleur.get() == "Rose":
        fen.configure (bg = "antique white")
        historique.configure (bg = "antique white")
        zoneSortie.configure (bg = "antique white")
   
    elif choixCouleur.get() == "Crème":
        fen.configure (bg = "mint cream")
        historique.configure (bg = "mint cream")
        zoneSortie.configure (bg = "mint cream")

    else:
        fen.configure (bg = "DarkSeaGreen1")
        historique.configure (bg = "DarkSeaGreen1")
        zoneSortie.configure (bg = "DarkSeaGreen1")


#--------------------------------Insertion interface 
fen = Tk ()
fen.title("CalculaCopp")
fen.geometry("335x400")
fen.resizable(width = False, height = False)
fen.configure (bg = backGround)


#--------------------------------------------Calculatrice interface
#ROW 0---------------------------
aff = StringVar()
zoneSaisie = Entry(fen, textvariable = aff, width =50, bg = "light cyan2", justify = RIGHT, bd = 4)
zoneSaisie.grid(row=0, column=0,columnspan=5)
aff.set("0")

#ROW 1---------------------------
def sept():
    entrée("7")

def huit():
    entrée("8")

def neuf():
    entrée("9")


bouton7 = Button (fen, text = "7", command = sept, width = largeurBouton, height = hauteurBouton, bg = CouleurBoutChiffre, bd = 3)
bouton7.grid (row = 1, column = 0, columnspan = 1)

bouton8 = Button (fen, text = "8", command = huit, width = largeurBouton, height = hauteurBouton, bg = CouleurBoutChiffre, bd = 3)
bouton8.grid (row = 1, column = 1, columnspan = 1)

bouton9 = Button (fen, text = "9", command = neuf, width = largeurBouton, height = hauteurBouton, bg = CouleurBoutChiffre, bd = 3)
bouton9.grid (row = 1, column = 2, columnspan = 1)

choixCouleur = StringVar(fen)
choixCouleur.set("Couleur")
liste = OptionMenu(fen, choixCouleur, "Rose", "Vert", "Crème", command = changement)
liste.config(bg ="salmon")
liste["menu"].config(bg = "mint cream")
liste.grid (row = 1, column = 3, columnspan = 1)




#ROW 2---------------------------
def quatre():
    entrée("4")

def cinq():
    entrée("5")

def six():
    entrée("6")

bouton4 = Button (fen, text = "4", command = quatre, width = largeurBouton, height = hauteurBouton, bg = CouleurBoutChiffre, bd = 3)
bouton4.grid (row = 2, column = 0, columnspan = 1)

bouton5 = Button (fen, text = "5", command = cinq, width = largeurBouton, height = hauteurBouton, bg = CouleurBoutChiffre, bd = 3)
bouton5.grid (row = 2, column = 1, columnspan = 1)

bouton6 = Button (fen, text = "6", command = six, width = largeurBouton, height = hauteurBouton, bg = CouleurBoutChiffre, bd = 3)
bouton6.grid (row = 2, column = 2, columnspan = 1)

import pathlib
current_dir = pathlib.Path(__file__).parent
print(current_dir)
flamme = PhotoImage(file = str(current_dir) +'\\flamme.png')
EffacerHistorique = Button(fen, image = flamme, width = 50, height = 25, command = EffacerHistorique)
EffacerHistorique = Button(fen, width = 50, height = 25, command = EffacerHistorique)
EffacerHistorique.grid (row = 2, column = 3, columnspan = 1)


#ROW 3---------------------------
def un():
    entrée("1")

def deux():
    entrée("2")

def trois():
    entrée("3")
    
def multi():
    entrée("*")

bouton1 = Button (fen, text = "1", command = un, width = largeurBouton, height = hauteurBouton, bg = CouleurBoutChiffre, bd = 3)
bouton1.grid (row = 3, column = 0, columnspan = 1)

bouton2 = Button (fen, text = "2", command = deux, width = largeurBouton, height = hauteurBouton, bg = CouleurBoutChiffre, bd = 3)
bouton2.grid (row = 3, column = 1, columnspan = 1)

bouton3 = Button (fen, text = "3", command = trois, width = largeurBouton, height = hauteurBouton, bg = CouleurBoutChiffre, bd = 3)
bouton3.grid (row = 3, column = 2, columnspan = 1)

boutonMulti = Button (fen, text = "*", command = multi, width = largeurBouton, height = hauteurBouton, bg = CouleurBoutSpecial, bd = 3)
boutonMulti.grid (row = 3, column = 3, columnspan = 1)


#ROW 4---------------------------
def zero():
    entrée("0")

def point():
    entrée(".")

def pourcentage():
    entrée("%")

def div():
    entrée("/")

bouton0 = Button (fen, text = "0", command = zero, width = largeurBouton, height = hauteurBouton, bg = CouleurBoutChiffre, bd = 3)
bouton0.grid (row = 4, column = 0, columnspan = 1)

boutonDecimal = Button (fen, text = ".", command = point, width = largeurBouton, height = hauteurBouton, bg = CouleurBoutSpecial, bd = 3)
boutonDecimal.grid (row = 4, column = 1, columnspan = 1)

boutonPourcentage = Button (fen, text = "%", command = pourcentage, width = largeurBouton, height = hauteurBouton, bg = CouleurBoutSpecial, bd = 3)
boutonPourcentage.grid (row = 4, column = 2, columnspan = 1)

boutonDiviser = Button (fen, text = "÷", command = div, width = largeurBouton, height = hauteurBouton, bg = CouleurBoutSpecial, bd = 3)
boutonDiviser.grid (row = 4, column = 3, columnspan = 1)


#ROW 5---------------------------
def parGau():
    entrée("(")

def parDroi():
    entrée(")")

def add():
    entrée("+")


boutonParantGauche = Button (fen, text = "(", command = parGau, width = largeurBouton, height = hauteurBouton, bg = CouleurBoutSpecial, bd = 3)
boutonParantGauche.grid (row = 5, column = 0, columnspan = 1)

boutonParantDroite = Button (fen, text = ")", command = parDroi, width = largeurBouton, height = hauteurBouton, bg = CouleurBoutSpecial, bd = 3)
boutonParantDroite.grid (row = 5, column = 1, columnspan = 1)

boutonAddition = Button (fen, text = "+", command = add, width = largeurBouton, height = hauteurBouton, bg = CouleurBoutSpecial, bd = 3)
boutonAddition.grid (row = 5, column = 2, columnspan = 1)

boutonÉgal= Button (fen, text = "=", command = egal, width = largeurBouton, height = hauteurBouton, bg = CouleurBoutSpecial, bd = 3)
boutonÉgal.grid (row = 5, column = 3, columnspan = 1)


#ROW 6---------------------------
def carr():
    entrée("carr")

def racCar():
    entrée("√")

def soust():
    entrée("-")

boutonExposantDeux = Button (fen, text = "^2", command = carr, width = largeurBouton, height = hauteurBouton, bg = CouleurBoutSpecial, bd = 3)
boutonExposantDeux.grid (row = 6, column = 0, columnspan = 1)

boutonRacineCarr = Button (fen, text = "√", command = racCar, width = largeurBouton, height = hauteurBouton, bg = CouleurBoutSpecial, bd = 3)
boutonRacineCarr.grid (row = 6, column = 1, columnspan = 1)

boutonSoustraction = Button (fen, text = "-", command = soust, width = largeurBouton, height = hauteurBouton, bg = CouleurBoutSpecial, bd = 3)
boutonSoustraction.grid (row = 6, column = 2, columnspan = 1)

boutonC= Button (fen, text = "C", command = clear, width = largeurBouton, height = hauteurBouton, bg = CouleurBoutSpecial, bd = 3)
boutonC.grid (row = 6, column = 3, columnspan = 1)



#ROW 7---------------------------

historique = Label(fen, text= "Historique", width = 30, font=("Bahnschrift", 10), bg = backGround)
historique.grid(row=7, column=0,columnspan=5)



#ROW 8---------------------------

from tkinter import font
myFont = font.Font(size = 10, family='Bahnschrift')

zoneSortie = scrolledtext.ScrolledText(fen)
zoneSortie.config(width=40, height=10, wrap=WORD, bd = 3)
zoneSortie.grid(row=9, column=0,columnspan=7) 
zoneSortie.tag_configure("font_normale", font = myFont)
zoneSortie.tag_configure("font_reponse", font = myFont, foreground = "steel blue")
zoneSortie.tag_configure("font_erreur", font = myFont, foreground = "firebrick1")


fen.mainloop()
