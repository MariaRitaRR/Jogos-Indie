import pygame 
from pygame import mixer
from time import sleep
from random import randint
from random import Random


pygame.init()
mixer.init()

# som_missil = mixer.music.load('som-laser.mp3')

# som_explosao = pygame.mixer.Sound('som-explosao.ogg')

x,y = (960 , 540)
janela = pygame.display.set_mode([x, y]) #define o tamanho da janela
pygame.display.set_caption("Meu Primeiro Jogo") #define o título da janela

#IMPORTAÇÃO DE IMAGENS
imagem_fundo = pygame.image.load("images/space bg game.png")
nave_player = pygame.image.load("images/sprite_nave_pequena.png")
nave_inimiga = pygame.image.load("images/nave_inimiga_pequena.png")
missil_pequeno = pygame.image.load("images/missil_pequeno.png")
missil_pequeno = pygame.transform.scale(missil_pequeno, (30,30))


tiro_alvo = False

#POSIÇÃO PLAYER
pos_x_player = 400
pos_y_player= 420
vel_nave_player = 10

#POSIÇÃO INIMIGO
pos_x_inimigo = 430
pos_y_inimigo = 50
vel_nave_inimigo = 15

#POSIÇÃO MISSIL
pos_x_missil = 430
pos_y_missil = 450
vel_x_missil = 10

pontuacao = 0


loop = True

while loop:

    for events in pygame.event.get():

        if events.type == pygame.QUIT:
            loop = False
    teclas = pygame.key.get_pressed()

    #MOVIMENTAÇÃO DO PLAYER
    if (teclas[pygame.K_UP] and pos_y_player > 1):
        #faz a nave subir
        pos_y_player -= vel_nave_player
        if not tiro_alvo:
            pos_y_missil -= vel_x_missil
            vel_x_missil = 10


    if (teclas[pygame.K_DOWN] and pos_y_player < 440):
        #faz a nave descer
        pos_y_player += vel_nave_player
        if not tiro_alvo:
            pos_y_missil += vel_x_missil
            vel_x_missil = 10


    if teclas[pygame.K_LEFT]:
        pos_x_player -= vel_nave_player
    
    if teclas[pygame.K_RIGHT]:
        pos_x_player += vel_nave_player

    
    #MOVIMENTAÇÃO DO INIMIGO
    pos_y_inimigo += vel_nave_inimigo
    if (pos_y_inimigo > 530):
        random_y = randint(1,440)
        random_x = randint(1,870)
        pos_y_inimigo -= 450
        pos_y_inimigo = random_y
        pos_x_inimigo = random_x
       
       

    janela.blit(imagem_fundo, (0,0)) #o quanto minha imagem vai ocupar, no caso a tela toda
    janela.blit(nave_player,(pos_x_player,pos_y_player))
    janela.blit(nave_inimiga,(50,50))
    # janela.blit()
    


    pygame.display.update()