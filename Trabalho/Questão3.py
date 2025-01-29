import heapq

# Definindo as estações e as distâncias reais entre elas
grafo = {
    'E1': {'E2': 11},
    'E2': {'E1': 11, 'E3': 9, 'E9': 11, 'E10': 4},
    'E3': {'E2': 9, 'E4': 7, 'E9': 10, 'E13': 19},
    'E4': {'E3': 7, 'E5': 14, 'E8': 16, 'E13': 12},
    'E5': {'E4': 14, 'E6': 3, 'E7': 2, 'E8': 33},
    'E6': {'E5': 3},
    'E7': {'E5': 2},
    'E8': {'E4': 16, 'E5': 33, 'E9': 10, 'E12': 7},
    'E9': {'E2': 11, 'E3': 10, 'E8': 10, 'E11': 14},
    'E10': {'E2': 4},
    'E11': {'E9': 14},
    'E12': {'E8': 7},
    'E13': {'E3': 19, 'E4': 12, 'E14': 5},
    'E14': {'E13': 5}
}

# Heurística: distância em linha reta entre as estações
distancia_linha_reta = {
    "E1": {"E1": 0, "E2": 11, "E3": 20, "E4": 27, "E5": 40, "E6": 43, "E7": 39, "E8": 28, "E9": 18, "E10": 10, "E11": 18, "E12": 30, "E13": 30, "E14": 32},
    "E2": {"E1": 11, "E2": 0, "E3": 9, "E4": 16, "E5": 29, "E6": 32, "E7": 28, "E8": 19, "E9": 11, "E10": 4, "E11": 17, "E12": 23, "E13": 21, "E14": 24},
    "E3": {"E1": 20, "E2": 9, "E3": 0, "E4": 7, "E5": 20, "E6": 22, "E7": 19, "E8": 15, "E9": 10, "E10": 11, "E11": 21, "E12": 21, "E13": 13, "E14": 18},
    "E4": {"E1": 27, "E2": 16, "E3": 7, "E4": 0, "E5": 13, "E6": 16, "E7": 12, "E8": 13, "E9": 13, "E10": 18, "E11": 26, "E12": 21, "E13": 11, "E14": 17},
    "E5": {"E1": 40, "E2": 29, "E3": 20, "E4": 13, "E5": 0, "E6": 3, "E7": 2, "E8": 21, "E9": 25, "E10": 31, "E11": 38, "E12": 27, "E13": 16, "E14": 20},
    "E6": {"E1": 43, "E2": 32, "E3": 22, "E4": 16, "E5": 3, "E6": 0, "E7": 4, "E8": 23, "E9": 28, "E10": 33, "E11": 41, "E12": 30, "E13": 17, "E14": 20},
    "E7": {"E1": 39, "E2": 28, "E3": 19, "E4": 12, "E5": 2, "E6": 4, "E7": 0, "E8": 22, "E9": 25, "E10": 29, "E11": 38, "E12": 28, "E13": 13, "E14": 17},
    "E8": {"E1": 28, "E2": 19, "E3": 15, "E4": 13, "E5": 21, "E6": 23, "E7": 22, "E8": 0, "E9": 9, "E10": 22, "E11": 18, "E12": 7, "E13": 25, "E14": 30},
    "E9": {"E1": 18, "E2": 11, "E3": 10, "E4": 13, "E5": 25, "E6": 28, "E7": 25, "E8": 9, "E9": 0, "E10": 13, "E11": 12, "E12": 12, "E13": 23, "E14": 28},
    "E10": {"E1": 10, "E2": 4, "E3": 11, "E4": 18, "E5": 31, "E6": 33, "E7": 29, "E8": 22, "E9": 13, "E10": 0, "E11": 20, "E12": 27, "E13": 20, "E14": 23},
    "E11": {"E1": 18, "E2": 17, "E3": 21, "E4": 26, "E5": 38, "E6": 41, "E7": 38, "E8": 18, "E9": 12, "E10": 20, "E11": 0, "E12": 15, "E13": 35, "E14": 39},
    "E12": {"E1": 30, "E2": 23, "E3": 21, "E4": 21, "E5": 27, "E6": 30, "E7": 28, "E8": 7, "E9": 12, "E10": 27, "E11": 15, "E12": 0, "E13": 31, "E14": 37},
    "E13": {"E1": 30, "E2": 21, "E3": 13, "E4": 11, "E5": 16, "E6": 17, "E7": 13, "E8": 25, "E9": 23, "E10": 20, "E11": 35, "E12": 31, "E13": 0, "E14": 5},
    "E14": {"E1": 32, "E2": 24, "E3": 18, "E4": 17, "E5": 20, "E6": 20, "E7": 17, "E8": 30, "E9": 28, "E10": 23, "E11": 39, "E12": 37, "E13": 5, "E14": 0}
}

