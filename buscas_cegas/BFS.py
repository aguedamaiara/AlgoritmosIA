from collections import deque


def bfs(graph, start_node):
    """
    Implementação do algoritmo de Busca em Largura (BFS).

    Args:
        graph (dict): Grafo representado como um dicionário de listas de adjacência.
        start_node (any): Nó inicial para começar a busca.

    Returns:
        list: Ordem dos nós visitados durante a busca.
    """
    visited = set()  # Conjunto de nós visitados
    queue = deque([start_node])  # Fila para explorar os nós
    result = []  # Lista de nós na ordem de visita

    while queue:
        # Retira o primeiro elemento da fila
        current_node = queue.popleft()

        # Verifica se o nó já foi visitado
        if current_node not in visited:
            visited.add(current_node)  # Marca como visitado
            result.append(current_node)  # Adiciona ao resultado

            # Adiciona vizinhos à fila
            for neighbor in graph.get(current_node, []):
                if neighbor not in visited:
                    queue.append(neighbor)

    return result


# Exemplo de uso
if __name__ == "__main__":
    # Grafo exemplo
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }

    # Executando BFS a partir do nó 'A'
    start_node = 'A'
    traversal_order = bfs(graph, start_node)

    print("Ordem de visita dos nós (BFS):", traversal_order)
