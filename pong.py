from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *
from random import randint

# Inicialização
janela = Window(1024, 768)
janela.set_title('GameDemo - Luiz Willner')
# janela.update()
teclado = Window.get_keyboard()

background = GameImage('sw_background.jpg')
bolinha = Sprite('ball.png', 1)
bolinha2 = Sprite('ball2.png', 1)
pad_right = Sprite('pad.png', 1)
pad_left = Sprite('pad.png', 1)

random = (-1, 1)

# Placar
score_left = 0
score_right = 0

# Contadores
fps = 0
fps_register = '--'
hit_contador = 0
tempo = 0

# Posição inicial bolinha(s)
bolinha.x = janela.width/2 - bolinha.width/2
bolinha.y = janela.height/2 - bolinha.height/2
bolinha2.x = janela.width/2 - bolinha2.width/2
bolinha2.y = janela.height/2 - bolinha2.height/2

# Posição inicial dos Pads
pad_right.x = 5
pad_right.y = janela.height / 2 - pad_right.height / 2
pad_left.x = janela.width - pad_left.width - 5
pad_left.y = janela.height / 2 - pad_left.height / 2

# Velocidades
# bolinha 1
vel_x1 = 250
init_vel_x1 = vel_x1
vel_y1 = 250
init_vel_y1 = vel_y1

# bolinha 2
vel_x2 = 250
init_vel_x2 = vel_x2
vel_y2 = 250
init_vel_y2 = vel_y2

# pads
vel_pad = 500

# GameLoop
while True:
    # Entrada de interface
    if teclado.key_pressed("W") and pad_right.y > 0:
        pad_right.y = pad_right.y - vel_pad * janela.delta_time()
    if teclado.key_pressed("S") and (pad_right.y + pad_right.height) < janela.height:
        pad_right.y = pad_right.y + vel_pad * janela.delta_time()

    '''if teclado.key_pressed("UP") and pad_left.y > 0:
        pad_left.y = pad_left.y - vel_pad * janela.delta_time()
    if teclado.key_pressed("DOWN") and (pad_left.y + pad_left.height) < janela.height:
        pad_left.y = pad_left.y + vel_pad * janela.delta_time()'''

    # IA
    if hit_contador < 3:
        if pad_left.y > bolinha.y:  # se bolinha estiver embaixo
            pad_left.y = pad_left.y - vel_pad / 1.6 * janela.delta_time()  # dividimos por 2 a velocidade para não ser impossível de ganhar
        elif pad_left.y < bolinha.y:  # se a bolinha estiver em cima
            pad_left.y = pad_left.y + vel_pad / 1.6 * janela.delta_time()  # dividimos por 2 a velocidade para não ser impossível de ganhar
    else:
        if bolinha.x > janela.width / 2 - bolinha.width / 2:  # se a bolinha azul estiver perto da IA
            if pad_left.y > bolinha.y:  # se o PAD da IA estiver embaixo
                pad_left.y = pad_left.y - vel_pad / 1.2 * janela.delta_time()
            elif pad_left.y < bolinha.y:  # se o pad da IA estiver em cima
                pad_left.y = pad_left.y + vel_pad / 1.2 * janela.delta_time()

        if bolinha2.x > janela.width / 2 - bolinha.width / 2:  # se a bolinha vermelha estiver perto da IA
            if pad_left.y > bolinha2.y:  # se o pad da IA estiver embaixo
                pad_left.y = pad_left.y - vel_pad / 1.2 * janela.delta_time()
            elif pad_left.y < bolinha2.y:  # se o pad da IA estiver em cima
                pad_left.y = pad_left.y + vel_pad / 1.2 * janela.delta_time()

    # Contador de frames por segundo
    if tempo <= 1:
        fps += 1
        tempo += janela.delta_time()
    else:
        fps_register = fps
        tempo = 0
        fps = 0

    # Movimento da bolinha
    bolinha.x = bolinha.x + vel_x1 * janela.delta_time()  # dá no mesmo que fazer < bolinha.movex(velocidade_x) > (o msm serve pra y)
    bolinha.y = bolinha.y + vel_y1 * janela.delta_time()

    if hit_contador >= 3:
        bolinha2.x = bolinha2.x + vel_x2 * janela.delta_time()
        bolinha2.y = bolinha2.y + vel_y2 * janela.delta_time()

    # Colisão da bolinha

    # É Gol!
    if (bolinha.x + bolinha.width) > janela.width:
        bolinha.x = janela.width / 2 - bolinha.width / 2
        bolinha.y = janela.height / 2 - bolinha.height / 2
        vel_x1 = init_vel_x1 * (-1)
        vel_y1 = init_vel_y1
        score_left += 1
    if bolinha.x < 0:
        bolinha.x = janela.width / 2 - bolinha.width / 2
        bolinha.y = janela.height / 2 - bolinha.height / 2
        vel_x1 = init_vel_x1 * (-1)
        vel_y1 = init_vel_y1
        score_right += 1

    if (bolinha2.x + bolinha2.width) > janela.width:
        bolinha2.x = janela.width / 2 - bolinha2.width / 2
        bolinha2.y = janela.height / 2 - bolinha2.height / 2
        vel_x2 = init_vel_x2 * (-1)
        vel_y2 = init_vel_y2
        score_left += 1
    if bolinha2.x < 0:
        bolinha2.x = janela.width / 2 - bolinha2.width / 2
        bolinha2.y = janela.height / 2 - bolinha2.height / 2
        vel_x2 = init_vel_x2 * (-1)
        vel_y2 = init_vel_y2
        score_right += 1

    # Colisão com os pads
    if bolinha.collided(pad_right):
        vel_x1 *= -1.1
        bolinha.x += 5  # correção da patinação
        hit_contador += 1
    if bolinha.collided(pad_left):
        vel_x1 *= -1.1
        bolinha.x -= 5  # correção da patinação
        hit_contador += 1

    if bolinha2.collided(pad_right):
        vel_x2 *= -1
        bolinha2.x += 5  # correção da patinação
    if bolinha2.collided(pad_left):
        vel_x2 *= -1
        bolinha2.x -= 5  # correção da patinação

    # Colisão eixo Y
    if (bolinha.y + bolinha.height) > janela.height:
        vel_y1 *= -1
        bolinha.y -= 5  # correção da patinação
    if bolinha.y < 0:
        vel_y1 *= -1
        bolinha.y += 5  # correção da patinação

    if (bolinha2.y + bolinha2.height) > janela.height:
        vel_y2 *= -1.05
        bolinha2.y -= 5  # correção da patinação
    if bolinha2.y < 0:
        vel_y2 *= -1.05
        bolinha2.y += 5  # correção da patinação

    # Desenhos
    background.draw()
    janela.draw_text(text='{} x {}'.format(score_left, score_right), x=janela.width / 2.125, y=janela.height / 16, size=40, color=(233, 204, 0), font_name='Impact', bold=False)
    bolinha.draw()
    if hit_contador >= 3:
        bolinha2.draw()
    pad_right.draw()
    pad_left.draw()
    janela.draw_text(text='{}'.format(fps_register), x=janela.width/1.1, y=janela.height/32, size=40, color=(50, 205, 50))
    janela.update()
