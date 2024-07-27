import heapq

def min_cost_to_connect_cables(cables):
    # Створюємо мін-купу з кабелів
    heapq.heapify(cables)
    total_cost = 0
    
    while len(cables) > 1:
        # Витягуємо два найменших кабелі
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)
        
        # Вартість з'єднання цих двох кабелів
        cost = first + second
        total_cost += cost
        
        # Додаємо новий кабель назад у мін-купу
        heapq.heappush(cables, cost)
    
    return total_cost

# Приклад використання
cables = [5, 13, 22, 1]
min_cost = min_cost_to_connect_cables(cables)
print("Мінімальні витрати на з'єднання кабелів:", min_cost)