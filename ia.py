import heapq
from collections import deque

# ---------- utilitários ----------
def dentro_limites(x, y, mapa):
    return 0 <= y < len(mapa) and 0 <= x < len(mapa[0])

def vizinhos_4(x, y, mapa):
    # retorna vizinhos (x,y) em 4-direções (direita, esquerda, baixo, cima)
    direcoes = [(1,0), (-1,0), (0,1), (0,-1)]
    for dx, dy in direcoes:
        nx, ny = x + dx, y + dy
        if dentro_limites(nx, ny, mapa) and mapa[ny][nx] == 0:
            yield nx, ny

def heuristica_manhattan(a, b):
    ax, ay = a
    bx, by = b
    return abs(ax - bx) + abs(ay - by)

def a_star(mapa, inicio, objetivo):
    """retorna caminho como lista de posições ou None"""
    if inicio == objetivo:
        return [inicio]

    open_heap = []
    heapq.heappush(open_heap, (0 + heuristica_manhattan(inicio, objetivo), 0, inicio))
    veio_de = {inicio: None}
    custo_g = {inicio: 0}

    while open_heap:
        _, g_atual, atual = heapq.heappop(open_heap)

        if atual == objetivo:
            # reconstruir caminho
            path = []
            cur = objetivo
            while cur is not None:
                path.append(cur)
                cur = veio_de[cur]
            path.reverse()
            return path

        x, y = atual
        for nx, ny in vizinhos_4(x, y, mapa):
            novo_g = g_atual + 1  # custo uniforme
            vizinho = (nx, ny)
            if vizinho not in custo_g or novo_g < custo_g[vizinho]:
                custo_g[vizinho] = novo_g
                prioridade = novo_g + heuristica_manhattan(vizinho, objetivo)
                heapq.heappush(open_heap, (prioridade, novo_g, vizinho))
                veio_de[vizinho] = atual

    return None

# ---------- converter caminho em passos (dx,dy) ----------
def caminho_para_passos(path):
    """recebe lista de posições e retorna lista de (dx,dy) passos"""
    passos = []
    for (x0,y0), (x1,y1) in zip(path, path[1:]):
        passos.append((x1 - x0, y1 - y0))
    return passos
