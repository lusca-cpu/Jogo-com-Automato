# Trabalho de LFA
# Nomes: Igor Vieira e Lucas Antônio

# As teclas:                                 Combos:
# w = Pulo                                   w depois l = Voadora
# s = Abaixar                                w depois k = Soco pra cima
# d = Virar para direita                     s depois l = Chute baixo
# a = Virar para a esquerda                  s depois w = Gordo
# k = Soco                                   k depois k = Socão
# l = Chute                                  k depois k depois k = Metralhadora
#                                            l dedpois l = Chutão

import pygame
from time import time

from pygame.locals import (
    K_w, #PULO
    K_s, #ABAIXAR
    K_d, #VIRAR PARA DIREITA
    K_a, #VIRAR PARA A ESQUERDA
    K_k, #SOCO
    K_l, #CHUTE
    K_ESCAPE,
    KEYDOWN,
    QUIT,
    RLEACCEL
)

pygame.init()

SCREEN_WIDTH = 630
SCREEN_HEIGHT = 360

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.imagem = pygame.image.load("imagens/P_D.png").convert_alpha()
        self.imagem.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.imagem.get_rect()
        self.rect.move_ip(240, 200)
        self.imagem = pygame.transform.scale(self.imagem, (80, 100))

    def update(self, Estado):
        self.imagem = pygame.image.load("imagens/"+Estado+".png").convert_alpha()
        self.imagem = pygame.transform.scale(self.imagem, (80, 100))
        
class AFD:
    def __init__(self, alfabeto, estados, estadoAtual, transicoes, inicial, finais):
        self.alfabeto = alfabeto
        self.estados = estados
        self.estadoAtual = estadoAtual
        self.transicoes = transicoes
        self.inicial = inicial
        self.fianis = finais

def transicao(estadoAtual, comando, transicoes):
    for i in transicoes:
        if i['ini'] == estadoAtual and i['alfabeto'] == comando:
            return i['fim']
        

