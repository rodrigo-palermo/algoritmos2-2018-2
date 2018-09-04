"""Compute a random list and its parity, with True (even) or False (odd)."""


from sistema import is_even
import random

L = [random.randint(0, 100) for x in range(random.randint(10, 100))]

parity_L = is_even(L)

print(L)
print(parity_L)
