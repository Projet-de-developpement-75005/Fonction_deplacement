import math


# Couleurs
ROUGE = (200, 0, 0)
BLEU = (0, 0, 200)

# Paramètres du robot
ROBOT_LONGUEUR = 60
ROBOT_LARGEUR = 30

class Robot:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.angle = 0  # Orientation du robot
        self.vitesse_roue_gauche = 0
        self.vitesse_roue_droite = 0

    

    def deplacer(self):
        """Déplace le robot en fonction des vitesses des roues."""
        vitesse_moyenne = (self.vitesse_roue_gauche + self.vitesse_roue_droite) / 2
        difference_vitesse = self.vitesse_roue_droite - self.vitesse_roue_gauche

        self.angle += difference_vitesse * 0.5  # Rotation
        self.x += math.cos(math.radians(self.angle)) * vitesse_moyenne
        self.y += math.sin(math.radians(self.angle)) * vitesse_moyenne


    def limiter_position(self, largeur_fenetre, hauteur_fenetre):
        """Empêche le robot de sortir des limites."""
        self.x = max(ROBOT_LONGUEUR // 2, min(self.x, largeur_fenetre - ROBOT_LONGUEUR // 2))
        self.y = max(ROBOT_LARGEUR // 2, min(self.y, hauteur_fenetre - ROBOT_LARGEUR // 2))
        
    