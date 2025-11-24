import heapq

class Node:
    def __init__(self, level, value, weight, bound):
        self.level = level
        self.value = value
        self.weight = weight
        self.bound = bound

    # Para usar heapq como max-heap, invertendo o bound
    def __lt__(self, other):
        return self.bound > other.bound

def branch_and_bound_knapsack(values, weights, capacity):
    n = len(values)

    # Ordenar por valor/peso (decrescente)
    items = list(zip(values, weights))
    items.sort(key=lambda x: x[0]/x[1], reverse=True)
    values, weights = zip(*items)

    def bound(node):
        if node.weight >= capacity:
            return 0
        
        profit_bound = node.value
        j = node.level + 1
        totweight = node.weight

        # adicionar itens completos
        while j < n and totweight + weights[j] <= capacity:
            totweight += weights[j]
            profit_bound += values[j]
            j += 1

        # adicionar parte fracionária do próximo item, se existir
        if j < n:
            profit_bound += (capacity - totweight) * (values[j] / weights[j])

        return profit_bound

    # Criar nó raiz
    root = Node(level=-1, value=0, weight=0, bound=0)
    root.bound = bound(root)

    max_profit = 0
    pq = []
    heapq.heappush(pq, root)

    while pq:
        node = heapq.heappop(pq)

        # Se não pode melhorar, poda
        if node.bound <= max_profit:
            continue

        level = node.level + 1

        # ----- Ramo: inclui item -----
        left = Node(
            level=level,
            value=node.value + values[level],
            weight=node.weight + weights[level],
            bound=0
        )

        if left.weight <= capacity:
            if left.value > max_profit:
                max_profit = left.value

            left.bound = bound(left)
            if left.bound > max_profit:
                heapq.heappush(pq, left)

        # ----- Ramo: não inclui item -----
        right = Node(
            level=level,
            value=node.value,
            weight=node.weight,
            bound=0
        )

        right.bound = bound(right)
        if right.bound > max_profit:
            heapq.heappush(pq, right)

    return max_profit

# Exemplo de uso
values  = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50

print(branch_and_bound_knapsack(values, weights, capacity))
# Saída esperada: 220
