import numpy as np
from numpy import random
import matplotlib.pyplot as plt
'''
Generera en array med 1000 prover från 
en binomialfördelning med n=10 och p=0,5.
'''

rng = random.binomial(n=10, p=0.5, size=1000)

plt.hist(rng, bins=10, edgecolor='red')

plt.show()