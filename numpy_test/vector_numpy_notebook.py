import numpy as np

print(np.__version__)

vec01 = np.arange(1, 10, dtype='int32')
matrix_01 = vec01.reshape(3,3)