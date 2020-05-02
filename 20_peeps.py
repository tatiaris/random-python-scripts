from math import factorial

def product(iterable):
    prod = 1
    for n in iterable:
        prod *= n
    return prod

def npr(n, r):
    assert 0 <= r <= n
    return product(range(n - r + 1, n + 1))

print(1 - npr(365, 23)/(365**23))
