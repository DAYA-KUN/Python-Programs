import numpy as np

#matrix creation
matrix = np.array([[1,2],[3,4]])
print(matrix)

#matrix addition
matrix1 = np.array([[1,2],[3,4]])
matrix2 = np.array([[5,6],[7,8]])
c=matrix1+matrix2
print(c)

#matrix subtraction
c=matrix1-matrix2
print(c)

#Mulipying matrix elements
c=matrix1*matrix2
print(c)

#matrix multiplication
c=np.dot(matrix1,matrix2)
print(c)

#matrix transpose
c=matrix1.T
print(c)

#determinant
d=np.linalg.det(matrix1)
d=round(d,2) #-2.0000004
print(d)