import random
import time
from collections import OrderedDict

# Ініціалізація масиву
N = 100_000
array = [random.randint(1, 100) for _ in range(N)]

# Генерація запитів
Q = 50_000
queries = []
for _ in range(Q):
    if random.choice(['Range', 'Update']) == 'Range':
        L = random.randint(0, N-1)
        R = random.randint(L, N-1)
        queries.append(('Range', L, R))
    else:
        index = random.randint(0, N-1)
        value = random.randint(1, 100)
        queries.append(('Update', index, value))

# Функції без кешу
def range_sum_no_cache(array, L, R):
    return sum(array[L:R+1])

def update_no_cache(array, index, value):
    array[index] = value

# Реалізація LRU-кешу
class LRUCache:
    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        if key not in self.cache:
            return None
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)

# Функції з кешем
lru_cache = LRUCache(1000)

def range_sum_with_cache(array, L, R):
    key = (L, R)
    cached_result = lru_cache.get(key)
    if cached_result is not None:
        return cached_result
    result = sum(array[L:R+1])
    lru_cache.put(key, result)
    return result

def update_with_cache(array, index, value):
    array[index] = value
    # Очищення кешу, оскільки зміни в масиві можуть вплинути на всі збережені суми
    lru_cache.cache.clear()

# Вимірювання часу виконання
start_time = time.time()
for query in queries:
    if query[0] == 'Range':
        range_sum_no_cache(array, query[1], query[2])
    else:
        update_no_cache(array, query[1], query[2])
no_cache_time = time.time() - start_time

start_time = time.time()
for query in queries:
    if query[0] == 'Range':
        range_sum_with_cache(array, query[1], query[2])
    else:
        update_with_cache(array, query[1], query[2])
cache_time = time.time() - start_time

# Виведення результатів
print(f"Час виконання без кешування: {no_cache_time:.2f} секунд")
print(f"Час виконання з LRU-кешем: {cache_time:.2f} секунд")