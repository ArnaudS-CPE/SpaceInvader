# BURLOT Alexandre, SIBENALER Arnaud
# début du projet le 15/12/2020
# Objectif : réalisation d'un space invader sous Tkinter
# TODO : 

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