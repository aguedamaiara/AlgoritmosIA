def dfs_iterative(graph, start_node):
    """
    Implementação do algoritmo de Busca em Profundidade (DFS) usando uma pilha.

    Args:
        graph (dict): Grafo representado como um dicionário de listas de adjacência.
        start_node (any): Nó inicial para começar a busca.

    Returns:
        list: Ordem dos nós visitados durante a busca.
    """
    visited = set()  # Conjunto de nós visitados
    stack = [start_node]  # Pilha para gerenciar os nós a visitar
    result = []  # Lista de nós na ordem de visita

    while stack:
        # Remove o último elemento da pilha
        current_node = stack.pop()

        if current_node not in visited:
            visited.add(current_node)  # Marca como visitado
            result.append(current_node)  # Adiciona ao resultado

            # Adiciona os vizinhos à pilha (em ordem reversa para preservar a sequência)
            for neighbor in reversed(graph.get(current_node, [])):
                if neighbor not in visited:
                    stack.append(neighbor)

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

    # Executando DFS a partir do nó 'A'
    start_node = 'A'
    traversal_order = dfs_iterative(graph, start_node)

    print("Ordem de visita dos nós (DFS - Iterativo):", traversal_order)
