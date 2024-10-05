import numpy as np
'''

Utför elementvis multiplikation av två 4x4 matriser.
'''

arr1 = np.array(([1,2,3,2],
                [5,4,2,2],
                [3,2,1,3],
                [2,3,5,2]))

arr2 = np.array(([1,3,3,1],
                [2,1,2,5],
                [2,6,5,7],
                [2,7,3,1]))

arr3 = np.multiply(arr1,arr2)
print(arr3)