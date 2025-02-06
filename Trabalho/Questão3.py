import heapq
# Inicializando as variáveis diretamente no código
distancia_direta  = [
    [0, 11, 20, 27, 40, 43, 39, 28, 18, 10, 18, 30, 30, 32],  # E1
    [0, 0, 9, 16, 29, 32, 28, 19, 11, 4, 17, 23, 21, 24],    # E2
    [0, 0, 0, 7, 20, 22, 19, 15, 10, 11, 21, 21, 13, 18],    # E3
    [0, 0, 0, 0, 13, 16, 12, 13, 13, 18, 26, 21, 11, 17],    # E4
    [0, 0, 0, 0, 0, 3, 2, 21, 25, 31, 38, 27, 16, 20],       # E5
    [0, 0, 0, 0, 0, 0, 4, 23, 28, 33, 41, 30, 17, 20],       # E6
    [0, 0, 0, 0, 0, 0, 0, 22, 25, 29, 38, 28, 13, 17],       # E7
    [0, 0, 0, 0, 0, 0, 0, 0, 9, 22, 18, 7, 25, 30],          # E8
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 13, 12, 12, 23, 28],         # E9
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 20, 27, 20, 23],          # E10
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 15, 35, 39],           # E11
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 31, 37],            # E12
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5],              # E13
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]               # E14
]

distancia_real  = [
 #   1  2  3   4  5  6  7  8  9 10 11 12 13 14
    [0, 11, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],# E1
    [0, 0, 9, 0, 0, 0, 0, 0, 11, 4, 0, 0, 0, 0],# E2
    [0, 0, 0, 7, 0, 0, 0, 0, 10, 0, 0, 0, 19, 0],# E3
    [0, 0, 0, 0, 14, 0, 0, 16, 0, 0, 0, 0, 12, 0],# E4
    [0, 0, 0, 0, 0, 3, 2, 33, 0, 0, 0, 0, 0, 0],# E5
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],# E6
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],# E7
    [0, 0, 0, 0, 0, 0, 0, 0, 10, 0, 0, 7, 0, 0],# E8
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 14, 0, 0, 0],# E9
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],# E10
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],# E11
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],# E12
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5],# E13
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]# E14
]

#Cada linha representa uma estação,
# e cada coluna na linha indica a conexão com outra estação.
linhas_metro  = [
    [0, 'Azul', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],                        # E1
    ['Azul', 0, 'Azul', 0, 0, 0, 0, 0, 'Amarelo', 'Amarelo', 0, 0, 0, 0],   # E2
    [0, 'Azul', 0, 'Azul', 0, 0, 0, 0, 'Vermelho', 0, 0, 0, 'Vermelho', 0], # E3
    [0, 0, 'Azul', 0, 'Azul', 0, 0, 'Verde', 0, 0, 0, 0, 'Verde', 0],       # E4
    [0, 0, 0, 'Azul', 0, 'Azul', 'Amarelo', 'Amarelo', 0, 0, 0, 0, 0, 0],   # E5
    [0, 0, 0, 0, 'Azul', 0, 0, 0, 0, 0, 0, 0, 0, 0],                        # E6
    [0, 0, 0, 0, 'Amarelo', 0, 0, 0, 0, 0, 0, 0, 0, 0],                     # E7
    [0, 0, 0, 'Verde', 'Amarelo', 0, 0, 0, 'Amarelo', 0, 0, 'Verde', 0, 0], # E8
    [0, 'Amarelo', 'Vermelho', 0, 0, 0, 0, 'Amarelo', 0, 0, 'Vermelho', 0, 0, 0],# E9
    [0, 'Amarelo', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],                     # E10
    [0, 0, 0, 0, 0, 0, 0, 0, 'Vermelho', 0, 0, 0, 0, 0],                    # E11
    [0, 0, 0, 0, 0, 0, 0, 'Verde', 0, 0, 0, 0, 0, 0],                       # E12
    [0, 0, 'Vermelho', 'Verde', 0, 0, 0, 0, 0, 0, 0, 0, 0, 'Verde', 0],     # E13
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'Verde', 0]                        # E14
]


class FilaPrioridade:
    def __init__(self):
        self.estacoes = []

    def inserir(self, estacao, custo):
        heapq.heappush(self.estacoes, (custo, estacao))

    def remover(self):
        return heapq.heappop(self.estacoes)

    def fronteira(self):
        return sorted(self.estacoes)

    def esta_vazia(self):
        return not self.estacoes


