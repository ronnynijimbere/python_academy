import numpy as np

# a = np.zeros((10, 10, 10, 10, 10))
# print(a.shape)
# # (10, 10, 10, 10, 10)

# b = np.zeros((2,3))
# print(b)
# # [[0. 0. 0.]
# #  [0. 0. 0.]]

# c = np.ones((3, 2, 2))
# print(c)
# # [[[1. 1.]
# #   [1. 1.]]
# #
# # [[1. 1.]
# #  [1. 1.]]
# #
# # [[1. 1.]
# #  [1. 1.]]]

# print(c.dtype)
# # float64

a = np.zeros((2,3), dtype=np.int16)
print(a)
# [[0 0 0]
#  [0 0 0]]

print(a.dtype)
# int16