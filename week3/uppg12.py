'''
Skapa en 5x5 identitetsmatris och ersätt sedan dess 
diagonal med en anpassad array.
'''
import numpy as np

arr = np.identity(5)
arr1 = np.array([3,2,5,6,7])

np.fill_diagonal(arr, arr1)
# print(arr)

print(arr)

