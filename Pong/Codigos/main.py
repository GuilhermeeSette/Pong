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
player_height = 100
player_width = 20



def player1(pl_x,pl_y):
    pygame.draw.rect(screen, white,(pl_x, pl_y, player_width, player_height))

def bola(x,y):
    pygame.draw.circle(screen, white,(x, y), 5, 3)

def game_loop():
    bol_x = (display_width //2)
    bol_y = (display_height //2)
    pl_x = (display_width - player_width)
    pl_y = (display_height// 2)
    x_change = -1
    y_change = -1
    py_change = 0
    sorte = 1#random.randint(0,1)
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
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    py_change = -2
                elif event.key == pygame.K_DOWN:
                    py_change = 2

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    py_change = 0


        plano_padrao()
        bol_x += x_change
        bol_y += y_change
        pl_y += py_change
        player1(pl_x,pl_y)
        bola(bol_x, bol_y)
        

        if bol_y < 0 or bol_y > display_height:
            y_change = y_change * -1
        elif bol_x == display_width -  player_width:
            if bol_y  >= pl_y  and bol_y <= pl_y + player_height:
             x_change = x_change * -1
        elif bol_x < 0 or bol_x > display_width:
            gol = True
            game_loop()
            
    
        pygame.display.update()
game_loop()
