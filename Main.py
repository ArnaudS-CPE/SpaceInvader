# BURLOT Alexandre, SIBENALER Arnaud
# début du projet le 15/12/2020
# Objectif : réalisation d'un space invader sous Tkinter
# TODO : lien du sujet du tp : https://prod.e-campus.cpe.fr/pluginfile.php/53617/mod_resource/content/1/TP3.pdf
# Gerer la collision entre le tir et l'Alien, ils doivent tous les deux disparaitres
# Si l'allien arrive au niveau du vaisseau et le touche, le vaiseau est détruit et la partie est terminée
# mettre maintenant plusieur aliens sur la meme ligne et verifier quetout se passe bien
# permettre aux aliens de tirer vers le bas, le déclenchement est aléatoire, même vitesse que ceux du vaiseau
# si un tir alien atteint le vaiseau, les deux sont détruits et la partie est finie
# faire 3 vies pour le joueur et lui afficher
# créer des ilots pour que le vaisseau puisse se cacher, se détruisent petit à petit si ils subissent un tir alien
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

from tkinter import Tk
import maLib as mL


vaisseau = mL.Vaisseau(10,600)
mL.canevas.focus_set()
mL.canevas.bind('<Key>',vaisseau.evenement)

alien1 = mL.Alien(10, 10, 50, 50)
alien2 = mL.Alien(110, 10, 50, 50)
alien3 = mL.Alien(210, 10, 50, 50)
alien4 = mL.Alien(310, 10, 50, 50)
alien5 = mL.Alien(410, 10, 50, 50)
alien6 = mL.Alien(510, 10, 50, 50)
alien7 = mL.Alien(610, 10, 50, 50)

mL.mw.mainloop()