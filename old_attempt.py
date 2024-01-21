import pygame
from random import *

TAILLE_CASE = 50

pygame.init()

plateau = []
with open('grille.txt') as level:
    for line in level:
        plateau.append(list(line.rstrip('\n')))

NB_COLONNES = len(plateau[0])
NB_LIGNES = len(plateau)
taille_fenetre = NB_COLONNES * TAILLE_CASE, NB_LIGNES * TAILLE_CASE
NOIR = (000, 000, 000)
BLANC = (255, 255, 255)
GRIS = (127, 127, 127)
ORANGE = (255, 127, 000)
VERT = (000, 255, 000)
screen = pygame.display.set_mode(taille_fenetre)
screen.fill(BLANC)
pygame.display.set_caption('App\'s Game')


def draw_field():
    screen.fill(BLANC)
    for i in range(NB_LIGNES):
        for j in range(NB_COLONNES):
            case = plateau[i][j]
            epaisseur = 1
            couleur = GRIS
            if case == '#':
                epaisseur = 0
                couleur = NOIR
            cx = j * TAILLE_CASE
            cy = i * TAILLE_CASE
            r = pygame.Rect(cx, cy, TAILLE_CASE, TAILLE_CASE)
            pygame.draw.rect(screen, couleur, r, epaisseur)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == 122:
                r = pygame.Rect(3 * TAILLE_CASE, 5 * TAILLE_CASE, TAILLE_CASE, TAILLE_CASE)
                pygame.draw.rect(screen, (000, 000, 000), r, 0)

    draw_field()
    pygame.display.flip()
