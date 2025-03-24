import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

''' 
A música e o som usados nesse projeto são para fins educativos. 
'''
pygame.mixer.music.set_volume(0.1)
musica_fundo = pygame.mixer.music.load("sons/Hang Glider - Pilotwings Resort.mp3")
pygame.mixer.music.play(-1)

som_colisao = pygame.mixer.Sound("sons/smw_coin.wav") # todos os sons sem ser o de fundo deve ser do tipo wav

largura = 640
altura = 480
x = int(largura/2)
y = int(altura/2)

fonte = pygame.font.SysFont('arial', 40, True, True) # fonte, tamanho, negrito, italico
pontos = 0

# Gerar numeros aleatorios para a posição do retangulo azul
x_azul = randint(40,600) # parametros: numeros aleatorios entre 40 e 600
y_azul = randint(50,430)

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Recicla Mack')
relogio = pygame.time.Clock()

# Condição para o jogo não ficar aberto infinitamente
while True:
    relogio.tick(60) # controlador de frames
    tela.fill((0,0,0)) # a tela sempre se manter preta
    mensagem = f'Pontos: {pontos}'
    texto_formatado = fonte.render(mensagem, True, (255,255,255)) # texto, tirar serrilhado, cor do texto

    # condição para o jogo ficar rodando até a gente apertar em sair
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    # Fazer o objeto ser controlado pelo jogador
        '''
        if event.type == KEYDOWN: # se alguma tecla for apertada
            if event.key == K_a:
                x -= 20

            if event.key == K_d:
                x += 20

            if event.key == K_s:
                y += 20

            if event.key == K_w:
                y -= 20
        '''

    if pygame.key.get_pressed()[K_a]: # quando pressionado a tecla, o objeto não para de se mexer
        x -= 20

    if pygame.key.get_pressed()[K_d]: 
        x += 20

    if pygame.key.get_pressed()[K_s]: 
        y += 20

    if pygame.key.get_pressed()[K_w]: 
        y -= 20

    #pygame.draw.circle(tela, (0,255,0), (300, 260), 40) # Circulo, onde o terceiro parametro é a posição xy e o quarto é o raio do circulo
    #pygame.draw.line(tela, (255, 255, 0), (390,0), (390,600),5) # Linha trabalha com ponto, 3º param ponto um, 4º ponto dois, 5º a expessura da linha 

    # Desenhando um retangulo vermelho
    # o sistema de cores é RGB onde 255 é o valor máximo. Nesse caso estou desenhando um retangulo vermelho
    ret_verm = pygame.draw.rect(tela, (255,0,0), (x,y,40,50)) # o segundo parametro são as cores do retangulo e o terceiro o seu tamanho: x, y, largura, altura
    ret_azul = pygame.draw.rect(tela, (0,0,255), (x_azul,y_azul,40,50))

    # Criando colisões entre objetos
    if ret_verm.colliderect(ret_azul):
        x_azul = randint(40,600)
        y_azul = randint(50,430)
        pontos += 1
        som_colisao.play()

    # # fazer o objeto se mover sozinho
    # if y >= altura:
    #     y = 0
    # y += 1

    tela.blit(texto_formatado, (450,40)) # texto para aparecer na tela, posição que vai aparecer na tela
    #sempre atualizar a tela do jogo até sair
    pygame.display.update()