if __name__ == '__main__':
    window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    bg_img = pygame.image.load("imagens/background.jpeg")

    afd = AFD(['K_w','K_s','K_a','K_d','K_k','K_l'],
              ['P_E','P_D',
              'Pulo_E','Pulo_D',
              'Abaixar_D','Abaixar_E',
              'Soco_E','Soco_D',
              'Socao_E','Socao_D',
              'SocoCima_D','SocoCima_E',
              'Chute_D','Chute_E',
              'Chutao_D','Chutao_E',
              'ChuteBaixo_E','ChuteBaixo_D',
              'Voadora_D','Voadora_E',
              'Gordo_E','Gordo_D',
              'Metralhadora_D','Metralhadora_E'],
               'P_E',
              [{'ini':'P_E','alfabeto':'K_w','fim':'Pulo_E'},
              {'ini':'P_D','alfabeto':'K_w','fim':'Pulo_D'},
              {'ini':'P_E','alfabeto':'K_s','fim':'Abaixar_E'},
              {'ini':'P_D','alfabeto':'K_s','fim':'Abaixar_D'},
              {'ini':'P_E','alfabeto':'K_a','fim':'P_E'},
              {'ini':'P_D','alfabeto':'K_d','fim':'P_D'},
              {'ini':'P_E','alfabeto':'K_d','fim':'P_D'},
              {'ini':'P_D','alfabeto':'K_a','fim':'P_E'},
              {'ini':'P_E','alfabeto':'K_k','fim':'Soco_E'},
              {'ini':'P_D','alfabeto':'K_k','fim':'Soco_D'},
              {'ini':'P_E','alfabeto':'K_l','fim':'Chute_E'},
              {'ini':'P_D','alfabeto':'K_l','fim':'Chute_D'},

              {'ini':'Abaixar_E','alfabeto':'K_w','fim':'Gordo_E'},
              {'ini':'Abaixar_D','alfabeto':'K_w','fim':'Gordo_D'},
              {'ini':'Abaixar_E','alfabeto':'K_s','fim':'Abaixar_E'},
              {'ini':'Abaixar_D','alfabeto':'K_s','fim':'Abaixar_D'},
              {'ini':'Abaixar_E','alfabeto':'K_a','fim':'Abaixar_E'},
              {'ini':'Abaixar_D','alfabeto':'K_d','fim':'Abaixar_D'},
              {'ini':'Abaixar_D','alfabeto':'K_a','fim':'Abaixar_E'},
              {'ini':'Abaixar_E','alfabeto':'K_d','fim':'Abaixar_D'},
              {'ini':'Abaixar_E','alfabeto':'K_l','fim':'ChuteBaixo_E'},
              {'ini':'Abaixar_D','alfabeto':'K_l','fim':'ChuteBaixo_D'},
              {'ini':'Abaixar_E','alfabeto':'K_k','fim':'Soco_E'},
              {'ini':'Abaixar_D','alfabeto':'K_k','fim':'Soco_D'},
              
              {'ini':'Soco_E','alfabeto':'K_w','fim':'Pulo_E'},
              {'ini':'Soco_D','alfabeto':'K_w','fim':'Pulo_D'},
              {'ini':'Soco_E','alfabeto':'K_s','fim':'Abaixar_E'},
              {'ini':'Soco_D','alfabeto':'K_s','fim':'Abaixar_D'},
              {'ini':'Soco_E','alfabeto':'K_a','fim':'P_E'},
              {'ini':'Soco_D','alfabeto':'K_d','fim':'P_D'},
              {'ini':'Soco_D','alfabeto':'K_a','fim':'P_E'},
              {'ini':'Soco_E','alfabeto':'K_d','fim':'P_D'},
              {'ini':'Soco_E','alfabeto':'K_k','fim':'Socao_E'},
              {'ini':'Soco_D','alfabeto':'K_k','fim':'Socao_D'},
              {'ini':'Soco_E','alfabeto':'K_l','fim':'Chute_E'},
              {'ini':'Soco_D','alfabeto':'K_l','fim':'Chute_D'},
            
              {'ini':'Socao_E','alfabeto':'K_w','fim':'Pulo_E'},
              {'ini':'Socao_D','alfabeto':'K_w','fim':'Pulo_D'},
              {'ini':'Socao_E','alfabeto':'K_s','fim':'Abaixar_E'},
              {'ini':'Socao_D','alfabeto':'K_s','fim':'Abaixar_D'},
              {'ini':'Socao_E','alfabeto':'K_a','fim':'P_E'},
              {'ini':'Socao_D','alfabeto':'K_d','fim':'P_D'},
              {'ini':'Socao_D','alfabeto':'K_a','fim':'P_E'},
              {'ini':'Socao_E','alfabeto':'K_d','fim':'P_D'},
              {'ini':'Socao_E','alfabeto':'K_k','fim':'Metralhadora_E'},
              {'ini':'Socao_D','alfabeto':'K_k','fim':'Metralhadora_D'},
              {'ini':'Socao_E','alfabeto':'K_l','fim':'Chute_E'},
              {'ini':'Socao_D','alfabeto':'K_l','fim':'Chute_D'},

              {'ini':'Metralhadora_E','alfabeto':'K_w','fim':'Pulo_E'},
              {'ini':'Metralhadora_D','alfabeto':'K_w','fim':'Pulo_D'},
              {'ini':'Metralhadora_E','alfabeto':'K_s','fim':'Abaixar_E'},
              {'ini':'Metralhadora_D','alfabeto':'K_s','fim':'Abaixar_D'},
              {'ini':'Metralhadora_E','alfabeto':'K_a','fim':'P_E'},
              {'ini':'Metralhadora_D','alfabeto':'K_d','fim':'P_D'},
              {'ini':'Metralhadora_D','alfabeto':'K_a','fim':'P_E'},
              {'ini':'Metralhadora_E','alfabeto':'K_d','fim':'P_D'},
              {'ini':'Metralhadora_E','alfabeto':'K_k','fim':'Soco_E'},
              {'ini':'Metralhadora_D','alfabeto':'K_k','fim':'Soco_D'},
              {'ini':'Metralhadora_E','alfabeto':'K_l','fim':'Chute_E'},
              {'ini':'Metralhadora_D','alfabeto':'K_l','fim':'Chute_D'},

              {'ini':'SocoCima_E','alfabeto':'K_w','fim':'Pulo_E'},
              {'ini':'SocoCima_D','alfabeto':'K_w','fim':'Pulo_D'},
              {'ini':'SocoCima_E','alfabeto':'K_s','fim':'Abaixar_E'},
              {'ini':'SocoCima_D','alfabeto':'K_s','fim':'Abaixar_D'},
              {'ini':'SocoCima_E','alfabeto':'K_a','fim':'P_E'},
              {'ini':'SocoCima_D','alfabeto':'K_d','fim':'P_D'},
              {'ini':'SocoCima_D','alfabeto':'K_a','fim':'P_E'},
              {'ini':'SocoCima_E','alfabeto':'K_d','fim':'P_D'},
              {'ini':'SocoCima_E','alfabeto':'K_k','fim':'Soco_E'},
              {'ini':'SocoCima_D','alfabeto':'K_k','fim':'Soco_D'},
              {'ini':'SocoCima_E','alfabeto':'K_l','fim':'Chute_E'},
              {'ini':'SocoCima_D','alfabeto':'K_l','fim':'Chute_D'},

              {'ini':'Pulo_E','alfabeto':'K_w','fim':'Pulo_E'},
              {'ini':'Pulo_D','alfabeto':'K_w','fim':'Pulo_D'},
              {'ini':'Pulo_E','alfabeto':'K_s','fim':'Abaixar_E'},
              {'ini':'Pulo_D','alfabeto':'K_s','fim':'Abaixar_D'},
              {'ini':'Pulo_E','alfabeto':'K_a','fim':'Pulo_E'},
              {'ini':'Pulo_D','alfabeto':'K_d','fim':'Pulo_D'},
              {'ini':'Pulo_D','alfabeto':'K_a','fim':'Pulo_E'},
              {'ini':'Pulo_E','alfabeto':'K_d','fim':'Pulo_D'},
              {'ini':'Pulo_E','alfabeto':'K_k','fim':'SocoCima_E'},
              {'ini':'Pulo_D','alfabeto':'K_k','fim':'SocoCima_D'},
              {'ini':'Pulo_E','alfabeto':'K_l','fim':'Voadora_E'},
              {'ini':'Pulo_D','alfabeto':'K_l','fim':'Voadora_D'},
            
              {'ini':'Chute_E','alfabeto':'K_w','fim':'Pulo_E'},
              {'ini':'Chute_D','alfabeto':'K_w','fim':'Pulo_D'},
              {'ini':'Chute_E','alfabeto':'K_s','fim':'Abaixar_E'},
              {'ini':'Chute_D','alfabeto':'K_s','fim':'Abaixar_D'},
              {'ini':'Chute_E','alfabeto':'K_a','fim':'P_E'},
              {'ini':'Chute_D','alfabeto':'K_d','fim':'P_D'},
              {'ini':'Chute_D','alfabeto':'K_a','fim':'P_E'},
              {'ini':'Chute_E','alfabeto':'K_d','fim':'P_D'},
              {'ini':'Chute_D','alfabeto':'K_k','fim':'Soco_D'},
              {'ini':'Chute_E','alfabeto':'K_k','fim':'Soco_E'},
              {'ini':'Chute_E','alfabeto':'K_l','fim':'Chutao_E'},
              {'ini':'Chute_D','alfabeto':'K_l','fim':'Chutao_D'},

              {'ini':'Chutao_E','alfabeto':'K_w','fim':'Pulo_E'},
              {'ini':'Chutao_D','alfabeto':'K_w','fim':'Pulo_D'},
              {'ini':'Chutao_E','alfabeto':'K_s','fim':'Abaixar_E'},
              {'ini':'Chutao_D','alfabeto':'K_s','fim':'Abaixar_D'},
              {'ini':'Chutao_E','alfabeto':'K_a','fim':'P_E'},
              {'ini':'Chutao_D','alfabeto':'K_d','fim':'P_D'},
              {'ini':'Chutao_D','alfabeto':'K_a','fim':'P_E'},
              {'ini':'Chutao_E','alfabeto':'K_d','fim':'P_D'},
              {'ini':'Chutao_D','alfabeto':'K_k','fim':'Soco_D'},
              {'ini':'Chutao_E','alfabeto':'K_k','fim':'Soco_E'},
              {'ini':'Chutao_E','alfabeto':'K_l','fim':'Chute_E'},
              {'ini':'Chutao_D','alfabeto':'K_l','fim':'Chute_D'},

              {'ini':'ChuteBaixo_E','alfabeto':'K_w','fim':'Pulo_E'},
              {'ini':'ChuteBaixo_D','alfabeto':'K_w','fim':'Pulo_D'},
              {'ini':'ChuteBaixo_E','alfabeto':'K_s','fim':'Abaixar_E'},
              {'ini':'ChuteBaixo_D','alfabeto':'K_s','fim':'Abaixar_D'},
              {'ini':'ChuteBaixo_E','alfabeto':'K_a','fim':'P_E'},
              {'ini':'ChuteBaixo_D','alfabeto':'K_d','fim':'P_D'},
              {'ini':'ChuteBaixo_D','alfabeto':'K_a','fim':'P_E'},
              {'ini':'ChuteBaixo_E','alfabeto':'K_d','fim':'P_D'},
              {'ini':'ChuteBaixo_D','alfabeto':'K_k','fim':'Soco_D'},
              {'ini':'ChuteBaixo_E','alfabeto':'K_k','fim':'Soco_E'},
              {'ini':'ChuteBaixo_E','alfabeto':'K_l','fim':'Chute_E'},
              {'ini':'ChuteBaixo_D','alfabeto':'K_l','fim':'Chute_D'},

              {'ini':'Voadora_E','alfabeto':'K_w','fim':'Pulo_E'},
              {'ini':'Voadora_D','alfabeto':'K_w','fim':'Pulo_D'},
              {'ini':'Voadora_E','alfabeto':'K_s','fim':'Abaixar_E'},
              {'ini':'Voadora_D','alfabeto':'K_s','fim':'Abaixar_D'},
              {'ini':'Voadora_E','alfabeto':'K_a','fim':'P_E'},
              {'ini':'Voadora_D','alfabeto':'K_d','fim':'P_D'},
              {'ini':'Voadora_D','alfabeto':'K_a','fim':'P_E'},
              {'ini':'Voadora_E','alfabeto':'K_d','fim':'P_D'},
              {'ini':'Voadora_D','alfabeto':'K_k','fim':'Soco_D'},
              {'ini':'Voadora_E','alfabeto':'K_k','fim':'Soco_E'},
              {'ini':'Voadora_E','alfabeto':'K_l','fim':'Chute_E'},
              {'ini':'Voadora_D','alfabeto':'K_l','fim':'Chute_D'},

              {'ini':'Gordo_E','alfabeto':'K_w','fim':'Pulo_E'},
              {'ini':'Gordo_D','alfabeto':'K_w','fim':'Pulo_D'},
              {'ini':'Gordo_E','alfabeto':'K_s','fim':'Abaixar_E'},
              {'ini':'Gordo_D','alfabeto':'K_s','fim':'Abaixar_D'},
              {'ini':'Gordo_E','alfabeto':'K_a','fim':'Gordo_E'},
              {'ini':'Gordo_D','alfabeto':'K_d','fim':'Gordo_D'},
              {'ini':'Gordo_D','alfabeto':'K_a','fim':'Gordo_E'},
              {'ini':'Gordo_E','alfabeto':'K_d','fim':'Gordo_D'},
              {'ini':'Gordo_D','alfabeto':'K_k','fim':'Soco_D'},
              {'ini':'Gordo_E','alfabeto':'K_k','fim':'Soco_E'},
              {'ini':'Gordo_E','alfabeto':'K_l','fim':'Chute_E'},
              {'ini':'Gordo_D','alfabeto':'K_l','fim':'Chute_D'}],
              ['P_E'],
              ['P_E'])

    running = True
    player = Player()
    estado = str(afd.inicial)[2:-2]

    player.update(estado)
    while running:
        window.blit(bg_img,(0,0))
        window.blit(player.imagem, player.rect)
        
        for event in pygame.event.get():
            if event.type == KEYDOWN:                    
            # If the Esc key is pressed, then exit the main loop
                if event.key == K_ESCAPE:
                    running = False
        # Check for QUIT event. If QUIT, then set running to false.
            elif event.type == QUIT:
                running = False

        # Get all the keys currently pressed
        start = 0
        start = time()
        while(time() - start < 0.07):
            pressed_keys = pygame.key.get_pressed()

        if pressed_keys[K_s]:
            estado = transicao(estado,'K_s',afd.transicoes)
            player.update(estado)
        elif pressed_keys[K_w]:
            estado = transicao(estado,'K_w',afd.transicoes)
            player.update(estado)
        elif pressed_keys[K_a]:
            estado = transicao(estado,'K_a',afd.transicoes)
            player.update(estado)
        elif pressed_keys[K_d]:
            estado = transicao(estado,'K_d',afd.transicoes)
            player.update(estado)
        elif pressed_keys[K_k]:
            estado = transicao(estado,'K_k',afd.transicoes)
            player.update(estado)
        elif pressed_keys[K_l]:
            estado = transicao(estado,'K_l',afd.transicoes)
            player.update(estado)

        # Flip the display
        pygame.display.flip()
        
    pygame.quit()