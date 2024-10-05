import numpy as np
'''
Använd NumPy för att lösa ett system av linjära ekvationer 
(Ax = b).
'''
a = np.array(([2, 1, -1],
              [-3, -1, 2],
              [-2, 1, 2]))

b = np.array(([8],
              [-11],
              [-3]))

# print(a)
# print(b)

line = np.linalg.solve(a,b)

print(line)