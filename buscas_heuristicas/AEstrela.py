import heapq


def a_star_search(graph, start, goal, heuristic):
    """
    Implementação do algoritmo A*.

    Args:
        graph (dict): Grafo representado como um dicionário onde as chaves são nós e os valores
                      são listas de tuplas (vizinho, custo).
        start (any): Nó inicial.
        goal (any): Nó objetivo.
        heuristic (dict): Dicionário contendo os valores heurísticos dos nós.

    Returns:
        list: O caminho do nó inicial ao nó objetivo.
    """
    # Fila de prioridade (min-heap)
    priority_queue = [(0, start, [])]  # (f(n) = g(n) + h(n), nó atual, caminho percorrido)
    visited = set()  # Conjunto de nós visitados
    cost_so_far = {start: 0}  # g(n): custo acumulado até cada nó

    while priority_queue:
        # Retira o nó com menor f(n) da fila
        _, current_node, path = heapq.heappop(priority_queue)

        # Se o nó já foi visitado, pula para o próximo
        if current_node in visited:
            continue

        # Marca o nó como visitado
        visited.add(current_node)

        # Adiciona o nó atual ao caminho
        path = path + [current_node]

        # Verifica se o objetivo foi alcançado
        if current_node == goal:
            return path

        # Expande os vizinhos do nó atual
        for neighbor, cost in graph.get(current_node, []):
            new_cost = cost_so_far[current_node] + cost  # g(n) = custo acumulado até o vizinho

            # Se o vizinho não foi visitado ou um caminho mais barato foi encontrado
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                f_score = new_cost + heuristic[neighbor]  # f(n) = g(n) + h(n)
                heapq.heappush(priority_queue, (f_score, neighbor, path))

    return []  # Retorna uma lista vazia se o objetivo não for alcançado


# Exemplo de uso
if __name__ == "__main__":
    # Grafo exemplo
    graph = {
        'A': [('B', 1), ('C', 4)],
        'B': [('D', 2), ('E', 5)],
        'C': [('F', 1)],
        'D': [('G', 3)],
        'E': [('G', 2)],
        'F': [('G', 2)],
        'G': []
    }

    # Heurística: valores estimados para alcançar 'G'
    heuristic = {
        'A': 7,
        'B': 6,
        'C': 3,
        'D': 3,
        'E': 2,
        'F': 2,
        'G': 0
    }

    # Executando A* para encontrar o caminho de 'A' para 'G'
    start_node = 'A'
    goal_node = 'G'
    path = a_star_search(graph, start_node, goal_node, heuristic)

    print(f"Caminho: {path}")
