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

x_cobra = int(largura/2)
y_cobra = int(altura/2)

velocidade = 5
x_controle = velocidade
y_controle = 0

fonte = pygame.font.SysFont('arial', 40, True, True) # fonte, tamanho, negrito, italico
pontos = 0

# Gerar numeros aleatorios para a posição do retangulo azul
x_maca = randint(40,600) # parametros: numeros aleatorios entre 40 e 600
y_maca = randint(50,430)

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Recicla Mack')
relogio = pygame.time.Clock()

morreu = False

lista_cobra = []
comprimento_inicial = 5

def aumenta_cobra(lista_cobra):
    for XeY in lista_cobra:
        pygame.draw.rect(tela, (0,255,0), (XeY[0], XeY[1], 20, 20))

def reiniciar_jogo():
    global pontos, comprimento_inicial, x_cobra, y_cobra, lista_cobra, lista_cabeca, x_maca, y_maca, morreu

    pontos = 0
    comprimento_inicial = 5
    x_cobra = int(largura/2)
    y_cobra = int(altura/2)
    lista_cobra = []
    lista_cabeca = []
    x_maca = randint(40,600) 
    y_maca = randint(50,430)
    morreu = False

# Condição para o jogo não ficar aberto infinitamente
while True:
    relogio.tick(60) # controlador de frames
    tela.fill((255,255,255)) # a tela sempre se manter preta
    mensagem = f'Pontos: {pontos}'
    texto_formatado = fonte.render(mensagem, True, (0,0,0)) # texto, tirar serrilhado, cor do texto

    # condição para o jogo ficar rodando até a gente apertar em sair
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    # Fazer o objeto ser controlado pelo jogador
        if event.type == KEYDOWN: # se alguma tecla for apertada
            if event.key == K_a:
                if x_controle == velocidade:
                    pass
                else:
                    x_controle = -velocidade
                    y_controle = 0
            if event.key == K_d:
                if x_controle == -velocidade:
                    pass
                else:
                    x_controle = velocidade
                    y_controle = 0
            if event.key == K_w:
                if y_controle == velocidade:
                    pass
                else:
                    x_controle = 0
                    y_controle = -velocidade
            if event.key == K_s:
                if y_controle == -velocidade:
                    pass
                else:
                    x_controle = 0
                    y_controle = velocidade

    x_cobra += x_controle
    y_cobra += y_controle
       
    # if pygame.key.get_pressed()[K_a]: # quando pressionado a tecla, o objeto não para de se mexer
    #     x_cobra -= 10

    # if pygame.key.get_pressed()[K_d]: 
    #     x_cobra += 10

    # if pygame.key.get_pressed()[K_s]: 
    #     y_cobra += 10

    # if pygame.key.get_pressed()[K_w]: 
    #     y_cobra -= 10

    #pygame.draw.circle(tela, (0,255,0), (300, 260), 40) # Circulo, onde o terceiro parametro é a posição xy e o quarto é o raio do circulo
    #pygame.draw.line(tela, (255, 255, 0), (390,0), (390,600),5) # Linha trabalha com ponto, 3º param ponto um, 4º ponto dois, 5º a expessura da linha 

    # Desenhando um retangulo vermelho
    # o sistema de cores é RGB onde 255 é o valor máximo. Nesse caso estou desenhando um retangulo vermelho
    cobra = pygame.draw.rect(tela, (0,255,0), (x_cobra,y_cobra,20,20)) # o segundo parametro são as cores do retangulo e o terceiro o seu tamanho: x, y, largura, altura
    maca = pygame.draw.rect(tela, (255,0,0), (x_maca,y_maca,20,20))

    # Criando colisões entre objetos
    if cobra.colliderect(maca):
        x_maca = randint(40,600)
        y_maca = randint(50,430)
        pontos += 1
        som_colisao.play()

        comprimento_inicial += 1

    lista_cabeca = []
    lista_cabeca.append(x_cobra)
    lista_cabeca.append(y_cobra)

    lista_cobra.append(lista_cabeca)

    if lista_cobra.count(lista_cabeca) > 1:
        fonte2 = pygame.font.SysFont('arial', 20, True, True)
        mensagem = 'Game Over! Pressione R para jogar novamente'
        texto_formatado = fonte2.render(mensagem, True, (0,0,0))
        ret_texto = texto_formatado.get_rect()
        morreu = True

        while morreu:
            tela.fill((255, 255, 255))

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        reiniciar_jogo()

            ret_texto.center = (largura//2, altura//2)
            tela.blit(texto_formatado, ret_texto)
            pygame.display.update()

    if x_cobra > largura:
        x_cobra = 0
    if x_cobra < 0:
        x_cobra = largura
    if y_cobra < 0:
        y_cobra = altura
    if y_cobra > altura:
        y_cobra = 0

    if len(lista_cobra) > comprimento_inicial:
        del lista_cobra[0]

    aumenta_cobra(lista_cobra)

    # # fazer o objeto se mover sozinho
    # if y >= altura:
    #     y = 0
    # y += 1

    tela.blit(texto_formatado, (450,40)) # texto para aparecer na tela, posição que vai aparecer na tela
    #sempre atualizar a tela do jogo até sair
    pygame.display.update()