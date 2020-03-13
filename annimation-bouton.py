import pygame
import math
import pygame.image
import pygame.font
import pygame.mixer

Width = 300
Height = 300
v = 1.1
togle1 = True
compte = 0
y = 20
togle2 = True

pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((Width,Height))
police = pygame.font.SysFont('comicsans', 30, True, True)
clock = pygame.time.Clock()

continuer = True
while continuer:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            continuer = False
           
###################################################################
    
    screen.fill((0,0,0))
    pygame.draw.rect(screen, (255,255,255), (145,y,10,10))
    if v <= 0:
        togle1 = True
        togle2 = not(togle2)
    if v >= 3:
        togle1 = False
    if togle1 == True:
        v = v+0.1
    if togle1 == False:
        v = v-0.1
    if togle2 == True:
        y = y+v
    if togle2 == False:
        y = y-v

######################################################################

    pygame.display.flip()
    clock.tick(30)
pygame.quit()
quit()

