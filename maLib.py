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
# 
# 
# 
#  
# La collision est detectée, il manque la suppression des deux objets dans la condition de collision

from tkinter import Label, Canvas, Button, Tk, Entry

LargeurCanevas = 900
HauteurCanevas = 800
DX=3
dicoalien = {} # contient les objets aliens et leurs informations 


class Alien:
    global LargeurCanevas, HauteurCanevas, dicoalien

    def __init__(self, posX, posY, height, width):
        self.__height = height
        self.__width = width
        self.__posX = posX
        self.__posY = posY
        self.__pattern = canevas.create_rectangle(posX, posY, posX+width, posY+height, width=3, outline='green', fill='yellow')
    
    def get_posX(self):
        return self.__posX
    
    def get_posY(self):
        return self.__posY
    
    def get_height(self):
        return self.__height

    def get_width(self):
        return self.__width
    
    def deplacementAlien(self) :
        global DX
        if self.__posX+self.__width > LargeurCanevas :
            self.__posX = LargeurCanevas-self.__width
            DX = -DX        
        if self.__posX < 3:
            self.__posX = 0
            DX = -DX
        self.__posX += DX
        canevas.coords(self.__pattern, self.__posX, self.__posY, self.__posX+self.__width, self.__posY+self.__height)
        mw.after(20,self.deplacementAlien)
        dicoalien[self] = [self.__posX, self.__posY, self.__width, self.__height]

class Vaisseau:
    global LargeurCanevas, HauteurCanevas

    def __init__(self, posX, posY):
        self.__posX = posX
        self.__posY = posY
        self.__height = 50
        self.__width = 100
        self.__pattern = canevas.create_rectangle(self.__posX, self.__posY, self.__posX+self.__width, self.__posY+self.__height, 
            width=2, outline='red', fill='white')
    
    def evenement(self, event):
        touche = event.keysym
        print(touche)
        if touche == 'Right':
            if self.__posX+self.__width >= LargeurCanevas:
                pass
            else:
                self.__posX += 6
                canevas.coords(self.__pattern, self.__posX, self.__posY, self.__posX+self.__width, self.__posY+self.__height)
        
        if touche == 'Left':
            if self.__posX <= 4:
                pass
            else:
                self.__posX -= 6
                canevas.coords(self.__pattern, self.__posX, self.__posY, self.__posX+self.__width, self.__posY+self.__height)
        
        if touche == "space":
            posXTir = self.__posX + (self.__width//2)
            posYTir = self.__posY
            tir = Tir(posXTir, posYTir)
            del tir
        

class Tir:
    global dicoalien
    def __init__(self, posXTir, posYTir):
        self.__posX = posXTir
        self.__posY = posYTir
        self.__pattern = canevas.create_rectangle(posXTir,posYTir,posXTir,posYTir-6, fill = "black")
        self.movementTir()

    def movementTir(self):
        if self.__posX > dicoalien.get(alien1)[0] and self.__posX < dicoalien.get(alien1)[0]+dicoalien.get(alien1)[2] and self.__posY > dicoalien.get(alien1)[1] and self.__posY < dicoalien.get(alien1)[1]+dicoalien.get(alien1)[3]:
            canevas.delete(self.__pattern)
            return
        if self.__posY <=0:
            return
        if True:
            self.__posY -= 6
            canevas.coords(self.__pattern, self.__posX, self.__posY, self.__posX, self.__posY-6)
            mw.after(20,self.movementTir)

class Mur:

    def __init__(self, height, width):
        self.__height = height
        self.__width = width



# création de la fenetre
mw = Tk()
mw.geometry("1000x800")
mw.title("Space Invader")

# création des widgets
quit = Button(mw, text = "Quitter", command = mw.destroy)
quit.pack()
canevas = Canvas(mw, width = LargeurCanevas, height = HauteurCanevas, bg = "grey")
canevas.pack(padx = 5, pady = 5)


vaisseau = Vaisseau(10,700)
canevas.focus_set()
canevas.bind('<Key>',vaisseau.evenement)

alien1 = Alien(240, 300, 50, 50)

alien1.deplacementAlien()

mw.mainloop()

