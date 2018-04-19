import pygame

pygame.init()


#Tamanha da Tela
display_height = 600
display_width = 800
#Cores
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

#Tela
screen = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Pong")

#Variável de fim do jogo
finish = False



screen.fill(white)

#pygame.draw.rect(screen,black,[50,50,50,50])

pygame.display.update()