# Definindo as estações por linha
estacoes_por_linha = {
    "Linha Azul": ["E1", "E2", "E3", "E4", "E5", "E6"],
    "Linha Amarela": ["E10", "E2", "E9", "E8", "E5", "E7"],
    "Linha Vermelha": ["E11", "E9", "E3", "E13"],
    "Linha Verde": ["E12", "E8", "E4", "E13", "E14"]
}

def a_estrela(grafo, inicio, objetivo, distancia_linha_reta):
    conjunto_aberto = []
    heapq.heappush(conjunto_aberto, (0, inicio))
    veio_de = {}
    g_score = {estacao: float('inf') for estacao in grafo}
    g_score[inicio] = 0
    f_score = {estacao: float('inf') for estacao in grafo}
    f_score[inicio] = distancia_linha_reta[inicio][objetivo]

    while conjunto_aberto:
        _, atual = heapq.heappop(conjunto_aberto)

        if atual == objetivo:
            return reconstruir_caminho(veio_de, atual)

        for vizinho, distancia in grafo[atual].items():
            tentative_g_score = g_score[atual] + distancia

            if tentative_g_score < g_score[vizinho]:
                veio_de[vizinho] = atual
                g_score[vizinho] = tentative_g_score
                f_score[vizinho] = tentative_g_score + distancia_linha_reta[vizinho][objetivo]
                heapq.heappush(conjunto_aberto, (f_score[vizinho], vizinho))

    return None

def reconstruir_caminho(veio_de, atual):
    caminho = []
    while atual in veio_de:
        caminho.append(atual)
        atual = veio_de[atual]
    caminho.append(atual)
    caminho.reverse()
    return caminho

def encontrar_linhas(estacao, estacoes_por_linha):
    """Encontra todas as linhas de uma estação."""
    return [linha for linha, estacoes in estacoes_por_linha.items() if estacao in estacoes]

def calcular_tempo(caminho, grafo, estacoes_por_linha):
    velocidade = 30  # km/h
    tempo_troca = 5  # minutos por troca de linha
    distancia_total = 0
    tempo_total = 0
    trocas = 0
    linha_atual = None

    print("\nDetalhes do percurso:")
    for i in range(len(caminho) - 1):
        estacao_atual = caminho[i]
        proxima_estacao = caminho[i + 1]
        distancia = grafo[estacao_atual][proxima_estacao]
        distancia_total += distancia

        # Tempo de viagem entre estações
        tempo_trecho = (distancia / velocidade) * 60  # Convertendo para minutos
        tempo_total += tempo_trecho

        print(f"{estacao_atual} -> {proxima_estacao}: {tempo_trecho:.2f} minutos")

        # Verificar troca de linha
        linhas_atual = encontrar_linhas(estacao_atual, estacoes_por_linha)
        linhas_proxima = encontrar_linhas(proxima_estacao, estacoes_por_linha)

        if linha_atual is None:
            linha_atual = set(linhas_atual).intersection(linhas_proxima)

        if not linha_atual.intersection(linhas_proxima):
            trocas += 1
            tempo_total += tempo_troca
            print(f"  ** Troca de linha em {estacao_atual}, adicionando {tempo_troca} minutos **")
            linha_atual = set(linhas_proxima)

    print(f"\nDistância total: {distancia_total:.2f} km")
    print(f"Tempo total estimado: {tempo_total:.2f} minutos")
    print(f"Trocas de linha: {trocas}")

    return tempo_total

# Solicitar ao usuário as estações de origem e destino
estacao_inicio = input("Digite a estação de origem (ex: E1): ")
estacao_objetivo = input("Digite a estação de destino (ex: E14): ")

# Verificar se as estações existem no grafo
if estacao_inicio not in grafo or estacao_objetivo not in grafo:
    print("Uma ou ambas as estações digitadas não existem no grafo.")
else:
    caminho = a_estrela(grafo, estacao_inicio, estacao_objetivo, distancia_linha_reta)

    if caminho:
        print(f"\nCaminho mais rápido de {estacao_inicio} para {estacao_objetivo}: {' -> '.join(caminho)}")
        calcular_tempo(caminho, grafo, estacoes_por_linha)
    else:
        print(f"Não foi possível encontrar um caminho de {estacao_inicio} para {estacao_objetivo}.")