#############################################################

import numpy as np
import scipy as sp
import scipy.misc as spmis
import matplotlib.pyplot as mpplt

#############################################################

array = np.random.rand(4, 3, 2)
print("ndim=", array.ndim)
print("shape=", array.shape)
print("size=", array.size)
print("dtype=", array.dtype)
print("itemsize=", array.itemsize)
print("data=", array.data)

matrix1 = np.random.randint(0, 9, [3, 3])
matrix2 = np.random.randint(0, 11, [3, 3])
result = np.dot(matrix1, matrix2)
result_transposed = np.transpose(result)

determinant = np.linalg.det(result_transposed)
inverse = np.linalg.inv(result_transposed)
valeurs_vecteurs_propres = np.linalg.eig(result_transposed)

#############################################################

image = spmis.imread("test.jpg")
image = spmis.imresize(image, (250, 250))
mpplt.imshow(image)

#############################################################
