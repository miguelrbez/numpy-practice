# Test script for Numpy and Pandas libs

import numpy as np
import pandas as pd
from datetime import datetime

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


# A = np.array([ [1.5, 4], [1, 1]])
# b = np.array([5050, 2200])
#
# s = np.linalg.solve(A, b)
#
# print(s)


# X = []
#
# for line in open("data_2d.csv"):
#     row = line.split(',')
#     # sample = map(float, row)
#     X.append(row)
#     # print(type(row[0]))
#
# X = np.array(X,dtype=float)
#
# print(X.shape)
#
# # print(X)


# X = pd.read_csv("data_2d.csv", header=None)
# print(type(X))
# print(X.info())
# print(X.head(8))

# print(X[0])

# M = X.as_matrix()
# print(M[0])

# Xarr = X.to_numpy()
# print(type(X))
# print(x[0])

# print(X.iloc[0])
# print(X.iloc[[0,2]])
# print(X[[0,2]])
# print(X[ X[0] <5 ])
# print(X[0]<5)


# df = pd.read_csv("international-airline-passengers.csv", engine="python", skipfooter=3)
# # print(df.columns)
# df.columns = ["month", "passengers"]
# # print(df.columns)
# # print(df['passengers'])
# # print(df.passengers)
# df['ones'] = 1
# # print(df)
#
# # print(datetime.strptime("1949-01", "%Y-%m"))
# df['date'] = df.apply(lambda row: datetime.strptime(row['month'], "%Y-%m"), axis=1)
# print(df.info())


t1 = pd.read_csv("table1.csv")
t2 = pd.read_csv("table2.csv")
# print(t1)
# print(t2)
# m = pd.merge(t1, t2, on='user_id')
m = t1.merge(t2, on='user_id')
# m = pd.merge(t1, t2)
print(m)