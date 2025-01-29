def dfs_recursive(graph, node, visited=None):
    """
    Implementação do algoritmo de Busca em Profundidade (DFS) usando recursão.

    Args:
        graph (dict): Grafo representado como um dicionário de listas de adjacência.
        node (any): Nó inicial para começar a busca.
        visited (set): Conjunto de nós já visitados.

    Returns:
        list: Ordem dos nós visitados durante a busca.
    """
    if visited is None:
        visited = set()

    visited.add(node)
    result = [node]  # Adiciona o nó atual ao resultado

    # Visita recursivamente os vizinhos que ainda não foram visitados
    for neighbor in graph.get(node, []):
        if neighbor not in visited:
            result.extend(dfs_recursive(graph, neighbor, visited))

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
    traversal_order = dfs_recursive(graph, start_node)

    print("Ordem de visita dos nós (DFS - Recursivo):", traversal_order)
