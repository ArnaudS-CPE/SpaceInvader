# BURLOT Alexandre, SIBENALER Arnaud
# début du projet le 15/12/2020
# Objectif : bibliothèque de fonctions pour le space invader
# TODO : lien du sujet du tp : https://prod.e-campus.cpe.fr/pluginfile.php/53617/mod_resource/content/1/TP3.pdf
# Gerer la collision entre le tir et l'Alien, ils doivent tous les deux disparaitres
# permettre à l'alien de descendre petit à petit lorsqu'il à fait un allé retour
# Si l'allien arrive au niveau du vaisseau et le touche, le vaiseau est détruit et la partie est terminée
# mettre maintenant plusieur aliens sur la meme ligne et verifier quetout se passe bien
# permettre aux aliens de tirer vers le bas, le déclenchement est aléatoire, même vitesse que ceux du vaiseau
# si un tir alien atteint le vaiseau, les deux sont détruits et la partie est finie
# faire 3 vies pour le joueur et lui afficher
# créer des ilots pour que le vaisseau puisse se cacher, se détruisent petità petit si ils subissent un tir alien
# Faire apparaitre un ennemi bonus et gerer son état
# introduire les scores transformer les aliens soit en formes simples soit en images
# barre du menu
# BONUS :
# • Augmenter la vitesse des Aliens lorsqu’ils sont moins nombreux.
# • Gérer le passage de la soucoupe
# • Créer plusieurs niveaux à votre jeu
# • Ajouter une image de fond (différente pour chaque niveau)
# • Gestion des meilleurs scores (avec inscription dans un fichier texte)
# • Permettre à l’utilisateur de changer les touches de contrôle
# • Mettre des cheat codes afin de gagner des vies supplémentaires
# • Laisser parler votre imagination et n’hésitez pas à demander conseil à vos ainés qui auraient perdu un temps précieux à jouer à ce jeu ! 
#
# Changer les variables "X", "Y" et "DX" pour que la fonction de déplacement alien et Alien se fassent bien
#

from tkinter import *

LargeurCanevas = 900
HauteurCanevas = 800
x = 10
y = 700
DX=3
posXAlien = 240
posYAlien = 300

class Window:

    def __init__(self, geom, title):
        self.__name = self
        self.__geometry = geom
        self.__title = title


class Alien:

    def __init__(self):
        self.__height = height
        self.__width = width


class Vaisseau:

    def __init__(self,posX,posY):
        self.__posX = posX
        self.__posY = posY


class Mur:

    def __init__(self, height, width):
        self.__height = height
        self.__width = width


def deplacementAlien () :
    global posXAlien, posYAlien, DX
    if posXAlien+12+DX > LargeurCanevas :
        posXAlien = 2*(LargeurCanevas-12)-posXAlien
        DX = -DX        
    if posXAlien-12+DX < 0:
        posXAlien = 2*12-posXAlien
        DX = -DX
    posXAlien += DX
    canevas.coords(Alien, posXAlien-12, posYAlien-12, posXAlien+12, posYAlien+12)
    mw.after(20,deplacementAlien)

def evenement(event):
    global x,y
    touche = event.keysym
    print(touche)
    if touche == 'Right':
        if x+50 >= 900:
            pass
        else:
            x += 6
            canevas.coords(Vaisseau, x,y,x+50,y+30)
    
    if touche == 'Left':
        if x <= 4:
            pass
        else:
            x -= 6
            canevas.coords(Vaisseau, x,y,x+50,y+30)
    
    if touche == "space":
        posXTir = x +(50/2)
        posYTir = y
        Tir = canevas.create_rectangle(posXTir,posYTir,posXTir,posYTir-6, fill = "black")
        movementTir(Tir, posXTir, posYTir)
        
def movementTir(Tir, posXTir,posYTir):
    if posYTir <=0:
        pass
    else:
        posYTir -= 6
        canevas.coords(Tir,posXTir,posYTir,posXTir,posYTir-6)
        mw.after(30,lambda:[movementTir(Tir,posXTir,posYTir)])

# création de la fenetre
mw = Tk()
mw.geometry("1000x800")
mw.title("Space Invaders")

# création des widgets
quit = Button(mw, text = "Quitter", command = mw.destroy)
quit.pack()
canevas = Canvas(mw, width = LargeurCanevas, height = HauteurCanevas, bg = "grey")
canevas.pack(padx = 5, pady = 5)


Vaisseau = canevas.create_rectangle(x, y, x+50, y+30, width=2, outline='red', fill='white')
canevas.focus_set()
canevas.bind('<Key>',evenement)
Alien = canevas.create_oval(posXAlien-12, posYAlien-12, posXAlien+12, posYAlien+12, width=3, outline='green', fill='yellow')

deplacementAlien()

mw.mainloop()

