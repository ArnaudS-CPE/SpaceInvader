# BURLOT Alexandre, SIBENALER Arnaud
# début du projet le 15/12/2020
# Lien GitHub : https://github.com/ArnaudS-CPE/SpaceInvader 
# Objectif : réalisation d'un space invaders sous Tkinter
# TODO : lien du sujet du tp : https://prod.e-campus.cpe.fr/pluginfile.php/53617/mod_resource/content/1/TP3.pdf
# transformer les aliens soit en formes simples soit en images
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
# le tir en rafale à nerf ? ( apparition d'un bool pour les alliés )peut etre accessible en cheat code ?
# ligne 126, si on met moins que 1001 ms de delai, les aliens semblent pas etre correctement supprimés
# les jaunes se décalent petit à petit vers la droite
# pas de focus sur la page d'un nouveau niveau (que sur windows?)
# pour la rafale, mettre deux bind dans le main, un sur Key (pour right et left), l'autre sur KeyRelease (pour espace), scinder la fct
# evenement en deux pour que le bind en appelle une chacun.
# changer vieAlien en int()
# au niveau 6, lors de la deuxième apparition du boss et probablement pour tous les autres, il n'a qu'une vie 

from tkinter import Label, Canvas, Button, Tk, messagebox
from random import choice

LargeurCanevas = 900
HauteurCanevas = 700

DX = 4 # déplacement des aliens en horizontale
DXbonus = 8 # déplacement de l'alien bonus en horizontale
DY=10 # déplacement des aliens en verticale
DXVaisseau = 8 # déplacement du vaisseau en horizontale
freqTirAlienBonus = 1000 # fréquence de tir de l'alien bonus
lengthTir = 6 # taille d'un tir
maxTirs = 5 # nb de tirs alliés max possible sur le terrain


# on définie le nombre de vies de l'alien bonus
vieAlien = []
for i in range(10) :
    vieAlien.append(1)

dicoAlien = {} # contient les objets aliens et leurs informations quand ils sont en vie
dicoMur = {} # contient les murs non détruits
dicoTir = {} # contient les tirs alliés seulement



