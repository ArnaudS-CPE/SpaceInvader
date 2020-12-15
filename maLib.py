# BURLOT Alexandre, SIBENALER Arnaud
# début du projet le 15/12/2020
# Objectif : bibliothèque de fonctions pour le space invader
# TODO :

from tkinter import Tk, Label, Button, Canvas, ALL


mw = Tk()
mw.geometry("1000x800")
quit = Button(mw, text = "Quitter", command = mw.destroy)
quit.pack()
canevas = Canvas(mw, width = "900", height = "800", bg = "grey")
canevas.pack(padx = 5, pady = 5)
x = 0
y = 0
while True:
    x += 1
    y = y
    canevas.delete("all")
    canevas.create_rectangle(x,y,x+50,y+30, outline = "red", fill = "blue")
    mw.mainloop()
