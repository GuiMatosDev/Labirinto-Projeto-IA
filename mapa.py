import pygame
import random
from config import largura_tela, altura_tela, tamanho_da_celula
from config import fundo, cor_da_grade, cor_debug, debug, cor_vermelho

#labirinto
def gerar_labirinto(mapa):
    #DFS iterativo#

    #Tamanho
    altura = len(mapa)
    largura = len(mapa[0])

    #Preenche tudo com parede
    for y in range(altura):
        for x in range(largura):
            mapa[y][x] = 1

    #Inicio do Labirinto
    pilha = []
    pilha_x, pilha_y = 1, 1

    # Limites
    if pilha_x >= largura or pilha_y >= altura:
        return mapa

    mapa[pilha_y][pilha_x] = 0
    pilha.append((pilha_x, pilha_y))

    #Enquanto tiver elementos na pilha
    while pilha:
        x, y = pilha[-1]

        # embaralha direções e tenta cavar para vizinhos a duas casas
        direcoes = [(2,0), (-2,0), (0,2), (0,-2)]
        random.shuffle(direcoes)

        moved = False
        for dx, dy in direcoes:
            nx, ny = x + dx, y + dy

            # dentro dos limites e ainda não cavado
            if 0 <= ny < altura and 0 <= nx < largura and mapa[ny][nx] == 1:
                # remove a parede entre (x,y) e (nx,ny)
                meio_x, meio_y = x + dx//2, y + dy//2
                mapa[meio_y][meio_x] = 0
                mapa[ny][nx] = 0
                pilha.append((nx, ny))
                moved = True
                break

        #Se não encontrou mais caminhos, encerra 
        if not moved:
            pilha.pop()

    
    return mapa

    

#Mapa lógico
def criar_mapa(colunas, linhas):
    mapa = [[ 0 for x in range(colunas)] for y in range(linhas)]
    
    #Debug
    '''for linha in range(3,15):
        mapa[10][linha] = 1'''

    #Labirinto
    gerar_labirinto(mapa)
            
    return mapa

#Desenhando    
def desenhar_mapa(tela, mapa, cam_coluna, cam_linha, mapa_coluna, mapa_linha):
    
    tela.fill(fundo)

    quant_colunas = largura_tela // tamanho_da_celula
    quant_linhas = altura_tela // tamanho_da_celula
      
    #Varrendo toda a janela e guardando em coordenadas
    for x_coluna in range(quant_colunas):
        for y_linha in range(quant_linhas):
            janela_atual_coluna = cam_coluna + x_coluna
            janela_atual_linha = cam_linha + y_linha

            #Verificando se a janela está dentro do mapa
            if (0 <= janela_atual_linha < len(mapa) and
                0 <= janela_atual_coluna < len(mapa[0])):

                #Formação da janela atual em notação da grade matemática
                janela_atual_coordenada = mapa[janela_atual_linha][janela_atual_coluna]


                #Criando a janela pela função rect para possibilitar o desenho
                celula_x = x_coluna * tamanho_da_celula
                celula_y = y_linha * tamanho_da_celula
                rect = pygame.Rect(celula_x, celula_y, tamanho_da_celula, tamanho_da_celula)

                #Desenhando de acordo com valor
                if janela_atual_coordenada == 0: #Nada
                    pygame.draw.rect(tela, fundo, rect)                    
                elif janela_atual_coordenada == 1: #Parede
                    pygame.draw.rect(tela, cor_debug, rect)
                elif janela_atual_coordenada == 2: #Objetivo
                    pygame.draw.rect(tela, cor_vermelho, rect)

                #Desenhando a grade
                pygame.draw.rect(tela, cor_da_grade, rect, 1)
