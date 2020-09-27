import numpy as np


# l = list(range(10))
# l[::2] = 999
# Throws error --> assign iterable 
# to extended slice


# a = np.arange(10)
# a[::2] = 999
# print(a)
# [999 1 999 3 999 5 999 7 999 9]

# Multi-Demesional arrays example
a = np.arange(16)
a = a.reshape((4,4))
print(a)
# [ 0  1  2  3]
# [ 4  5  6  7]
# [ 8  9 10 11]
# [12 13 14 15]]

print(a[:, 1])
# Second column:
# [ 1  5  9 13]

print(a[1, :])
# Second row:
# [4 5 6 7]

print(a[1, ::2])
# Second row, every other element
# [4 6]

print(a[:, :-1])
# All columns except last one
# [[ 0  1  2]
# [ 4  5  6]
# [ 8  9 10]
# [12 13 14]]

print(a[:-1])
# Same as a[:-1, :]
# [[ 0  1  2  3]
# [ 4  5  6  7]
# [ 8  9 10 11]]