import random

def random_list(n, start=1, end=100):
    return [random.randint(start, end) for _ in range(n)]

print(random_list(5))
