import pygame
import sys
import random

# Initialisation de Pygame
pygame.init()

# Définir des couleurs
noir = (0, 0, 0)
vert = (0, 255, 0)
rouge = (255, 0, 0)
blanc = (255, 255, 255)

# Définir la taille de la fenêtre
largeur, hauteur = 800, 600
fenetre = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Snake Game")

# Définir la taille d'une cellule du serpent
taille_cellule = 20

# Initialiser la position et la direction du serpent
serpent = [(100, 100), (90, 100), (80, 100)]
direction = (1, 0)

# Initialiser la position de la pomme
pomme = (largeur // 2, hauteur // 2)

# Définir la vitesse du serpent
vitesse = 10
fps = pygame.time.Clock()

# Initialiser le score
score = 0

# Font pour le score et le menu
font_score = pygame.font.Font(None, 36)
font_menu = pygame.font.Font(None, 48)

# Fonction pour afficher le menu de fin
def afficher_menu_fin():
    menu_fin = True
    while menu_fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return  # Relancer le jeu

        fenetre.fill(noir)
        score_text = font_score.render(f"Score: {score}", True, blanc)
        fenetre.blit(score_text, (largeur // 2 - 70, hauteur // 2 - 50))

        texte_menu = font_menu.render("Appuyez sur Entrée pour rejouer", True, blanc)
        fenetre.blit(texte_menu, (largeur // 2 - 220, hauteur // 2 + 20))

        pygame.display.flip()
        fps.tick(5)

# Boucle principale du jeu
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != (0, 1):
                direction = (0, -1)
            elif event.key == pygame.K_DOWN and direction != (0, -1):
                direction = (0, 1)
            elif event.key == pygame.K_LEFT and direction != (1, 0):
                direction = (-1, 0)
            elif event.key == pygame.K_RIGHT and direction != (-1, 0):
                direction = (1, 0)

    # Mettre à jour la position du serpent
    tête = (serpent[0][0] + direction[0] * taille_cellule, serpent[0][1] + direction[1] * taille_cellule)
    serpent.insert(0, tête)

    # Vérifier si le serpent a mangé la pomme
    if tête == pomme:
        pomme = (random.randint(0, (largeur - taille_cellule) // taille_cellule) * taille_cellule,
                 random.randint(0, (hauteur - taille_cellule) // taille_cellule) * taille_cellule)
        score += 100

    else:
        serpent.pop()

    # Vérifier si le serpent a touché les bords ou s'est mordu la queue
    if tête[0] < 0 or tête[0] >= largeur or tête[1] < 0 or tête[1] >= hauteur or tête in serpent[1:]:
        afficher_menu_fin()
        # Réinitialiser le jeu après avoir fermé le menu de fin
        serpent = [(100, 100), (90, 100), (80, 100)]
        direction = (1, 0)
        pomme = (largeur // 2, hauteur // 2)
        score = 0

    # Afficher le serpent, la pomme et le score
    fenetre.fill(noir)
    for position in serpent:
        pygame.draw.rect(fenetre, vert, (position[0], position[1], taille_cellule, taille_cellule))

    pygame.draw.rect(fenetre, rouge, (pomme[0], pomme[1], taille_cellule, taille_cellule))

    # Ajouter des yeux au serpent
    tête_centre = (tête[0] + taille_cellule // 2, tête[1] + taille_cellule // 2)
    œil_gauche = (tête_centre[0] - taille_cellule // 4, tête_centre[1] - taille_cellule // 4)
    œil_droit = (tête_centre[0] + taille_cellule // 4, tête_centre[1] - taille_cellule // 4)
    pygame.draw.circle(fenetre, noir, œil_gauche, taille_cellule // 8)
    pygame.draw.circle(fenetre, noir, œil_droit, taille_cellule // 8)

    # Afficher le score en haut à gauche
    score_text = font_score.render(f"Score: {score}", True, blanc)
    fenetre.blit(score_text, (10, 10))

    pygame.display.flip()

    # Contrôler la fréquence d'images
    fps.tick(vitesse)
