# BURLOT Alexandre, SIBENALER Arnaud
# début du projet le 15/12/2020
# Objectif : bibliothèque de fonctions pour le space invader
# TODO :

from tkinter import *


x = 10
y = 700

def bouger(event):
    global x,y
    touche = event.keysym
    print(touche)
    if touche == 'Right':
        x += 6
        canevas.coords(Vaisseau, x,y,x+50,y+30)
    if touche == 'Left':
        x -= 6
        canevas.coords(Vaisseau, x,y,x+50,y+30)


mw = Tk()
mw.geometry("1000x800")
quit = Button(mw, text = "Quitter", command = mw.destroy)
quit.pack()
canevas = Canvas(mw, width = "900", height = "800", bg = "grey")
canevas.pack(padx = 5, pady = 5)
Vaisseau = canevas.create_rectangle(x, y, x+50, y+30, width=2, outline='red', fill='white')
canevas.focus_set()
canevas.bind('<Key>',bouger)

mw.mainloop()

