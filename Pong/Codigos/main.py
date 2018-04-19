import pygame
import random

pygame.init()


#Tamanha da Tela
display_height = 600
display_width = 1200

#Cores
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

#Tela
screen = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Pong")

#Variável de fim do laço



#Plano de fundo padrão

def plano_padrao():  
    screen.fill(black)
    pygame.draw.line(screen,white,((display_width /2) ,0),((display_width /2),display_height), 3)
    pygame.draw.circle(screen, white,((display_width //2), (display_height //2)), 100, 3)

screen.fill(black)
pygame.draw.line(screen,white,((display_width /2) ,0),((display_width /2),display_height), 3)
pygame.draw.circle(screen, white,((display_width //2), (display_height //2)), 100, 3)


#Bolinha


def bola(x,y):
    pygame.draw.circle(screen, white,(x, y), 5, 3)

def game_loop():
    bol_x = (display_width //2)
    bol_y = (display_height //2)
    x_change = -3
    y_change = -3
    sorte = random.randint(0,1)
    #Decide na sorte para qual lado a bolinha vai sair do meio de campo
    if sorte == 1:
            
            x_change = x_change * -1
            y_change = y_change * 1
    gol = False
    while not gol:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


            

        plano_padrao()
        bol_x += x_change
        bol_y += y_change
        bola(bol_x, bol_y)

        if bol_y < 0 or bol_y > display_height:
            y_change = y_change * -1
        elif bol_x < 0 or bol_x > display_width:
            gol = True
            game_loop()
            
    

 
        pygame.display.update()
game_loop()
