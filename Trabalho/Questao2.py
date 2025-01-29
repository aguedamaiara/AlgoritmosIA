import time

# Função para calcular o número de conflitos no estado atual
def calcular_conflitos(estado):
    conflitos = 0
    n = len(estado)
    for i in range(n):
        for j in range(i + 1, n):
            if estado[i] == estado[j] or abs(estado[i] - estado[j]) == abs(i - j):
                conflitos += 1
    return conflitos

# Gerar sucessores movendo uma rainha em sua coluna
def gerar_sucessores(estado):
    sucessores = []
    n = len(estado)
    for col in range(n):
        for linha in range(n):
            if estado[col] != linha:  # Evitar a mesma posição
                novo_estado = estado[:]
                novo_estado[col] = linha
                sucessores.append(novo_estado)
    return sucessores

# Busca gulosa com rastreamento de conflitos
def busca_gulosa(estado_inicial):
    estado_atual = estado_inicial
    caminho = [estado_atual]

    print(f"Estado inicial: {estado_atual} | Conflitos: {calcular_conflitos(estado_atual)}")

    while True:
        conflitos_atual = calcular_conflitos(estado_atual)

        # Se não houver conflitos, solução encontrada
        if conflitos_atual == 0:
            print(f"Solução encontrada com {conflitos_atual} conflitos.")
            return caminho

        sucessores = gerar_sucessores(estado_atual)
        melhor_estado = None
        menor_conflitos = float('inf')

        # Avaliar sucessores
        for sucessor in sucessores:
            conflitos = calcular_conflitos(sucessor)
            if conflitos < menor_conflitos:
                menor_conflitos = conflitos
                melhor_estado = sucessor

        print(f"Estado atual: {estado_atual} | Conflitos: {conflitos_atual}")
        print(f"Melhor sucessor: {melhor_estado} | Conflitos: {menor_conflitos}")

        # Se não houver melhora, retornar o caminho
        if menor_conflitos >= conflitos_atual:
            print("Nenhuma melhoria possível. Parando a busca.")
            return caminho

        # Atualizar o estado atual
        estado_atual = melhor_estado
        caminho.append(estado_atual)

# Caso 1: Estado inicial já é solução
def caso_1():
    estado_inicial = [0, 4, 7, 5, 2, 6, 1, 3]  # Solução válida sem conflitos
    print("\n--- Caso 1: Solução inicial ---")
    start_time = time.time()
    caminho = busca_gulosa(estado_inicial)
    end_time = time.time()
    exibir_resultado(caminho, end_time - start_time)

# Caso 2: Todas as rainhas em ataques na diagonal principal
def caso_2():
    estado_inicial = [0, 1, 2, 3, 4, 5, 6, 7]  # Totalmente conflituoso
    print("\n--- Caso 2: Rainhas em ataque na diagonal principal ---")
    start_time = time.time()
    caminho = busca_gulosa(estado_inicial)
    end_time = time.time()
    exibir_resultado(caminho, end_time - start_time)

# Caso 3: Estado aleatório
def caso_3():
    estado_inicial = [4, 1, 5, 3, 6, 7, 0, 2]
    print("\n--- Caso 3: Opcional ---")
    start_time = time.time()
    caminho = busca_gulosa(estado_inicial)
    end_time = time.time()
    exibir_resultado(caminho, end_time - start_time)

# Exibir resultado final
def exibir_resultado(caminho, tempo_execucao):
    print("\nCaminho para a solução:")
    for passo, estado in enumerate(caminho):
        print(f"Passo {passo}: {estado} | Conflitos: {calcular_conflitos(estado)}")
    print(f"Tempo de processamento: {tempo_execucao:.6f} segundos")
    print(f"Total de passos: {len(caminho)}\n")


# Executar os casos
def main():
    caso_1()
    caso_2()
    caso_3()

if __name__ == "__main__":
    main()
