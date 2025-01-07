import math
import random


def simulated_annealing(problem, initial_state, initial_temperature, cooling_rate, min_temperature):
    """
    Implementação do algoritmo de Simulated Annealing.

    Args:
        problem (dict): Um dicionário contendo:
            - 'neighbors': Função que retorna os vizinhos de um estado.
            - 'objective': Função que calcula o valor da função objetivo para um estado.
        initial_state (any): Estado inicial do problema.
        initial_temperature (float): Temperatura inicial.
        cooling_rate (float): Taxa de resfriamento (deve ser entre 0 e 1).
        min_temperature (float): Temperatura mínima para encerrar o algoritmo.

    Returns:
        tuple: O melhor estado encontrado e seu valor objetivo.
    """
    current_state = initial_state
    current_value = problem['objective'](current_state)
    temperature = initial_temperature

    while temperature > min_temperature:
        # Gera um vizinho aleatório
        neighbor = random.choice(problem['neighbors'](current_state))
        neighbor_value = problem['objective'](neighbor)

        # Calcula a mudança no valor da função objetivo
        delta = neighbor_value - current_value

        # Decide aceitar o vizinho
        if delta > 0 or math.exp(delta / temperature) > random.random():
            current_state = neighbor
            current_value = neighbor_value

        # Resfria a temperatura
        temperature *= cooling_rate

    return current_state, current_value


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

    # Parâmetros do Simulated Annealing
    initial_state = random.randint(-10, 10)  # Estado inicial aleatório
    initial_temperature = 100.0  # Temperatura inicial
    cooling_rate = 0.95  # Taxa de resfriamento
    min_temperature = 0.1  # Temperatura mínima

    # Executando Simulated Annealing
    best_state, best_value = simulated_annealing(problem, initial_state, initial_temperature, cooling_rate,
                                                 min_temperature)

    print(f"Estado inicial: {initial_state}")
    print(f"Melhor estado encontrado: {best_state}")
    print(f"Valor objetivo do melhor estado: {best_value}")
