# First test script for Numpy lib

import numpy as np

# L = np.array([[1, 2],[3,4]])
#
# print(type(L))
#
# a = L.dot(L)
#
# print(a)
# print(L)

# R1 = np.random.random((10,10))
# print(R1)
#
# R2 = np.random.randn(10,10)
# print(R2)
#
# print(R1.var())
# print(R2.var())

A = np.array([ [1.5, 4], [1, 1]])
b = np.array([5050, 2200])

s = np.linalg.solve(A, b)

print(s)