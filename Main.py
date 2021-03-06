# BURLOT Alexandre, SIBENALER Arnaud
# début du projet le 15/12/2020
# Objectif : réalisation d'un space invaders sous Tkinter
# Sujet du tp : https://prod.e-campus.cpe.fr/pluginfile.php/53617/mod_resource/content/1/TP3.pdf
# Lien du répertoire Git : https://github.com/ArnaudS-CPE/SpaceInvader



from tkinter import Tk, Label, Button, Canvas, messagebox, LabelFrame, PhotoImage, Menu
import maLib as mL


frequence = 3001 # fréquence de tir des aliens
viesVaisseau = 3 # vies du vaisseau

def jeu(scoreactuel, niveau):
    global frequence, viesVaisseau

    # création de la fenetre
    mw = Tk()
    mw.geometry(str(mL.LargeurCanevas+100) + "x" + str(mL.HauteurCanevas))
    mw.title("Space Invader")
    mw.minsize(mL.HauteurCanevas, mL.LargeurCanevas)
    
    # création des widgets
    canevas = Canvas(mw, width = mL.LargeurCanevas, height = mL.HauteurCanevas, bg = 'grey')
    if niveau == 0: # image pour l'écran d'acceuil
        backgroundPicture = PhotoImage(file = 'accueil_space_invader.gif')
    elif niveau == -1: # image pour l'écran de game over
        backgroundPicture = PhotoImage(file = 'Game-over.gif')
    else: # image pour les niveau de jeu
        backgroundPicture = PhotoImage(file = 'Earth.gif')
    canevas.create_image(453,353, image=backgroundPicture)
    
    quit = Button(mw, text = "Quit", command = mw.destroy)
    newGameButton = Button(mw, text = 'New Game', command = lambda:[mw.destroy(),jeu(0,1)])
    score = Label(mw, text = 'Score : '+str(scoreactuel))
    vies = Label(mw, text = 'Vies : 3')
    niveauLabel = Label(mw, text = 'Niveau : '+str(niveau))

    # placement des éléments sur la fenêtre 
    score.grid(row=0, column=0, sticky='NW')
    niveauLabel.grid(row=0, column=1, sticky='N')
    vies.grid(row=0, column=2, sticky='NE')
    quit.grid(row=3, column=3, sticky='N', padx=5)
    newGameButton.grid(row=2, column=3, sticky='N', padx=5)
    canevas.grid(row=1, column=0, rowspan=3, columnspan=3, padx=5)

    # création d'un menu
    menuBar = Menu(mw)
    menuJeu = Menu(menuBar, tearoff = 0)
    menuJeu.add_command(label = "New Game", command = lambda:[mw.destroy(),jeu(0,1)])
    menuJeu.add_command(label = "Quit", command = mw.destroy)
    menuBar.add_cascade(label = "Jeu", menu = menuJeu)
    menuaide = Menu(menuBar,tearoff = 0)
    menuaide.add_command(label = "A propos",command = Apropos)
    menuBar.add_cascade(label = "Aide", menu = menuaide)
    mw.config(menu = menuBar)

    if niveau == 0: # niveau 0 (acceuil)
        canevas.create_text(450, 100, fill = "black", font = "Courier 15 bold", text = "Appuyez sur 'New Game' pour démarer la partie !")
    elif niveau == -1: # niveau -1 (game over)
        canevas.create_text(450, 100, fill = "white", font = "Courier 15 bold", text = "Appuyez sur 'New Game' pour recommencer une partie !")
    else: # niveaux >= 1
        # instanciation de l'objet vaisseau
        vaisseau = mL.Vaisseau(10, 600, viesVaisseau, canevas, mw)
        vaisseau.setScore(scoreactuel) # lui donne le score atteint jusque la, vaut 0 si le niveau est à 1
        
        # met le focus sur le canvas pour les actions à effectuer
        canevas.focus_set()
        canevas.bind('<Key>',vaisseau.evenement)

        if niveau%3 != 0: # tous les 3 lvl, c'est l'alien bonus qui apparaît
            # crée la ligne 1 d'aliens 
            alien1 = mL.Alien(10, 10, 50, 50, frequence, vaisseau, canevas, mw)
            alien2 = mL.Alien(110, 10, 50, 50, frequence, vaisseau, canevas, mw)
            alien3 = mL.Alien(210, 10, 50, 50, frequence, vaisseau, canevas, mw)
            alien4 = mL.Alien(310, 10, 50, 50, frequence, vaisseau, canevas, mw)
            alien5 = mL.Alien(410, 10, 50, 50, frequence, vaisseau, canevas, mw)
            alien6 = mL.Alien(510, 10, 50, 50, frequence, vaisseau, canevas, mw)
            alien7 = mL.Alien(610, 10, 50, 50, frequence, vaisseau, canevas, mw)

            # crée la ligne 2 d'aliens 
            alien8 = mL.Alien(10, 100, 50, 50, frequence, vaisseau, canevas, mw)
            alien9 = mL.Alien(110, 100, 50, 50, frequence, vaisseau, canevas, mw)
            alien10 = mL.Alien(210, 100, 50, 50, frequence, vaisseau, canevas, mw)
            alien11 = mL.Alien(310, 100, 50, 50, frequence, vaisseau, canevas, mw)
            alien12 = mL.Alien(410, 100, 50, 50, frequence, vaisseau, canevas, mw)
            alien13 = mL.Alien(510, 100, 50, 50, frequence, vaisseau, canevas, mw)
            alien14 = mL.Alien(610, 100, 50, 50, frequence, vaisseau, canevas, mw)

            # crée la ligne 3 d'aliens 
            alien15 = mL.Alien(10, 190, 50, 50, frequence, vaisseau, canevas, mw)
            alien16 = mL.Alien(110, 190, 50, 50, frequence, vaisseau, canevas, mw)
            alien17 = mL.Alien(210, 190, 50, 50, frequence, vaisseau, canevas, mw)
            alien18 = mL.Alien(310, 190, 50, 50, frequence, vaisseau, canevas, mw)
            alien19 = mL.Alien(410, 190, 50, 50, frequence, vaisseau, canevas, mw)
            alien20 = mL.Alien(510, 190, 50, 50, frequence, vaisseau, canevas, mw)
            alien21 = mL.Alien(610, 190, 50, 50, frequence, vaisseau, canevas, mw)

            alien1.createurTir() # initie le tir des aliens

        else:
            mL.freqTirAlienBonus = int(mL.freqTirAlienBonus / (niveau//3))
            alienbonus = mL.AlienBonus(100, 100, 200, 80, vaisseau, canevas, mw) # instanciation alienbonus
            alienbonus.createurTirBonus() # initie le tir de l'alien

        # lance les actualisaions en temps réel des informations du joueur
        checkWinning(niveau,vaisseau, mw)
        checkScore(score,vaisseau, mw)
        checkVies(vies,vaisseau,mw)

        # blocs de murs
        for k in range(8) :
            for l in range(2) :
                mur1 = mL.Mur(20, 20, 75+k*20, 520+l*20, canevas, mw)

        for k in range(8) :
            for l in range(2) :
                mur2 = mL.Mur(20, 20, 375+k*20, 520+l*20, canevas, mw)

        for k in range(8) :
            for l in range(2) :
                mur3 = mL.Mur(20, 20, 665+k*20, 520+l*20, canevas, mw)

    mw.mainloop() # boucle principale de la fenêtre Tkinter


def checkWinning(niveau,vaisseau,window): # vérifie si le joueur ne perd pas
    global frequence, viesVaisseau
    
    if mL.dicoAlien == {}: # regarde si il reste encore des aliens sur le terrain, condition passage lvl supérieur
        if frequence > 1001: # augmantation de la difficulté par la fréquence des tirs aliens
            frequence -= 250
        viesVaisseau = vaisseau.getVies() # on garde les vies du vaisseau pour avoir 3 vies par partie
        mL.DX = abs(mL.DX) + 1 # augmentation de la vitesse de déplacement horizontal des aliens
        mL.DY = abs(mL.DY) + 2 # augmentation de la vitesse de déplacement vertical des aliens
        scoreactuel = vaisseau.getScore() # on garde le score du vaisseau
        window.destroy() # supprime la fenêtre
        
        # réinitialise les dictionnaires 
        mL.dicoMur = {} 
        mL.dicoTir = {}
        jeu(scoreactuel,niveau+1) #commande pour continuer le jeu
    if not vaisseau.getWinning(): # si le joueur à perdu
        # réinitialisation des dictionnaires
        mL.dicoAlien = {}
        mL.dicoMur = {}
        # réinitialisation des aliens
        mL.DX = 4
        mL.DY = 10
        frequence = 3001
        window.destroy()
        jeu(vaisseau.getScore(), -1)
    window.after(200, lambda:[checkWinning(niveau,vaisseau, window)]) # vérifie toute les 200 ms

def checkScore(score,vaisseau,window):
    if score['text'] != 'Score : '+str(vaisseau.getScore()): # regarde si ca doit changer
        score['text'] = 'Score : '+str(vaisseau.getScore()) # change le texte du label avec la nouvelle valeur
    window.after(100, lambda:[checkScore(score,vaisseau,window)]) # vérifie toute les 100 ms

def checkVies(vies,vaisseau,window):
    if vies['text'] != 'Vies : '+str(vaisseau.getVies()): # regarde si ca doit changer
        vies['text'] = 'Vies : '+str(vaisseau.getVies()) # change le texte du label avec la nouvelle valeur
    window.after(100, lambda:[checkVies(vies,vaisseau,window)]) # vérifie toute les 100 ms
    
def checkNiveau(niveau,niveauLabel,window):
    if niveauLabel['text'] != 'Niveau : '+str(niveau): # regarde si ca doit changer
        niveauLabel['text'] = 'Niveau : '+str(niveau) # change le texte du label avec la nouvelle valeur
    window.after(100, lambda:[checkNiveau(niveau,niveauLabel,window)]) # vérifie toute les 100 ms

def Apropos():
    messagebox.showinfo("A propos","Space Invaders\n\nAlexandre BURLOT\nArnaud SIBENALER")

jeu(0,0) # Lance le jeu au niveau 0 (acceuil)
