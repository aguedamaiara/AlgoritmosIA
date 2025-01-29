import random


def hill_climbing(problem, initial_state):
    """
    Implementação do algoritmo Hill Climbing.

    Args:
        problem (dict): Um dicionário contendo:
            - 'neighbors': Função que retorna os vizinhos de um estado.
            - 'objective': Função que calcula o valor da função objetivo para um estado.
        initial_state (any): Estado inicial do problema.

    Returns:
        tuple: O melhor estado encontrado e seu valor objetivo.
    """
    current_state = initial_state
    current_value = problem['objective'](current_state)

    while True:
        # Gera os vizinhos do estado atual
        neighbors = problem['neighbors'](current_state)

        # Calcula os valores objetivos dos vizinhos
        neighbor_values = [(neighbor, problem['objective'](neighbor)) for neighbor in neighbors]

        # Encontra o melhor vizinho
        best_neighbor, best_value = max(neighbor_values, key=lambda x: x[1], default=(None, float('-inf')))

        # Se nenhum vizinho melhora o estado atual, encerra
        if best_value <= current_value:
            return current_state, current_value

        # Atualiza o estado atual para o melhor vizinho
        current_state = best_neighbor
        current_value = best_value


# Exemplo de uso
if __name__ == "__main__":
    # Definição do problema
    def neighbors(state):
        # Vizinhos são estados próximos (aqui incrementos ou decrementos de 1)
        return [state - 1, state + 1]


    def objective(state):
        # Exemplo: função objetivo é maximizar -(x-3)^2 + 9 (máximo em x=3)
        return -(state - 3) ** 2 + 9


    problem = {
        'neighbors': neighbors,
        'objective': objective
    }

    # Executando Hill Climbing
    initial_state = random.randint(-10, 10)  # Estado inicial aleatório
    best_state, best_value = hill_climbing(problem, initial_state)

    print(f"Estado inicial: {initial_state}")
    print(f"Melhor estado encontrado: {best_state}")
    print(f"Valor objetivo do melhor estado: {best_value}")
