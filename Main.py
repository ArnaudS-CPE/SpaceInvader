# BURLOT Alexandre, SIBENALER Arnaud
# début du projet le 15/12/2020
# Objectif : réalisation d'un space invader sous Tkinter
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

from tkinter import *


LargeurCanevas = 480
HauteurCanevas = 320
X=50
Y=50
x=240
y=300

DX=3


def deplacementAlien () :
    global X, Y, DX
    if X+12+DX > LargeurCanevas :
        X = 2*(LargeurCanevas-12)-X
        DX = -DX        
    if X-12+DX < 0:
        X = 2*12-X
        DX = -DX
    X=X+DX
    Canevas.coords(Alien, X-12, Y-12, X+12, Y+12)
    Mafenetre.after(20,deplacementAlien)

def deplacementVaisseau (event) :
    global x
    touche = event.keysym
    print(touche)
    if touche == 'Right' :
        x += 5
    if touche == 'Left' :
        x-= 5
    Canevas.coords(Vaisseau, x-15, y-8, x+15, y+8)


# création de la fenêtre principale
Mafenetre = Tk()
Mafenetre.title("Space Invaders")

# création d'un widget canvas
Canevas = Canvas(Mafenetre, height=HauteurCanevas, width=LargeurCanevas, bg='navy')
Canevas.pack(padx=5, pady=5)

# création d'un alien
Alien = Canevas.create_oval(X-12, Y-12, X+12, Y+12, width=3, outline='green', fill='yellow')

# création d'un vaisseau
Vaisseau = Canevas.create_rectangle(x-15, y-8, x+15, y+8, width=2, outline='red', fill='white')

Canevas.focus_set()
Canevas.bind('<Key>',deplacementVaisseau)

deplacementAlien()

Mafenetre.mainloop()