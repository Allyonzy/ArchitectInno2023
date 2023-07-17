import numpy as np

#элемент numpy от 0 до 2.7, с шагом 0.5
vec01 = np.arange(2.7, step=0.5,dtype='float')
print(vec01)
print(len(vec01))

vec02 = np.arange(1, 10, dtype='int')
print(vec02)
print(len(vec02))

matrix_from_vec01 = vec01.reshape(2, 3)
print(matrix_from_vec01)

matrix_from_vec02 = vec02.reshape(3, 3)
print(matrix_from_vec02)

result = np.matmul(matrix_from_vec01, matrix_from_vec02) 
print(result)

matrix_task04 = np.arange(1, 50, dtype='int64')
result = matrix_task04[(matrix_task04 % 2 == 0)]

print(", ".join(map(str, matrix_task04)))
print(result)

matrix_zeros = np.zeros((16, 16))
print(matrix_zeros)
matrix_zeros[0::3, ::2] = 8
matrix_zeros[::4] = 8
print(matrix_zeros)

matrix_zeros[::4] = 8
print(matrix_zeros)

matrix_zeros[:, 2] = 4
print(matrix_zeros)

matrix_zeros[::2, 1:4] = 3
print(matrix_zeros)

matrix_zeros[0::2, ::2] = 9
matrix_zeros[1::2, 1::2] = 9
print(matrix_zeros)
