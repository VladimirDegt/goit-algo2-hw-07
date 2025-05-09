import timeit
from functools import lru_cache
import matplotlib.pyplot as plt

# Реалізація функції з LRU-кешем
@lru_cache(maxsize=None)
def fibonacci_lru(n):
    if n < 2:
        return n
    return fibonacci_lru(n-1) + fibonacci_lru(n-2)

# Реалізація Splay Tree
class SplayTreeNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

class SplayTree:
    def __init__(self):
        self.root = None

    def _splay(self, root, key):
        if root is None or root.key == key:
            return root

        if key < root.key:
            if root.left is None:
                return root
            if key < root.left.key:
                root.left.left = self._splay(root.left.left, key)
                root = self._rotate_right(root)
            elif key > root.left.key:
                root.left.right = self._splay(root.left.right, key)
                if root.left.right is not None:
                    root.left = self._rotate_left(root.left)
            return root if root.left is None else self._rotate_right(root)
        else:
            if root.right is None:
                return root
            if key < root.right.key:
                root.right.left = self._splay(root.right.left, key)
                if root.right.left is not None:
                    root.right = self._rotate_right(root.right)
            elif key > root.right.key:
                root.right.right = self._splay(root.right.right, key)
                root = self._rotate_left(root)
            return root if root.right is None else self._rotate_left(root)

    def _rotate_left(self, x):
        y = x.right
        x.right = y.left
        y.left = x
        return y

    def _rotate_right(self, x):
        y = x.left
        x.left = y.right
        y.right = x
        return y

    def insert(self, key, value):
        if self.root is None:
            self.root = SplayTreeNode(key, value)
            return
        self.root = self._splay(self.root, key)
        if self.root.key == key:
            self.root.value = value
            return
        new_node = SplayTreeNode(key, value)
        if key < self.root.key:
            new_node.right = self.root
            new_node.left = self.root.left
            self.root.left = None
        else:
            new_node.left = self.root
            new_node.right = self.root.right
            self.root.right = None
        self.root = new_node

    def find(self, key):
        self.root = self._splay(self.root, key)
        if self.root and self.root.key == key:
            return self.root.value
        return None

# Реалізація функції з Splay Tree
def fibonacci_splay(n, tree):
    if n < 2:
        return n
    cached_value = tree.find(n)
    if cached_value is not None:
        return cached_value
    result = fibonacci_splay(n-1, tree) + fibonacci_splay(n-2, tree)
    tree.insert(n, result)
    return result

# Вимірювання часу виконання
n_values = list(range(0, 951, 50))
lru_times = []
splay_times = []

for n in n_values:
    # Вимірювання часу для LRU-кешу
    lru_time = timeit.timeit(lambda: fibonacci_lru(n), number=10)
    lru_times.append(lru_time)

    # Вимірювання часу для Splay Tree
    splay_tree = SplayTree()
    splay_time = timeit.timeit(lambda: fibonacci_splay(n, splay_tree), number=10)
    splay_times.append(splay_time)

# Побудова графіка
plt.plot(n_values, lru_times, label='LRU Cache', marker='o')
plt.plot(n_values, splay_times, label='Splay Tree', marker='x')
plt.xlabel('n')
plt.ylabel('Середній час виконання (секунди)')
plt.title('Порівняння продуктивності обчислення чисел Фібоначчі')
plt.legend()
plt.grid(True)
plt.show()

# Виведення таблиці результатів
print(f"{'n':<10}{'LRU Cache Time (s)':<20}{'Splay Tree Time (s)':<20}")
print('-' * 50)
for n, lru_time, splay_time in zip(n_values, lru_times, splay_times):
    print(f"{n:<10}{lru_time:<20.10f}{splay_time:<20.10f}")