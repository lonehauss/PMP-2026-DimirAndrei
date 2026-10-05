"""
Ex. 2
a. Probabilitea ca jocul sa se opreasca este 1/2 Deci P(N = n) = (1/2)^n
"""

import random
import numpy as np
import matplotlib.pyplot as plt

def simulare():
    N=0
    S=0
    while True:
        N += 1

        moneda = random.randint(0,1)

        if moneda == 1: #stema sa zicem
            z= random.randint(1,6)
            S += z - 3
            break
        else:
            S -= 0.5

    return S

N=10000
results = np.array([simulare() for _ in range(N)])
media_S = sum(results) / len(results)

print(media_S)

plt.hist(results, bins=15, alpha=0.7, color='lightgreen', edgecolor='black')
plt.title('Distributie S')
plt.xlabel('Suma (S)')
plt.ylabel('Numar de jocuri (N)')
plt.show()