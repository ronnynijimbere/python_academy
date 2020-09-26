import numpy as np

# a = np.array([1, 2, 3])
# print(a.ndim)
# # 1

# b = np.array([[1, 2], [2, 3], [3, 4]])
# print(b.ndim)
# # 2

# c = np.array([[[1, 2], [2, 3], [3, 4]],
#               [[1, 2], [2, 3], [3, 4]]])
# print(c.ndim)
# # 3

a = np.array([1, 2, 3])
print(a.shape)
# (3, )

b = np.array([[1, 2], [2, 3], [3, 4]])
print(b.shape)
# (3, 2)

c = np.array([[[1, 2], [2, 3], [3, 4]],
              [[1, 2], [2, 3], [3, 4]]])
print(c.shape)
# (2, 3, 2)