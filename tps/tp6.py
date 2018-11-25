# TP6 : Numpy et Scipy

# -----------------------numpy---------------------------------------#

import numpy as np
from numpy.linalg import *
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

numpyArray = np.arange(24).reshape((4, 3, 2), order='F')

print("Dimension : " + str(numpyArray.ndim))
print("Shape : " + str(numpyArray.shape))
print("Size : " + str(numpyArray.size))
print("DType : " + str(numpyArray.dtype))
print("Item size : " + str(numpyArray.itemsize))
print("Data : " + str(numpyArray.data))

m1 = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

m2 = np.array([
    [3, 4, 5],
    [6, 7, 8],
    [9, 10, 11]
])

m3 = np.array([
    [2, 1, 3],
    [1, 0, 2],
    [2, 0, -2]
])

print("Produit terme à terme \n", m1 * m2)
print("Produit matriciel : \n", m1.dot(m2))
print("Transposé : \n", m1.transpose())
print("Determinant de la matrice :", det(m3))
print("Inverse de la matrice : \n", inv(m3))

C = np.array([0, 1, 2])
result = np.linalg.solve(m1, C)
print("Résultat :", result)

A = np.array([[0, 1], [2, 3]])
print("Les valeurs et vecteurs propres de m1 sont : \n", eig(A))


# ----------------------------------scipy-------------------------------#

def func(x, a, b, c):
    return a * np.exp(-b * x) + c

xdata = np.linspace(0, 4, 50)
y = func(xdata, 2.5, 1.3, 0.5)
y_noise = 0.2 * np.random.normal(size=xdata.size)
ydata = y + y_noise
plt.plot(xdata, ydata, 'b-', label='data')
popt, pcov = curve_fit(func, xdata, ydata)
plt.plot(xdata, func(xdata, *popt), 'r-', label='fit')

plt.xlabel('x')
