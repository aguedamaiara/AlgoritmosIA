import heapq


def uniform_cost_search(graph, start, goal):
    """
    Implementação do algoritmo de Busca de Custo Uniforme (UCS).

    Args:
        graph (dict): Grafo representado como um dicionário onde as chaves são nós e os valores
                      são listas de tuplas (vizinho, custo).
        start (any): Nó inicial.
        goal (any): Nó objetivo.

    Returns:
        tuple: Um par contendo (custo total, caminho) até o nó objetivo.
    """
    # Fila de prioridade para explorar os caminhos de menor custo
    priority_queue = [(0, start, [])]  # (custo acumulado, nó atual, caminho percorrido)
    visited = set()  # Conjunto de nós visitados

    while priority_queue:
        # Retira o nó com o menor custo acumulado
        cost, current_node, path = heapq.heappop(priority_queue)

        # Se o nó já foi visitado, pula para o próximo
        if current_node in visited:
            continue

        # Marca o nó como visitado
        visited.add(current_node)

        # Adiciona o nó atual ao caminho
        path = path + [current_node]

        # Verifica se o objetivo foi alcançado
        if current_node == goal:
            return cost, path

        # Expande os vizinhos do nó atual
        for neighbor, edge_cost in graph.get(current_node, []):
            if neighbor not in visited:
                heapq.heappush(priority_queue, (cost + edge_cost, neighbor, path))

    return float('inf'), []  # Retorna custo infinito se o objetivo não for alcançado


# Exemplo de uso
if __name__ == "__main__":
    # Grafo exemplo com custos nas arestas
    graph = {
        'A': [('B', 1), ('C', 4)],
        'B': [('D', 2), ('E', 5)],
        'C': [('F', 1)],
        'D': [('G', 3)],
        'E': [('G', 2)],
        'F': [('G', 2)],
        'G': []
    }

    # Executando UCS para encontrar o caminho de 'A' para 'G'
    start_node = 'A'
    goal_node = 'G'
    total_cost, path = uniform_cost_search(graph, start_node, goal_node)

    print(f"Custo total: {total_cost}")
    print(f"Caminho: {path}")
