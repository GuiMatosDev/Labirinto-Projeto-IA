#Importações
import pygame
from config import largura_tela, altura_tela, mapa_coluna, mapa_linha, debug
from camera import cam_c, cam_l, cam_mov
from mapa import criar_mapa, desenhar_mapa, gerar_labirinto
from npc import campones
from ia import a_star, caminho_para_passos
     
#Execução do programa
def main():
    
    #Parametrôs de inicialização 
    pygame.init()
    pygame.display.set_caption("Labirinto Usando A* v0.1")

    tela = pygame.display.set_mode((largura_tela, altura_tela))
    clock = pygame.time.Clock()
    mapa = criar_mapa(mapa_coluna, mapa_linha)
    npc_campones = campones(1, 1)
    cam_coluna = cam_c
    cam_linha = cam_l

    #Objetivo
    altura = len(mapa)
    largura = len(mapa[0])

    objetivo_x = largura - 2
    objetivo_y = altura - 2

    #Npc
    path = a_star(mapa, (npc_campones.x, npc_campones.y), (objetivo_x, objetivo_y))
    if path:
        npc_campones.set_path_from_positions(path)

    #Objetivo recebendo valor/cor na grade
    mapa[objetivo_y][objetivo_x] = 2

    


    #Loop de Execução Global
    loop = True
    while loop:

        #Checa os eventos
        for eventos in pygame.event.get():
            
            #Camera
            teclas = pygame.key.get_pressed()
            cam_coluna, cam_linha = cam_mov(teclas, cam_coluna, cam_linha)
       
            #Fechando o Loop
            if eventos.type == pygame.QUIT:
                loop = False


        #Mapa
        desenhar_mapa(tela, mapa, cam_coluna, cam_linha, mapa_coluna, mapa_linha)
        
        npc_campones.step(mapa)
        npc_campones.desenhar(tela, cam_coluna, cam_linha)

        
        #Fps
        clock.tick(30)
    
        #Executa o que foi processado
        pygame.display.flip()

    #Fechando o Aplicativo
    pygame.quit()

#Iniciar Programa
if __name__ == "__main__":
    main()
    













