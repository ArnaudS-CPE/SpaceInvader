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


from tkinter import Tk, Button, Canvas, messagebox
import maLib as mL


def jeu():
    # création de la fenetre
    mw = Tk()
    mw.geometry(str(mL.LargeurCanevas+20) + "x" + str(mL.HauteurCanevas+20))
    mw.title("Space Invader")
    mw.minsize(mL.HauteurCanevas, mL.LargeurCanevas)

    # création des widgets
    quit = Button(mw, text = "Quitter", command = mw.destroy)
    quit.pack(padx = 5, pady = 5)
    canevas = Canvas(mw, width = mL.LargeurCanevas, height = mL.HauteurCanevas, bg = "grey")
    canevas.pack(padx = 5, pady = 5)


    vaisseau = mL.Vaisseau(10,600, canevas, mw)
    canevas.focus_set()
    canevas.bind('<Key>',vaisseau.evenement)

    alien1 = mL.Alien(10, 10, 50, 50, vaisseau, canevas, mw)
    alien2 = mL.Alien(110, 10, 50, 50, vaisseau, canevas, mw)
    alien3 = mL.Alien(210, 10, 50, 50, vaisseau, canevas, mw)
    alien4 = mL.Alien(310, 10, 50, 50, vaisseau, canevas, mw)
    alien5 = mL.Alien(410, 10, 50, 50, vaisseau, canevas, mw)
    alien6 = mL.Alien(510, 10, 50, 50, vaisseau, canevas, mw)
    alien7 = mL.Alien(610, 10, 50, 50, vaisseau, canevas, mw)

    alien1.createurTir()

    checkWinning(vaisseau, mw)

    mur1 = mL.Mur(80, 60, 500, canevas, mw)
    mur2 = mL.Mur(80, 200, 500, canevas, mw)
    mur3 = mL.Mur(80, 340, 500, canevas, mw)
    mur4 = mL.Mur(80, 480, 500, canevas, mw)
    mur5 = mL.Mur(80, 620, 500, canevas, mw)
    mur6 = mL.Mur(80, 760, 500, canevas, mw)

    mw.mainloop()


    
def checkWinning(vaisseau,window):
    if not vaisseau.getWinning():
        boiteMessage = messagebox.askyesno("Perdu", "Vous avez perdu !\n Voulez vous recommencer ?")
        if boiteMessage == 1:
            window.destroy()
            jeu() #commande pour recommencer
        elif boiteMessage == 0:
            window.destroy() # commande pour quitter
    window.after(100, lambda:[checkWinning(vaisseau, window)])

jeu()