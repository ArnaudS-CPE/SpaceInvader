# BURLOT Alexandre, SIBENALER Arnaud
# début du projet le 15/12/2020
# Objectif : réalisation d'un space invader sous Tkinter
# TODO : 

from tkinter import *


LargeurCanevas = 480
HauteurCanevas = 320
X=50
Y=50
DX=3


def deplacement () :
    global X, Y, DX
    if X-12+DX > LargeurCanevas :
        X = 2*(LargeurCanevas-12)-X
        DX = -DX        
    if X-12+DX < 0:
        X = 2*12-X
        DX = -DX
    X=X+DX
    Canevas.coords(Alien, X-12, Y-12, X+12, Y+12)
    Mafenetre.after(20,deplacement)

# création de la fenêtre principale
Mafenetre = Tk()
Mafenetre.title("Space Invaders")

# création d'un widget canvas
Canevas = Canvas(Mafenetre, height=HauteurCanevas, width=LargeurCanevas, bg='navy')
Canevas.pack(padx=5, pady=5)

# création d'un objet
Alien = Canevas.create_oval(X-12, Y-12, X+12, Y+12, width=3, outline='green', fill='yellow')


deplacement()

Mafenetre.mainloop()