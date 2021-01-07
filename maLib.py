# BURLOT Alexandre, SIBENALER Arnaud
# début du projet le 15/12/2020
# Objectif : réalisation d'un space invaders sous Tkinter
# TODO : lien du sujet du tp : https://prod.e-campus.cpe.fr/pluginfile.php/53617/mod_resource/content/1/TP3.pdf
# afficher les vies du vaisseau
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


from tkinter import Label, Canvas, Button, Tk, messagebox
import random

LargeurCanevas = 900
HauteurCanevas = 700

DX=4
DY=20

dicoalien = {} # contient les objets aliens et leurs informations 
dicomur = {}


class Alien:
    global LargeurCanevas, HauteurCanevas, dicoalien

    def __init__(self, posX, posY, height, width, vaisseau, canevas, mw):
        self.__height = height
        self.__width = width
        self.__posX = posX
        self.__posY = posY
        self.__canv = canevas
        self.__window = mw
        self.__ennemi = vaisseau
        self.__pattern = self.__canv.create_rectangle(posX, posY, posX+width, posY+height, width=3, outline='green', fill='yellow')
        dicoalien[self] = [self.__posX, self.__posY, self.__width, self.__height] # stocke dans un dictionnaire les positions en temps réel des aliens
        self.deplacementAlien() # initie le déplacement de l'alien

    def get_posX(self):
        return self.__posX
    
    def get_posY(self):
        return self.__posY

    def get_height(self):
        return self.__height

    def get_width(self):
        return self.__width
    
    def get_pattern(self):
        return self.__pattern
    
    def deplacementAlien(self) :
        global DX

        if self.__posX+self.__width+DX > LargeurCanevas : # touche le bord droit du canvas
            for key in dicoalien.keys():
                key.__posY += DY # déplacement vertical
                if key != self:
                    key.__posX -= DX
            self.__posX += DX
            DX = -DX # changement de sens de déplacement  
        if self.__posX+DX < 3: # touche le bord gauche du canvas
            for key in dicoalien.keys():
                key.__posY += DY
            DX = -DX # changement de sens de déplacement
        if self.__posY > HauteurCanevas - 100: # condition de fin de partie perdante à revoir avec la collision vaisseau
            self.__canv.delete(self.__pattern)
            self.__canv.create_text(LargeurCanevas//2, HauteurCanevas//2, fill = "red", font = "Courier 20 bold", text = "Fin de partie")
        if self not in dicoalien: # vérifie la présence de l'alien dans le dictionnaire / si il est touché, pour le supprimer du canevas
            self.__canv.delete(self.__pattern)
            if dicoalien == {} : # condition de sortie gagnante du jeu 
                self.__canv.create_text(240, 160, fill = "red", font = "Courier 20 bold", text = "Partie gagnée")
            return

        #if # condition touche alien / vaisseau

        self.__posX += DX # déplacement horizontal
        self.__canv.coords(self.__pattern, self.__posX, self.__posY, self.__posX+self.__width, self.__posY+self.__height) # déplacement de l'alien
        self.__window.after(20, self.deplacementAlien) # déplacement en continu
        dicoalien[self] = [self.__posX, self.__posY, self.__width, self.__height] # Update du dicoalien, pourquoi ça n'en recrée pas un ?

    def createurTir(self):
        alienTireur = random.choice(list(dicoalien.keys()))
        posXTir = alienTireur.__posX + (alienTireur.__width//2)
        posYTir =   alienTireur.__posY + alienTireur.__height
        tir = Tir(posXTir, posYTir, 1, self.__ennemi, self.__canv, self.__window) # instancie un objet de type Tir
        del tir # supprime le tir
        self.__canv.after(3000, self.createurTir)


class Vaisseau:
    global LargeurCanevas, HauteurCanevas

    def __init__(self, posX, posY, canevas, mw):
        self.__posX = posX
        self.__posY = posY
        self.__height = 50
        self.__width = 100
        self.__vies = 1
        self.__canv = canevas
        self.__window = mw
        self.__winning = True
        self.__pattern = self.__canv.create_rectangle(self.__posX, self.__posY, self.__posX+self.__width, self.__posY+self.__height, 
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

    def get_winning(self):
        return self.__winning
    
    def set_winning(self):
        self.__winning = False

    def evenement(self, event): # gestion des évènements claviers pour le déplacement et le tir du vaisseau
        touche = event.keysym
        # print(touche) # affiche la touche du clavier, facultatif
        if touche == 'Right': # déplacement à droite
            if self.__posX+self.__width >= LargeurCanevas: # condition d'arret
                pass
            else:
                self.__posX += 6
                self.__canv.coords(self.__pattern, self.__posX, self.__posY, self.__posX+self.__width, self.__posY+self.__height)
        
        if touche == 'Left': # déplacement à gauche
            if self.__posX <= 4: # condition d'arret
                pass
            else:
                self.__posX -= 6
                self.__canv.coords(self.__pattern, self.__posX, self.__posY, self.__posX+self.__width, self.__posY+self.__height)
        
        if touche == "space": # déclenche le tir du vaisseau
            posXTir = self.__posX + (self.__width//2)
            posYTir = self.__posY
            tir = Tir(posXTir, posYTir, 0, self, self.__canv, self.__window) # instancie un objet de type Tir
            del tir # supprime le tir
       

class Tir:
    global dicoalien
    def __init__(self, posXTir, posYTir, direction, vaisseau, canevas, mw):
        self.__posX = posXTir
        self.__posY = posYTir
        self.__direction = direction
        self.__cible = vaisseau
        self.__canv = canevas
        self.__window = mw
        if direction == 0 :
            self.__pattern = self.__canv.create_rectangle(posXTir,posYTir,posXTir,posYTir-6, fill = "black")
        else:
            self.__pattern = self.__canv.create_rectangle(posXTir,posYTir,posXTir,posYTir+6, fill = "black")
        self.movementTir() # Initie le déplacement du tir
            
        

    def movementTir(self):
        if self.__direction == 0:
            # gère la collision du tir et d'un alien
            for key in dicoalien.keys():
                if self.__posX > dicoalien.get(key)[0] and self.__posX < dicoalien.get(key)[0]+dicoalien.get(key)[2] and self.__posY > dicoalien.get(key)[1] and self.__posY < dicoalien.get(key)[1]+dicoalien.get(key)[3]:
                    self.__canv.delete(self.__pattern)
                    dicoalien.pop(key)
                    return
            for key in dicomur.keys():
                if self.__posX > dicomur.get(key)[0] and self.__posX < dicomur.get(key)[0]+dicomur.get(key)[2] and self.__posY > dicomur.get(key)[1] and self.__posY < dicomur.get(key)[1]+dicomur.get(key)[3]:
                    self.__canv.delete(self.__pattern)
                    dicomur.pop(key)
                    return
            if self.__posY <=0: # collision avec le haut du canvas
                return
            if True: # bouce infinie de déplacement
                self.__posY -= 6
                self.__canv.coords(self.__pattern, self.__posX, self.__posY, self.__posX, self.__posY-6)
                self.__window.after(20,self.movementTir)
        else:
            if self.__posX >= self.__cible.get_posX() and self.__posX <= self.__cible.get_posX()+self.__cible.get_width() and self.__posY >= self.__cible.get_posY() and self.__posY <= self.__cible.get_posY()+self.__cible.get_height():
                if self.__cible.get_vies() != 1:
                    self.__canv.delete(self.__pattern)
                    print("-1")
                    self.__cible.set_vies(self.__cible.get_vies()-1)
                    return
                else:
                    print("éliminé")
                    self.__canv.delete(self.__pattern)
                    self.__canv.delete(self.__cible.get_pattern())
                    self.__cible.set_winning()
                    # del le vaisseau
            for key in dicomur.keys():
                if self.__posX > dicomur.get(key)[0] and self.__posX < dicomur.get(key)[0]+dicomur.get(key)[2] and self.__posY > dicomur.get(key)[1] and self.__posY < dicomur.get(key)[1]+dicomur.get(key)[3]:
                    self.__canv.delete(self.__pattern)
                    dicomur.pop(key)
                    return
            if self.__posY >= HauteurCanevas:
                return
            elif True:
                self.__posY += 6
                self.__canv.coords(self.__pattern, self.__posX, self.__posY, self.__posX, self.__posY+6)
                self.__window.after(20,self.movementTir)

class Mur: # protections pour le vaisseau

    def __init__(self, width, posX, posY, canevas, mw):
        self.__width = width
        self.__posX = posX
        self.__posY = posY
        self.__canv = canevas
        self.__window = mw
        self.__pattern = self.__canv.create_rectangle(posX, posY, posX+width, posY+30, width=3, outline='black', fill='grey25')
        dicomur[self] = [self.__posX, self.__posY, self.__width, 30]
        self.verifMur()        
        
    def get_pattern(self):
        return self.__pattern
    
    def verifMur(self):
        if self not in dicomur :
            self.__canv.delete(self.__pattern)
        self.__window.after(10, self.verifMur)
