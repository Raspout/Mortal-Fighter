import pygame
import os

ROUGE = (255,0,0)
WIDTH = 600
HEIGHT = 400
BLANC = (255,255,255)


curdir = os.path.dirname(__file__)

class Balle(pygame.sprite.Sprite):
  def __init__(self, screen_width, screen_height):
    # Initialisation
    pygame.sprite.Sprite.__init__(self)

    # Se souvenir des dimensions de l'écran
    self.sw = screen_width
    self.sh = screen_height

    # Charger les images d'un bonhomme qui marche
    self.img = []
    for i in range(10):
      image = pygame.image.load(f's1.png/s2.png').convert_alpha()
      self.img.append(image)
    # Définir la première image
    self.image = self.img[0]

    # Rectangle pour les collisions
    self.rect = self.image.get_rect()

    # Position et vitesse initiales
    self.rect.bottom = self.sh
    self.dx = 3
    self.compteur = 0

  def update(self):
    # Déplacement
    self.rect.x += self.dx

    # Modification de l'image ?
    self.image = self.img[(self.compteur//2)%10]
    self.compteur += 1

    # Sortie à droite -> entrée à gauche
    if self.rect.left >= self.sw:
      self.rect.right = 0


# Démarrer la bibliothèque
pygame.init()

# Définir la taille de la fenêtre en pixels
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Progamme pygame")

# Horloge pour contrôler le fps
clock = pygame.time.Clock()

# Créer le sprite et l'ajouter à un groupe de sprites
b = Balle(WIDTH, HEIGHT)
mes_sprites = pygame.sprite.Group()
mes_sprites.add(b)

# Boucle principale
continuer = True
while continuer:
  # Gestion des évènements
  # (comme la fermeture de la fenêtre)
  for e in pygame.event.get():
    if e.type == pygame.QUIT:
      continuer = False

  #########################
  # Instructions de mise 
  # à jour du contenu de 
  # la fenètre 
  mes_sprites.update()

  #########################
  # Instructions de dessin
  screen.fill(BLANC)
  mes_sprites.draw(screen)

  #########################
  # raffraichir l'affichage
  pygame.display.flip()

  # fps: ici 30 image par seconde
  clock.tick(30)

# Terminer l'application
pygame.quit()
quit()