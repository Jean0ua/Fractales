

from turtle import *

def m1(taille):                # Définition du motif élémentaire - carré rempli
    fillcolor("black")         # couleur de remplissage
    begin_fill()               # commence le remplissage
    for i in range(4):
        forward(taille)
        left(90)
    end_fill()                 # termine le remplissage



def courbe(longueur, niveau, motif):  # pour dessiner la fractale
    if niveau == 1:
        motif(longueur)               # dessine le motif de niveau 0
    elif niveau == 0:
        up()                          # lève le stylo
    else:
        longueur = longueur / 3       # réduit la taille d'un tiers
        niveau = niveau - 1

        # Ligne du haut (3 carrés)
        courbe(longueur, niveau, motif)
        up()
        forward(longueur)
        down()
        courbe(longueur, niveau, motif)
        up()
        forward(longueur)
        down()
        courbe(longueur, niveau, motif)

        # Descend à la ligne du milieu
        up()
        backward(longueur * 2)
        right(90)
        forward(longueur)
        left(90)
        down()

        # Ligne du milieu (carré gauche et droit, pas le centre)
        courbe(longueur, niveau, motif)
        up()
        forward(longueur * 2)
        down()
        courbe(longueur, niveau, motif)

        # Descend à la ligne du bas
        up()
        backward(longueur * 2)
        right(90)
        forward(longueur)
        left(90)
        down()

        # Ligne du bas (3 carrés)
        courbe(longueur, niveau, motif)
        up()
        forward(longueur)
        down()
        courbe(longueur, niveau, motif)
        up()
        forward(longueur)
        down()
        courbe(longueur, niveau, motif)

        # Retour à la position de départ
        up()
        backward(longueur * 2)
        left(90)
        forward(longueur * 2)
        right(90)
        down()

up()                             # lève le stylo
goto(-200, 200)                  # position de départ
down()                           # abaisse le stylo
speed(100)                         # vitesse maximale
ht()                             # hide turtle: cache la tortue
width(1)                         # taille du trait
color("black")                   # couleur du trait

# appelle la fonction (taille de départ, niveau de profondeur, fonction pour qui dessine le motif)
courbe(300, 4, m1)

n=int(input("1 pour quitter"))   # pour que la fenêtre ne se ferme pas
if n==1:
    bye()