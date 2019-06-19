import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# x = np.linspace(0, 10, 100)
# y = np.sin(x)
#
# # plt.plot(x, y)
# # plt.show()
#
# plt.plot(x, y)
# plt.xlabel("Time")
# plt.ylabel("Happiness")
# plt.title("Happiness over time")
# plt.show()


A = pd.read_csv("data_1d.csv", header=None).to_numpy()
x = A[:,0]
y = A[:,1]
# print(x.shape)

# plt.scatter(x,y)
# plt.show()

# x_line = np.linspace(0, 100, 100)
# y_line = 2*x_line + 1
# plt.scatter(x, y)
# plt.plot(x_line, y_line)
# plt.show()


# # plt.hist(x)
# # plt.show()
#
# # R = np.random.random(10000)
# # plt.hist(R,bins=20)
# # plt.show()
#
# y_actual = 2 * x + 1
# residuals = y - y_actual
# plt.hist(residuals, bins=20)
# plt.show()