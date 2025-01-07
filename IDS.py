def depth_limited_search(problem, node, depth_limit):
    """
    Realiza a busca em profundidade com limite de profundidade.

    Args:
        problem (dict): Um dicionário contendo:
            - 'goal_test': Função que verifica se o estado é a solução.
            - 'successors': Função que gera os filhos de um estado.
        node (any): Estado atual.
        depth_limit (int): Limite de profundidade para a busca.

    Returns:
        state (any) ou None: O estado final se encontrado ou None se não encontrado.
    """
    if problem['goal_test'](node):
        return node
    if depth_limit == 0:
        return None

    for child in problem['successors'](node):
        result = depth_limited_search(problem, child, depth_limit - 1)
        if result is not None:
            return result
    return None


def iterative_deepening_search(problem, initial_state, max_depth):
    """
    Realiza a Busca Iterativa em Profundidade (IDS).

    Args:
        problem (dict): Um dicionário contendo:
            - 'goal_test': Função que verifica se o estado é a solução.
            - 'successors': Função que gera os filhos de um estado.
        initial_state (any): Estado inicial do problema.
        max_depth (int): Profundidade máxima para o limite de busca.

    Returns:
        state (any) ou None: O estado final se encontrado ou None se não encontrado.
    """
    for depth in range(max_depth + 1):
        result = depth_limited_search(problem, initial_state, depth)
        if result is not None:
            return result
    return None


# Exemplo de uso
if __name__ == "__main__":
    # Definição do problema
    def goal_test(state):
        return state == "G"  # Objetivo é chegar ao estado "G"


    def successors(state):
        # Gera os sucessores (vizinhos) do estado atual
        if state == "A":
            return ["B", "C"]
        elif state == "B":
            return ["D", "E"]
        elif state == "C":
            return ["F"]
        elif state == "D" or state == "E" or state == "F":
            return []
        else:
            return []


    problem = {
        'goal_test': goal_test,
        'successors': successors
    }

    # Parâmetros da Busca Iterativa em Profundidade
    initial_state = "A"
    max_depth = 5  # Definir a profundidade máxima

    # Executando a Busca Iterativa em Profundidade
    result = iterative_deepening_search(problem, initial_state, max_depth)

    if result:
        print(f"Solução encontrada: {result}")
    else:
        print("Solução não encontrada.")