class Alien:
    global LargeurCanevas, HauteurCanevas, dicoAlien, dicoMur

    def __init__(self, posX, posY, height, width, frequence, vaisseau, canevas, window):
        self.__height = height
        self.__width = width
        self.__posX = posX
        self.__posY = posY
        self.__perdu = False # initie un bool qui dit que le joueur n'est pas en train de perdre
        self.__frequence = frequence
        self.__canv = canevas
        self.__window = window
        self.__ennemi = vaisseau
        if self.__posY == 10: # met la ligne du fond en jaune
            self.__pattern = self.__canv.create_rectangle(posX, posY, posX+width, posY+height, width=3, outline='white', fill='yellow')
        elif self.__posY == 100: # met la ligne du milieu en bleu
            self.__pattern = self.__canv.create_rectangle(posX, posY, posX+width, posY+height, width=3, outline='white', fill='blue')
        else: # met la ligne du devant en rouge
            self.__pattern = self.__canv.create_rectangle(posX, posY, posX+width, posY+height, width=3, outline='white', fill='red')

        dicoAlien[self] = [self.__posX, self.__posY, self.__width, self.__height, 0] # stocke dans un dictionnaire les positions en temps réel des aliens
        self.deplacementAlien() # initie le déplacement de l'alien

    # Getters
    def getPosX(self):
        return self.__posX
    
    def getPosY(self):
        return self.__posY

    def getHeight(self):
        return self.__height

    def getWidth(self):
        return self.__width
    
    def getPattern(self):
        return self.__pattern

    # Setter
    def setPerdu(self):
        self.__perdu = True
        return self.__perdu
    
    def deplacementAlien(self) :
        global DX

        if self.__perdu: # si la valeur de l'attibut perdu est à 'True', tous les aliens se stoppent
            return

        # touche le bord droit du canvas
        if self.__posX+self.__width+DX > LargeurCanevas :
            for key in dicoAlien.keys():
                key.__posY += DY # déplacement vertical vers le bas
                if key != self: # si ce n'est pas l'alien qui vient de vérifier la condition, se déplace vers la gauche 
                    key.__posX -= DX
            self.__posX += DX
            DX = -DX # changement de sens de déplacement  
        
        # touche le bord gauche du canvas
        if self.__posX+DX < 3:
            for key in dicoAlien.keys():
                key.__posY += DY # déplacement vertical vers le bas
            DX = -DX # changement de sens de déplacement
        
        # vérifie la présence de l'alien dans le dictionnaire / si il est touché, pour le supprimer du canevas
        if self not in dicoAlien:
            self.__canv.delete(self.__pattern)
            if dicoAlien == {} : # condition de sortie gagnante du jeu 
                self.__canv.create_text(240, 160, fill = "red", font = "Courier 20 bold", text = "Partie gagnée")
            return

        # condition touche alien / vaisseau
        if (self.__posX+self.__width > self.__ennemi.getPosX() and self.__posX+self.__width < self.__ennemi.getPosX()+self.__ennemi.getWidth() and self.__posY+self.__height > self.__ennemi.getPosY() and self.__posY+self.__height < self.__ennemi.getPosY()+self.__ennemi.getHeight() or 
            self.__posX > self.__ennemi.getPosX() and self.__posX < self.__ennemi.getPosX()+self.__ennemi.getWidth() and self.__posY+self.__height > self.__ennemi.getPosY() and self.__posY+self.__height < self.__ennemi.getPosY()+self.__ennemi.getHeight()):
            self.__canv.create_text(LargeurCanevas//2, HauteurCanevas//2, fill = "red", font = "Courier 20 bold", text = "Fin de partie")
            self.__ennemi.setWinning()
            for key in dicoAlien.keys():
                key.setPerdu() # pour chaque alien, met son attribut __perdu à 'True'

        # condition touche alien / mur
        listeSuppression = []
        for key in dicoMur.keys():
            if (self.__posX+self.__width > dicoMur.get(key)[0] and self.__posX+self.__width < dicoMur.get(key)[0]+dicoMur.get(key)[2] and self.__posY+self.__height > dicoMur.get(key)[1] and self.__posY+self.__height < dicoMur.get(key)[1]+dicoMur.get(key)[3] or 
                self.__posX > dicoMur.get(key)[0] and self.__posX < dicoMur.get(key)[0]+dicoMur.get(key)[2] and self.__posY+self.__height > dicoMur.get(key)[1] and self.__posY+self.__height < dicoMur.get(key)[1]+dicoMur.get(key)[3]):
                listeSuppression.append(key)
        #print(listeSuppression)
        for i in range(len(listeSuppression)-1):
            dicoMur.pop(listeSuppression[i])
            del listeSuppression[i]
            

        self.__posX += DX # déplacement horizontal
        self.__canv.coords(self.__pattern, self.__posX, self.__posY, self.__posX+self.__width, self.__posY+self.__height) # déplacement du pattern de l'alien
        self.__window.after(20, self.deplacementAlien) # boucle de déplacement en continu
        dicoAlien[self] = [self.__posX, self.__posY, self.__width, self.__height, 0] # Update du dicoAlien sur les aliens encore en déplacement

    def createurTir(self):
        # arrête les tirs des aliens si le vaisseau est collisionné avec un alien
        if self.__perdu == True:
            return # fct à vérifier 

        # si tous les aliens sont touchés, arrête les tirs
        if dicoAlien == {} :
            return
        
        alienTireur = choice(list(dicoAlien.keys()))
        posXTir = alienTireur.__posX + (alienTireur.__width//2)
        posYTir =   alienTireur.__posY + alienTireur.__height
        tir = Tir(posXTir, posYTir, 1, self.__ennemi, self.__canv, self.__window) # instancie un objet de type Tir
        del tir # supprime le tir
        self.__canv.after(self.__frequence, self.createurTir)


class Vaisseau:
    global LargeurCanevas, HauteurCanevas

    def __init__(self, posX, posY, canevas, window):
        self.__posX = posX
        self.__posY = posY
        self.__height = 50
        self.__width = 100
        self.__vies = 3
        self.__score = 0
        self.__rafale = False
        self.__canv = canevas
        self.__window = window
        self.__winning = True
        self.__pattern = self.__canv.create_rectangle(self.__posX, self.__posY, self.__posX+self.__width, self.__posY+self.__height, 
            width=2, outline='red', fill='white')
    
    def getPosX(self):
        return self.__posX
    
    def getPosY(self):
        return self.__posY

    def getHeight(self):
        return self.__height

    def getWidth(self):
        return self.__width
    
    def getVies(self):
        return self.__vies

    def setVies(self, newVies):
        self.__vies = newVies

    def getPattern(self):
        return self.__pattern
        
    def getScore(self):
        return self.__score

    def getWinning(self):
        return self.__winning
        
    def getRafale(self):
        return self.__rafale
    
    def setWinning(self):
        self.__winning = False

    def setScore(self, points):
        self.__score += points
    
    def resetRafale(self):
        self.__rafale = False

    def evenement(self, event): # gestion des évènements claviers pour le déplacement et le tir du vaisseau
        global DXVaisseau

        touche = event.keysym
        print(touche) # affiche la touche du clavier, facultatif
        if touche == 'Right': # déplacement à droite
            if self.__posX+self.__width >= LargeurCanevas: # condition d'arret
                pass
            else:
                self.__posX += DXVaisseau
                self.__canv.coords(self.__pattern, self.__posX, self.__posY, self.__posX+self.__width, self.__posY+self.__height)
        
        if touche == 'Left': # déplacement à gauche
            if self.__posX <= 4: # condition d'arret
                pass
            else:
                self.__posX -= DXVaisseau
                self.__canv.coords(self.__pattern, self.__posX, self.__posY, self.__posX+self.__width, self.__posY+self.__height)
        
        if touche == "space": # déclenche le tir du vaisseau
            posXTir = self.__posX + (self.__width//2) # trouve le centre du vaisseau pour lancer le tir
            posYTir = self.__posY
            if len(dicoTir) < maxTirs: # limite le nombre de tirs alliés sur le canvas
                tir = Tir(posXTir, posYTir, 0, self, self.__canv, self.__window) # instancie un objet de type Tir
                del tir # supprime le tir

        # Cheat codes
        if touche == "bar": # ajoute une vie si on appuie sur Shift-Alt-l
            self.setVies(self.__vies+1)
        
        if touche == 'Oacute': # tir en rafale si on appuie sur Shift-Alt-m, à effectuer seulement quand aucun tir alié n'est présent
            for key in dicoTir.keys():
                self.__window.delete(key.getPattern())
                dicoTir.pop(key)
                del key
            self.__rafale = True
            self.__window.after(10000, self.resetRafale)

        

class Tir:
    global dicoAlien, lengthTir, vieAlien

    def __init__(self, posXTir, posYTir, direction, vaisseau, canevas, window):
        self.__posX = posXTir
        self.__posY = posYTir
        self.__length = lengthTir
        self.__direction = direction
        self.__cible = vaisseau
        self.__canv = canevas
        self.__window = window
        if direction == 0 :
            if not self.__cible.getRafale():
                dicoTir[self] = True
            self.__pattern = self.__canv.create_rectangle(posXTir,posYTir,posXTir,posYTir-self.__length, fill = 'black', outline='yellow')
        else:
            self.__pattern = self.__canv.create_rectangle(posXTir,posYTir,posXTir,posYTir+self.__length, fill = 'black', outline='red')
        self.movementTir() # Initie le déplacement du tir
            
    def movementTir(self):
        if self.__direction == 0:
            for key in dicoAlien.keys():
                # gère la collision du tir et d'un alien
                if self.__posX > dicoAlien.get(key)[0] and self.__posX < dicoAlien.get(key)[0]+dicoAlien.get(key)[2] and self.__posY > dicoAlien.get(key)[1] and self.__posY < dicoAlien.get(key)[1]+dicoAlien.get(key)[3]:
                    # cas des aliens normaux
                    if dicoAlien.get(key)[4] == 0 :
                        self.__canv.delete(self.__pattern)
                        if not self.__cible.getRafale():
                            dicoTir.pop(self)
                        dicoAlien.pop(key)
                        self.__cible.setScore(100)
                        return
                    # cas de l'alien bonus
                    if dicoAlien.get(key)[4] == 1 :
                        if len(vieAlien) == 1 :
                            self.__canv.delete(self.__pattern)
                            if not self.__cible.getRafale():
                                dicoTir.pop(self)
                            dicoAlien.pop(key)
                            self.__cible.setScore(500)
                            return
                        else :
                            self.__canv.delete(self.__pattern)
                            if not self.__cible.getRafale():
                                dicoTir.pop(self)
                            vieAlien.pop()
                            return
            for key in dicoMur.keys():
                # gère la collision du tir et d'un mur
                if self.__posX > dicoMur.get(key)[0]-2 and self.__posX < dicoMur.get(key)[0]+dicoMur.get(key)[2]+2 and self.__posY > dicoMur.get(key)[1] and self.__posY < dicoMur.get(key)[1]+dicoMur.get(key)[3]:
                    self.__canv.delete(self.__pattern)
                    if not self.__cible.getRafale():
                        dicoTir.pop(self)
                    dicoMur.pop(key)
                    return
            if self.__posY <=0: # collision avec le haut du canvas
                self.__canv.delete(self.__pattern)
                if not self.__cible.getRafale():
                    dicoTir.pop(self)
                return
            if True: # bouce infinie de déplacement
                self.__posY -= self.__length
                self.__canv.coords(self.__pattern, self.__posX, self.__posY, self.__posX, self.__posY-self.__length)
                self.__window.after(20,self.movementTir)
        else:
            if self.__posX >= self.__cible.getPosX() and self.__posX <= self.__cible.getPosX()+self.__cible.getWidth() and self.__posY >= self.__cible.getPosY() and self.__posY <= self.__cible.getPosY()+self.__cible.getHeight():
                if self.__cible.getVies() != 1:
                    self.__canv.delete(self.__pattern)
                    self.__cible.setVies(self.__cible.getVies()-1)
                    return
                else:
                    print("éliminé")
                    self.__canv.delete(self.__pattern)
                    self.__canv.delete(self.__cible.getPattern())
                    self.__cible.setWinning()
                    self.__cible.setVies(self.__cible.getVies()-1)
                    del self.__cible
                    return
            for key in dicoMur.keys():
                if self.__posX > dicoMur.get(key)[0]-2 and self.__posX < dicoMur.get(key)[0]+dicoMur.get(key)[2]+2 and self.__posY > dicoMur.get(key)[1] and self.__posY < dicoMur.get(key)[1]+dicoMur.get(key)[3]:
                    self.__canv.delete(self.__pattern)
                    dicoMur.pop(key)
                    return
            if self.__posY >= HauteurCanevas:
                self.__canv.delete(self.__pattern)
                return
            elif True:
                self.__posY += self.__length
                self.__canv.coords(self.__pattern, self.__posX, self.__posY, self.__posX, self.__posY+self.__length)
                self.__window.after(20,self.movementTir)


class Mur: # protections pour le vaisseau

    def __init__(self, width, height, posX, posY, canevas, window):
        self.__width = width
        self.__height = height
        self.__posX = posX
        self.__posY = posY
        self.__canv = canevas
        self.__window = window
        self.__pattern = self.__canv.create_rectangle(posX, posY, posX+width, posY+height, width=2, outline='black', fill='grey25')
        dicoMur[self] = [self.__posX, self.__posY, self.__width, self.__height]
        self.verifMur()        
        
    def getPattern(self):
        return self.__pattern
    
    def verifMur(self):
        if self not in dicoMur :
            self.__canv.delete(self.__pattern)
            del self
            return
        self.__window.after(10, self.verifMur)


class AlienBonus:
    global LargeurCanevas, HauteurCanevas, dicoAlien, dicoMur

    def __init__(self, posX, posY, width, height, vaisseau, canevas, window):
        self.__posX = posX
        self.__posY = posY
        self.__width = width
        self.__height = height
        self.__perdu = False
        self.__vies = 3
        self.__canv = canevas
        self.__window = window
        self.__ennemi = vaisseau
        self.__pattern = self.__canv.create_rectangle(self.__posX, self.__posY, self.__posX+self.__width, self.__posY+self.__height, width=2, outline='red', fill='orange')
        dicoAlien[self] = [self.__posX, self.__posY, self.__width, self.__height, 1]
        self.deplacementAlienBonus()

    def setPerdu(self):
        self.__perdu = True
        return self.__perdu

    def deplacementAlienBonus(self) :
        global DXbonus
        # touche le bord droit du canvas
        if self.__posX+self.__width+DXbonus > LargeurCanevas :
            for key in dicoAlien.keys():
                key.__posY += DY # déplacement vertical vers le bas
                if key != self: # si ce n'est pas l'alien qui vient de vérifier la condition, se déplace vers la gauche 
                    key.__posX -= DXbonus
            self.__posX += DXbonus
            DXbonus = -DXbonus # changement de sens de déplacement  
        
        # touche le bord gauche du canvas
        if self.__posX+DXbonus < 3:
            for key in dicoAlien.keys():
                key.__posY += DY # déplacement vertical vers le bas
            DXbonus = -DXbonus # changement de sens de déplacement
        
        # vérifie la présence de l'alien dans le dictionnaire / si il est touché, pour le supprimer du canevas
        if self not in dicoAlien:
            self.__canv.delete(self.__pattern)
            if dicoAlien == {} : # condition de sortie gagnante du jeu 
                self.__canv.create_text(240, 160, fill = "red", font = "Courier 20 bold", text = "Partie gagnée")
            return

        # condition touche alien / vaisseau
        if (self.__posX+self.__width > self.__ennemi.getPosX() and self.__posX+self.__width < self.__ennemi.getPosX()+self.__ennemi.getWidth() and self.__posY+self.__height > self.__ennemi.getPosY() and self.__posY+self.__height < self.__ennemi.getPosY()+self.__ennemi.getHeight() or 
            self.__posX > self.__ennemi.getPosX() and self.__posX < self.__ennemi.getPosX()+self.__ennemi.getWidth() and self.__posY+self.__height > self.__ennemi.getPosY() and self.__posY+self.__height < self.__ennemi.getPosY()+self.__ennemi.getHeight()):
            self.__canv.create_text(LargeurCanevas//2, HauteurCanevas//2, fill = "red", font = "Courier 20 bold", text = "Fin de partie")
            self.__ennemi.setWinning()
            for key in dicoAlien.keys():
                key.setPerdu() # pour chaque alien, met son attribut __perdu à 'True'

        self.__posX += DXbonus # déplacement horizontal
        self.__canv.coords(self.__pattern, self.__posX, self.__posY, self.__posX+self.__width, self.__posY+self.__height) # déplacement du pattern de l'alien
        self.__window.after(20, self.deplacementAlienBonus) # boucle de déplacement en continu
        dicoAlien[self] = [self.__posX, self.__posY, self.__width, self.__height, 1] # Update du dicoAlien sur les aliens encore en déplacement

    def createurTirBonus(self):
        global freqTirAlienBonus

        # arrête les tirs des aliens si le vaisseau est collisionné avec un alien
        if self.__perdu == True:
            return # fct à vérifier 

        # si tous les aliens sont touchés, arrête les tirs
        if dicoAlien == {} :
            return
        
        alienTireur = choice(list(dicoAlien.keys()))
        posXTir = alienTireur.__posX + (alienTireur.__width//2)
        posYTir =   alienTireur.__posY + alienTireur.__height
        tir = Tir(posXTir, posYTir, 1, self.__ennemi, self.__canv, self.__window) # instancie un objet de type Tir
        del tir # supprime le tir
        self.__canv.after(freqTirAlienBonus, self.createurTirBonus)