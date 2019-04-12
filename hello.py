import pygame
import os


#setup
pygame.init()
gamedisplay = pygame.display.set_mode((1024, 768))
pygame.display.set_caption("Bobby's Revenge")
clock = pygame.time.Clock()
WHITE=(135, 206, 235)
gamedisplay.fill(WHITE)

#assets
bobby = pygame.image.load('bobby-small.png').convert()
bobbyx = 60
bobbyy = 630

#background
BLUE=(0,0,255)
rect = (0,758,1024,10)
pygame.draw.rect(gamedisplay, BLUE, rect)


crashed = False

while not crashed:
    
    for event in pygame.event.get():
        if(event.type) == pygame.QUIT:
            crashed = True

    #robot movements
    pressed = pygame.key.get_pressed()

    if pressed[pygame.K_LEFT]:
        pygame.draw.rect(gamedisplay, WHITE, bobby.get_rect(topleft=(bobbyx, bobbyy)))
        bobbyx -= 5

    if pressed[pygame.K_RIGHT]:
        pygame.draw.rect(gamedisplay, WHITE, bobby.get_rect(topleft=(bobbyx, bobbyy)))
        bobbyx += 5

    # if pressed[pygame.K_UP]:
    #     bobbyy -= 5

    # if pressed[pygame.K_DOWN]:
    #     bobbyy += 5

    gamedisplay.blit(bobby, (bobbyx, bobbyy))
    pygame.display.update()
    clock.tick(60)

pygame.display.quit()
