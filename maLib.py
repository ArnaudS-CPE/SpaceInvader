# BURLOT Alexandre, SIBENALER Arnaud
# début du projet le 15/12/2020
# Objectif : bibliothèque de fonctions pour le space invader
# TODO :

from tkinter import *
import time 

LargeurCanevas = 900
HauteurCanevas = 800
x = 10
y = 700
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
    canevas.coords(Alien, X-12, Y-12, X+12, Y+12)
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

mw = Tk()
mw.geometry("1000x800")
quit = Button(mw, text = "Quitter", command = mw.destroy)
quit.pack()
canevas = Canvas(mw, width = LargeurCanevas, height = HauteurCanevas, bg = "grey")
canevas.pack(padx = 5, pady = 5)
Vaisseau = canevas.create_rectangle(x, y, x+50, y+30, width=2, outline='red', fill='white')
canevas.focus_set()
canevas.bind('<Key>',evenement)
# Alien = canevas.create_oval(X-12, Y-12, X+12, Y+12, width=3, outline='green', fill='yellow')

mw.mainloop()

