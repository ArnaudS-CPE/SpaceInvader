# BURLOT Alexandre, SIBENALER Arnaud
# début du projet le 15/12/2020
# Lien GitHub : https://github.com/ArnaudS-CPE/SpaceInvader
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
# introduire les scores 
# transformer les aliens soit en formes simples soit en images
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
# L'alien le plus à gauche ne suit pas bien le déplacement vers le bas
# L'alien le plus a droite se décale de plus en plus vers la gauche, pas de façon normale
# Faire la condition de collision alien/ Vaisseau
# problème déplacement alien collision à droite


from tkinter import Label, Canvas, Button, Tk, Entry
from random import randint

LargeurCanevas = 900
HauteurCanevas = 700

DX=4
DY=20

dicoalien = {} # contient les objets aliens et leurs informations 


class Alien:
    global LargeurCanevas, HauteurCanevas, dicoalien

    def __init__(self, posX, posY, height, width):
        self.__height = height
        self.__width = width
        self.__posX = posX
        self.__posY = posY
        self.__pattern = canevas.create_rectangle(posX, posY, posX+width, posY+height, width=3, outline='green', fill='yellow')
        dicoalien[self] = [self.__posX, self.__posY, self.__width, self.__height] # stocke dans un dictionnaire les positions en temps réel des aliens
        self.deplacementAlien() # initie le déplacement de l'alien
        self.createurTir() # fait tirer les aliens

    def get_posX(self):
        return self.__posX
    
    def get_posY(self):
        return self.__posY
    
    def set_posY(self, newPosY):
        self.__posY = newPosY
    
    def get_height(self):
        return self.__height

    def get_width(self):
        return self.__width
    
    def get_pattern(self):
        return self.__pattern
    
    def deplacementAlien(self) :
        global DX
        if self.__posX+self.__width > LargeurCanevas : # touche le bord droit du canvas
            self.__posX = LargeurCanevas-self.__width
            for key, value in dicoalien.items():
                key.set_posY(self.__posY+DY) # déplacement vertical
            DX = -DX # changement de sens de déplacement  
        if self.__posX < 3: # touche le bord gauche du canvas
            self.__posX = 0
            for key, value in dicoalien.items():
                key.set_posY(self.__posY+DY)
            DX = -DX # changement de sens de déplacement
        if self.__posY > HauteurCanevas - 100: # condition de fin de partie perdante à revoir avec la collision vaisseau
            canevas.delete(self.__pattern)
            canevas.create_text(LargeurCanevas//2, HauteurCanevas//2, fill = "red", font = "Courier 20 bold", text = "Fin de partie")
        if self not in dicoalien: # vérifie la présence de l'alien dans le dictionnaire / si il est touché, pour le supprimer du canevas
            canevas.delete(self.__pattern)
            if dicoalien == {} : # condition de sortie gagnante du jeu 
                canevas.create_text(240, 160, fill = "red", font = "Courier 20 bold", text = "Partie gagnée")
            return

        #if # condition touche alien / vaisseau

        self.__posX += DX # déplacement horizontal
        canevas.coords(self.__pattern, self.__posX, self.__posY, self.__posX+self.__width, self.__posY+self.__height) # déplacement de l'alien
        mw.after(20, self.deplacementAlien) # déplacement en continu
        dicoalien[self] = [self.__posX, self.__posY, self.__width, self.__height] # Update du dicoalien, pourquoi ça n'en recrée pas un ?

    def createurTir(self):
        randAlien = randint(0,len(dicoalien)-1)
        compteur = 0
        for key, value in dicoalien.items():
            if compteur == randAlien:
                posXTir = key.__posX + (key.__width//2)
                posYTir = key.__posY
                tir = Tir(posXTir, posYTir, 1, self) # instancie un objet de type Tir
                del tir # supprime le tir
            compteur += 1
        mw.after(3000, self.createurTir)


class Vaisseau:
    global LargeurCanevas, HauteurCanevas

    def __init__(self, posX, posY):
        self.__posX = posX
        self.__posY = posY
        self.__height = 50
        self.__width = 100
        self.__vies = 3
        self.__pattern = canevas.create_rectangle(self.__posX, self.__posY, self.__posX+self.__width, self.__posY+self.__height, 
            width=2, outline='red', fill='white')
    
    def get_posX(self):
        return self.__posX
    
    def get_posY(self):
        return self.__posY

    def get_height(self):
        return self.__height

    def get_width(self):
        return self.__width
    
    def get_vies(self):
        return self.__vies

    def set_vies(self, newVies):
        self.__vies = newVies

    def get_pattern(self):
        return self.__pattern

    def evenement(self, event): # gestion des évènements claviers pour le déplacement et le tir du vaisseau
        touche = event.keysym
        print(touche) # affiche la touche du clavier, facultatif
        if touche == 'Right': # déplacement à droite
            if self.__posX+self.__width >= LargeurCanevas: # condition d'arret
                pass
            else:
                self.__posX += 6
                canevas.coords(self.__pattern, self.__posX, self.__posY, self.__posX+self.__width, self.__posY+self.__height)
        
        if touche == 'Left': # déplacement à gauche
            if self.__posX <= 4: # condition d'arret
                pass
            else:
                self.__posX -= 6
                canevas.coords(self.__pattern, self.__posX, self.__posY, self.__posX+self.__width, self.__posY+self.__height)
        
        if touche == "space": # déclenche le tir du vaisseau
            posXTir = self.__posX + (self.__width//2)
            posYTir = self.__posY
            tir = Tir(posXTir, posYTir, 0, self) # instancie un objet de type Tir
            del tir # supprime le tir
        

class Tir:
    global dicoalien
    def __init__(self, posXTir, posYTir, direction, vaisseau):
        self.__posX = posXTir
        self.__posY = posYTir
        self.__direction = direction
        self.__emetteur = vaisseau
        if direction == 0 :
            self.__pattern = canevas.create_rectangle(posXTir,posYTir,posXTir,posYTir-6, fill = "black")
        else:
            self.__pattern = canevas.create_rectangle(posXTir,posYTir,posXTir,posYTir+6, fill = "black")
        self.movementTir() # Initie le déplacement du tir
            
        

    def movementTir(self):
        if self.__direction == 0:
            # gère la collision du tir et d'un alien
            for key, value in dicoalien.items():
                if self.__posX > dicoalien.get(key)[0] and self.__posX < dicoalien.get(key)[0]+dicoalien.get(key)[2] and self.__posY > dicoalien.get(key)[1] and self.__posY < dicoalien.get(key)[1]+dicoalien.get(key)[3]:
                    canevas.delete(self.__pattern)
                    dicoalien.pop(key)
                    return
            if self.__posY <=0: # collision avec le haut du canvas
                return
            if True: # bouce infinie de déplacement
                self.__posY -= 6
                canevas.coords(self.__pattern, self.__posX, self.__posY, self.__posX, self.__posY-6)
                mw.after(20,self.movementTir)
        else:
            if self.__posX > self.__emetteur.get_posX() and self.__posX < self.__emetteur.get_posX()+self.__emetteur.get_width() and self.__posY > self.__emetteur.get_posY() and self.__posY < self.__emetteur.get_posY()+self.__emetteur.get_height():
                canevas.delete(self.__pattern)
                canevas.delete(self.__emetteur.get_pattern())
            if self.__posY >= HauteurCanevas:
                return
            if True:
                self.__posY += 6
                canevas.coords(self.__pattern, self.__posX, self.__posY, self.__posX, self.__posY+6)
                mw.after(20,self.movementTir)

class Mur: # protections pour le vaisseau

    def __init__(self, height, width):
        self.__height = height
        self.__width = width


