import random


def tabu_search(problem, initial_state, max_iterations, tabu_tenure):
    """
    Implementação do algoritmo Tabu Search.

    Args:
        problem (dict): Um dicionário contendo:
            - 'neighbors': Função que retorna os vizinhos de um estado.
            - 'objective': Função que calcula o valor da função objetivo para um estado.
        initial_state (any): Estado inicial do problema.
        max_iterations (int): Número máximo de iterações.
        tabu_tenure (int): Número de iterações para manter um movimento tabu na lista tabu.

    Returns:
        tuple: O melhor estado encontrado e seu valor objetivo.
    """
    current_state = initial_state
    current_value = problem['objective'](current_state)
    best_state = current_state
    best_value = current_value

    # Inicializa a lista tabu (não podemos reverter para os estados já visitados)
    tabu_list = []

    iteration = 0
    while iteration < max_iterations:
        neighbors = problem['neighbors'](current_state)
        best_neighbor = None
        best_neighbor_value = float('-inf')

        for neighbor in neighbors:
            if neighbor not in tabu_list:
                neighbor_value = problem['objective'](neighbor)
                if neighbor_value > best_neighbor_value:
                    best_neighbor = neighbor
                    best_neighbor_value = neighbor_value

        # Atualiza o estado atual
        current_state = best_neighbor
        current_value = best_neighbor_value

        # Se o novo estado for o melhor encontrado, atualiza o melhor estado
        if current_value > best_value:
            best_state = current_state
            best_value = current_value

        # Adiciona o movimento atual à lista tabu
        tabu_list.append(current_state)

        # Mantém a lista tabu com um tamanho máximo, removendo o item mais antigo
        if len(tabu_list) > tabu_tenure:
            tabu_list.pop(0)

        iteration += 1

    return best_state, best_value


# Exemplo de uso
if __name__ == "__main__":
    # Definição do problema
    def neighbors(state):
        # Vizinhos são estados próximos (incrementos ou decrementos de 1)
        return [state - 1, state + 1]


    def objective(state):
        # Exemplo: função objetivo é maximizar -(x-3)^2 + 9 (máximo em x=3)
        return -(state - 3) ** 2 + 9


    problem = {
        'neighbors': neighbors,
        'objective': objective
    }

    # Parâmetros do Tabu Search
    initial_state = random.randint(-10, 10)  # Estado inicial aleatório
    max_iterations = 100  # Número máximo de iterações
    tabu_tenure = 5  # Tamanho da lista tabu

    # Executando Tabu Search
    best_state, best_value = tabu_search(problem, initial_state, max_iterations, tabu_tenure)

    print(f"Estado inicial: {initial_state}")
    print(f"Melhor estado encontrado: {best_state}")
    print(f"Valor objetivo do melhor estado: {best_value}")