def calcular_distancia_g(estacao_inicio, estacao_fim):
    indice_inicio = int(estacao_inicio.split('E')[1]) - 1
    indice_fim = int(estacao_fim.split('E')[1]) - 1
    if indice_inicio > indice_fim:
        indice_inicio, indice_fim = indice_fim, indice_inicio
    return distancia_real[indice_inicio][indice_fim]


def calcular_heuristica_h(estacao_inicio, estacao_fim):
    indice_inicio = int(estacao_inicio.split('E')[1]) - 1
    indice_fim = int(estacao_fim.split('E')[1]) - 1
    if indice_inicio > indice_fim:
        indice_inicio, indice_fim = indice_fim, indice_inicio
    return distancia_direta[indice_inicio][indice_fim]


def obter_estacoes_adjacentes(atual):
    indice_atual = int(atual.split('E')[1]) - 1
    adjacentes = []
    for i in range(len(distancia_real[indice_atual])):
        if distancia_real[indice_atual][i] != 0.0 and i > indice_atual:
            estacao = "E" + str(i + 1)
            adjacentes.append(estacao)
        if distancia_real[i][indice_atual] != 0.0 and i <= indice_atual:
            estacao = "E" + str(i + 1)
            adjacentes.append(estacao)
    return adjacentes


def busca_a_estrela(estacao_inicio, estacao_destino):
    caminho = {}
    distancia = {}
    fila = FilaPrioridade()
    fila.inserir(estacao_inicio, 0)
    distancia[estacao_inicio] = 0
    caminho[estacao_inicio] = None
    expansao = []
    imprimir_percurso(estacao_inicio, estacao_destino, caminho, distancia, expansao, fila, 0)

    while not fila.esta_vazia():
        atual = fila.remover()[1]
        expansao.append(atual)

        if atual == estacao_destino:
            break

        adjacentes = obter_estacoes_adjacentes(atual)

        for estacao in adjacentes:
            custo_g = distancia[atual] + calcular_distancia_g(atual, estacao)
            if estacao not in distancia or custo_g < distancia[estacao]:
                distancia[estacao] = custo_g
                custo_f = custo_g + calcular_heuristica_h(estacao, estacao_destino)
                fila.inserir(estacao, custo_f)
                caminho[estacao] = atual

        imprimir_percurso(estacao_inicio, estacao_destino, caminho, distancia, expansao, fila, 1)

    imprimir_percurso(estacao_inicio, estacao_destino, caminho, distancia, expansao, fila, 2)


def imprimir_percurso(inicio, fim, caminho, distancia, expansao, fila, nivel):
    caminho_final = []
    estacao_atual = fim

    if nivel == 0:
        print(f'\nPartiremos de {inicio} e iremos até {fim}\n')
    if nivel == 2:
        while caminho.get(estacao_atual) is not None:
            caminho_final.append(estacao_atual)
            estacao_atual = caminho[estacao_atual]
        caminho_final.append(inicio)
        caminho_final.reverse()

        print(f'Caminho mais rápido de {inicio} para {fim}: {" -> ".join(caminho_final)}\n')

        print('Detalhes do percurso:')
        tempo_total = 0
        distancia_total = 0
        trocas_linha = 0
        linha_atual = None

        for i in range(len(caminho_final) - 1):
            estacao_atual = caminho_final[i]
            estacao_proxima = caminho_final[i + 1]
            indice_atual = int(estacao_atual.split('E')[1]) - 1
            indice_proxima = int(estacao_proxima.split('E')[1]) - 1

            distancia_trecho = distancia_real[indice_atual][indice_proxima] if indice_atual < indice_proxima else \
            distancia_real[indice_proxima][indice_atual]
            distancia_total += distancia_trecho

            tempo_trecho = (distancia_trecho / 30) * 60
            tempo_total += tempo_trecho

            linha_proxima = linhas_metro[indice_atual][indice_proxima]
            if i > 0 and linha_proxima != linha_atual:
                tempo_total += 5
                trocas_linha += 1
                print(f"  ** Troca de linha em {estacao_atual}, adicionando 5 minutos **")

            print(f"{estacao_atual} -> {estacao_proxima}: {distancia_trecho:.2f} km, {tempo_trecho:.2f} minutos")

            linha_atual = linha_proxima

        print(f'\nDistância total: {distancia_total:.2f} km')
        print(f'Tempo total estimado: {tempo_total:.2f} minutos')
        print(f'Trocas de linha: {trocas_linha}')


def main():
    inicio = input('Digite a estação de início: ').upper()
    fim = input('Digite a estação de destino: ').upper()
    busca_a_estrela(inicio, fim)


if __name__ == "__main__":
    main()