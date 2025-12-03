import pygame
from config import tamanho_da_celula
from ia import caminho_para_passos

class campones:
    def __init__(self, x, y):

        #Posição
        self.x = x
        self.y = y

        #Hitbox
        self.largura = tamanho_da_celula
        self.altura = tamanho_da_celula 
        self.cor = (0, 0, 255)

        #Velocidade
        self.velocidade = 1

        self.path_passos = []  # fila de (dx,dy) para executar
        self.index_passos = 0  # posição atual na fila

    def set_path_from_positions(self, pos_list):
        if not pos_list or len(pos_list) < 2:
            self.path_passos = []
            self.index_passos = 0
            return
        self.path_passos = caminho_para_passos(pos_list)
        self.index_passos = 0

    def step(self, mapa):
        if self.index_passos >= len(self.path_passos):
            return False
        dx, dy = self.path_passos[self.index_passos]

        #Garante que o caminho é possível
        if mapa[self.y + dy][self.x + dx] == 0:  
            self.x += dx * self.velocidade
            self.y += dy * self.velocidade
        else:
            # colisão inesperada: limpar path
            self.path_passos = []
            self.index_passos = 0
            return False

        self.index_passos += 1
        return True

    def has_path(self):
        return self.index_passos < len(self.path_passos)
    
    #Mover antigo - Manual
    '''def pode_mover(self, pos_x, pos_y, mapa):
        novo_x = self.x + pos_x
        novo_y = self.y + pos_y

        #Limite do mapa
        if novo_x < 0 or novo_y < 0:
            return False

        if novo_y >= len(mapa) or novo_x >= len(mapa[0]):
            return False

        #Parede
        if mapa[novo_x][novo_y] == 1:
            return False

        return True

        
        
    def mover(self, pos_x, pos_y, mapa):

        if self.pode_mover(pos_x, pos_y, mapa):
            self.x += pos_x * self.velocidade
            self.y += pos_y * self.velocidade

    #Mover pelo teclado
    def mover_teclado(self, teclas, mapa):

        ny = 0
        nx = 0
        
        if teclas[pygame.K_w]:
            ny = -1
                    
        if teclas[pygame.K_s]:
            ny = +1
                   
        if teclas[pygame.K_a]:
            nx = -1
                    
        if teclas[pygame.K_d]:
            nx = +1

        self.mover(nx, ny, mapa)'''

    def desenhar(self, tela, cam_coluna, cam_linha):

        #Posicão[x][y] para pixels na tela
        x = (self.x - cam_coluna) * tamanho_da_celula
        y = (self.y - cam_linha) * tamanho_da_celula - (self.altura - tamanho_da_celula)
    
        #Janela rect e desenho
        rect = pygame.Rect(x, y, self.largura, self.altura)
        pygame.draw.rect(tela, self.cor, rect)
