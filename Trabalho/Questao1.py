from collections import deque
import time

estado_objetivo = [[0, 1, 2],
                   [3, 4, 5],
                   [6, 7, 8]]

movimentos = {
    "cima": (-1, 0),
    "baixo": (1, 0),
    "esquerda": (0, -1),
    "direita": (0, 1),
}

def achar_espaco_em_branco(estado):
    for i in range(len(estado)):
        for j in range(len(estado[0])):
            if estado[i][j] == 0:
                return i, j

def gerar_novos_estados(estado, branco_pos, movimento):
    x, y = branco_pos
    dx, dy = movimentos[movimento]
    novo_x, novo_y = x + dx, y + dy

    if 0 <= novo_x < 3 and 0 <= novo_y < 3:
        novo_estado = [row[:] for row in estado]
        novo_estado[x][y], novo_estado[novo_x][novo_y] = novo_estado[novo_x][novo_y], novo_estado[x][y]
        return novo_estado
    return None

def bfs(estado_inicial):
    queue = deque([(estado_inicial, [])])
    visitado = set()
    visitado.add(tuple(tuple(row) for row in estado_inicial))

    while queue:
        current_estado, caminho = queue.popleft()

        if current_estado == estado_objetivo:
            return caminho

        branco_pos = achar_espaco_em_branco(current_estado)

        for movimento in movimentos:
            novo_estado = gerar_novos_estados(current_estado, branco_pos, movimento)
            if novo_estado:
                novo_estado_tuple = tuple(tuple(row) for row in novo_estado)
                if novo_estado_tuple not in visitado:
                    visitado.add(novo_estado_tuple)
                    queue.append((novo_estado, caminho + [(movimento, current_estado[branco_pos[0]][branco_pos[1]])]))

    return None

def exibir_passos(estado_inicial, passos):
    estado_atual = estado_inicial
    for i, (movimento, peca) in enumerate(passos):
        print(f"Passo {i + 1}: Mover peça {peca} para {movimento}")
        branco_pos = achar_espaco_em_branco(estado_atual)
        estado_atual = gerar_novos_estados(estado_atual, branco_pos, movimento)
        for linha in estado_atual:
            print(linha)
        print("-")

# Testar casos
casos = [
    ([[0, 1, 2], [3, 4, 5],  [6, 7, 8]], "Caso 1"),
    ([[6, 4, 2], [8, 1, 3], [7, 5, 0]], "Caso 2"),
    ([[4, 6, 2], [8, 1, 3], [7, 0, 5]], "Caso 3"),
    ([[3, 1, 2], [4, 7, 5], [6, 8, 0]], "Caso 4"),
    ([[1, 2, 3], [4, 5, 6], [7, 0, 8]], "Caso 5")
]

for estado_inicial, descricao in casos:
    print(f"{descricao}: Estado inicial:")
    for linha in estado_inicial:
        print(linha)

    inicio = time.time()
    passos = bfs(estado_inicial)
    fim = time.time()

    if passos:
        print(f"Solução encontrada em {len(passos)} passos (tempo: {fim - inicio:.4f}s):")
        exibir_passos(estado_inicial, passos)
    else:
        print("Este estado inicial não tem solução.")
    print("= " * 20)