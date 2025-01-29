import random


# Função de avaliação (fitness function)
def fitness_function(x):
    return x ** 2  # Maximizar x^2


# Geração da população inicial
def create_population(pop_size, x_min, x_max):
    return [random.randint(x_min, x_max) for _ in range(pop_size)]


# Seleção: escolher os melhores indivíduos com base no fitness
def selection(population, fitness_values, num_parents):
    selected_parents = random.choices(population, weights=fitness_values, k=num_parents)
    return selected_parents


# Cruzamento: criar filhos a partir de dois pais
def crossover(parents, crossover_rate):
    if random.random() < crossover_rate:
        # Ponto de corte para o cruzamento
        crossover_point = random.randint(1, 31)  # Ponto de corte para inteiros de 32 bits
        mask = (1 << crossover_point) - 1
        child1 = (parents[0] & mask) | (parents[1] & ~mask)
        child2 = (parents[1] & mask) | (parents[0] & ~mask)
        return child1, child2
    else:
        return parents[0], parents[1]


# Mutação: alterar aleatoriamente o gene de um indivíduo
def mutation(child, mutation_rate, x_min, x_max):
    if random.random() < mutation_rate:
        # Variação aleatória no valor do gene (mudança pequena)
        mutation_amount = random.randint(-1, 1)  # Variação pequena
        child += mutation_amount
        # Garantir que o gene não saia dos limites
        child = max(min(child, x_max), x_min)
    return child


# Algoritmo Genético
def genetic_algorithm(pop_size, x_min, x_max, generations, crossover_rate, mutation_rate, num_parents):
    # Inicializar a população
    population = create_population(pop_size, x_min, x_max)

    # Evolução
    for generation in range(generations):
        # Avaliar a aptidão de cada indivíduo
        fitness_values = [fitness_function(individual) for individual in population]

        # Exibir a melhor solução em cada geração
        best_individual = population[fitness_values.index(max(fitness_values))]
        print(f"Geração {generation + 1}: Melhor indivíduo = {best_individual}, Fitness = {max(fitness_values)}")

        # Seleção dos pais
        parents = selection(population, fitness_values, num_parents)

        # Criação da nova população através de cruzamento e mutação
        new_population = []
        for i in range(0, len(parents), 2):
            parent1, parent2 = parents[i], parents[i + 1] if i + 1 < len(parents) else parents[i]
            child1, child2 = crossover([parent1, parent2], crossover_rate)
            new_population.append(mutation(child1, mutation_rate, x_min, x_max))
            new_population.append(mutation(child2, mutation_rate, x_min, x_max))

        # Substituição da população
        population = new_population[:pop_size]  # Manter o tamanho da população constante

    # Retorna o melhor indivíduo encontrado
    best_individual = population[fitness_values.index(max(fitness_values))]
    return best_individual


# Parâmetros do Algoritmo Genético
pop_size = 10  # Tamanho da população
x_min = -10  # Valor mínimo para o gene
x_max = 10  # Valor máximo para o gene
generations = 20  # Número de gerações
crossover_rate = 0.7  # Taxa de cruzamento
mutation_rate = 0.1  # Taxa de mutação
num_parents = 6  # Número de pais a serem selecionados

# Executando o algoritmo
best_solution = genetic_algorithm(pop_size, x_min, x_max, generations, crossover_rate, mutation_rate, num_parents)
print(f"Melhor solução final: {best_solution} com fitness = {fitness_function(best_solution)}")
