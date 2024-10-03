import numpy as np

'''Använd numpy för att:

    Skapa två 3x3 matriser med slumpmässiga heltal.
    Beräkna produkten av dessa matriser.
    Beräkna determinanten för den resulterande matrisen.
'''
#slumpmässigt heltal för två 3x3 matriser
matrix1 = np.random.randint(0, 10, (3,3))
matrix2 = np.random.randint(0, 10, (3,3))
print(matrix1)
print(matrix2)

#Beräkning produkten av matrix1 och matrix2 
product = np.dot(matrix1, matrix2)
print(product)

#Beräkning av determinaten på product resultat

det = np.linalg.det(product)
print(f"\nDeterminant of resultat: {det}")