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


from tkinter import Tk, Label, Button, Canvas, messagebox, LabelFrame, PhotoImage
import maLib as mL


def level1():
    # création de la fenetre
    mw = Tk()
    mw.geometry(str(mL.LargeurCanevas+100) + "x" + str(mL.HauteurCanevas))
    mw.title("Space Invader")
    mw.minsize(mL.HauteurCanevas, mL.LargeurCanevas)

    # création des widgets
    canevas = Canvas(mw, width = mL.LargeurCanevas, height = mL.HauteurCanevas, bg = 'grey')
    backgroundPicture = PhotoImage(file = 'Earth.gif')
    canevas.create_image(453,353, image=backgroundPicture)
    
    quit = Button(mw, text = "Quit", command = mw.destroy)
    newGameButton = Button(mw, text = 'New Game', command = lambda:[mw.destroy(),level1()])
    score = Label(mw, text = 'Score : 0')
    vies = Label(mw, text = 'Vies : 3')

    score.grid(row=0, column=0, sticky='NW')
    vies.grid(row=0, column=0, sticky='NE')
    quit.grid(row=3, column=1, sticky='N', padx=5)
    newGameButton.grid(row=2, column=1, sticky='N', padx=5)
    canevas.grid(row=1, column=0, rowspan=3, padx=5)


    
    
    # menu = LabelFrame(mw, text = 'titre du cadre', height = , width = )
    # quit.pack(padx = 5, pady = 5)

    
    # canevas.pack(padx = 5, pady = 5)


    vaisseau = mL.Vaisseau(10,600, canevas, mw)
    canevas.focus_set()
    canevas.bind('<Key>',vaisseau.evenement)

    # ligne 1 d'aliens 
    alien1 = mL.Alien(10, 10, 50, 50, vaisseau, canevas, mw)
    alien2 = mL.Alien(110, 10, 50, 50, vaisseau, canevas, mw)
    alien3 = mL.Alien(210, 10, 50, 50, vaisseau, canevas, mw)
    alien4 = mL.Alien(310, 10, 50, 50, vaisseau, canevas, mw)
    alien5 = mL.Alien(410, 10, 50, 50, vaisseau, canevas, mw)
    alien6 = mL.Alien(510, 10, 50, 50, vaisseau, canevas, mw)
    alien7 = mL.Alien(610, 10, 50, 50, vaisseau, canevas, mw)

    # ligne 2 d'aliens
    alien8 = mL.Alien(10, 100, 50, 50, vaisseau, canevas, mw)
    alien9 = mL.Alien(110, 100, 50, 50, vaisseau, canevas, mw)
    alien10 = mL.Alien(210, 100, 50, 50, vaisseau, canevas, mw)
    alien11 = mL.Alien(310, 100, 50, 50, vaisseau, canevas, mw)
    alien12 = mL.Alien(410, 100, 50, 50, vaisseau, canevas, mw)
    alien13 = mL.Alien(510, 100, 50, 50, vaisseau, canevas, mw)
    alien14 = mL.Alien(610, 100, 50, 50, vaisseau, canevas, mw)

    # ligne 2 d'aliens
    alien15 = mL.Alien(10, 190, 50, 50, vaisseau, canevas, mw)
    alien16 = mL.Alien(110, 190, 50, 50, vaisseau, canevas, mw)
    alien17 = mL.Alien(210, 190, 50, 50, vaisseau, canevas, mw)
    alien18 = mL.Alien(310, 190, 50, 50, vaisseau, canevas, mw)
    alien19 = mL.Alien(410, 190, 50, 50, vaisseau, canevas, mw)
    alien20 = mL.Alien(510, 190, 50, 50, vaisseau, canevas, mw)
    alien21 = mL.Alien(610, 190, 50, 50, vaisseau, canevas, mw)

    alien1.createurTir()

    checkWinning(vaisseau, mw)
    checkScore(score,vaisseau, mw)
    checkVies(vies,vaisseau,mw)

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
            level1() #commande pour recommencer
        elif boiteMessage == 0:
            window.destroy() # commande pour quitter
    window.after(100, lambda:[checkWinning(vaisseau, window)])

def checkScore(score,vaisseau,window):
    if score['text'] != 'Score : '+str(vaisseau.getScore()):
        score['text'] = 'Score : '+str(vaisseau.getScore())
    window.after(100, lambda:[checkScore(score,vaisseau,window)])

def checkVies(vies,vaisseau,window):
    if vies['text'] != 'Vies : '+str(vaisseau.getVies()):
        vies['text'] = 'Vies : '+str(vaisseau.getVies())
    window.after(100, lambda:[checkVies(vies,vaisseau,window)])


level1()
