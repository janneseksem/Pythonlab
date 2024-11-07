'''
Skapa en 3x3 matris av slumpmässiga heltal mellan 1 och 10.
'''

import numpy as np
import random

arr = np.random.randint(0,10, (3,3))

print(arr)