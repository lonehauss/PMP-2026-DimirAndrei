"""
Ex. 3
pentru intrebarea "de ce?" explicatia mea ar fi ca, in fiecare ora, fiecare frizer face 3,6, respectiv 4 clienti asa ca tu ai sanse egale sa fii oricare dintre acei clienti si luand numarul cazul favorabile/numarul cazurilor totale egaleaza 3/13, 6/13, respectiv 4/13
"""

import numpy as np
from scipy.stats import gaussian_kde
from matplotlib import pyplot as plt

f1 = 3
f2 = 6
f3 = 4

prob = [3/13, 6/13, 4/13]

N = 10000

frizer = np.random.choice([1,2,3], size=N, p=prob)

T = []

for f in frizer:
    if f == 1:
        t = np.random.exponential(scale=1/3)
    elif f == 2:
        t = np.random.exponential(scale=1/6)
    else:
        t = np.random.exponential(scale=1/4)

    T.append(t)

media = sum(T)/len(T)
dev_standard = np.std(T)

print("Media: " + str(media))
print("Deviatia standard: " + str(dev_standard))

T = np.array(T)

kde = gaussian_kde(T)

x = np.linspace(min(T), max(T), 500)

plt.plot(x, kde(x))
plt.xlabel("Timp de servire")
plt.ylabel("Densitate")
plt.show()