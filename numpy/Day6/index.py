import numpy as np


a = np.arange(0, 10)
print(a)
# [0 1 2 3 4 5 6 7 8 9]

print(a[:])
# [0 1 2 3 4 5 6 7 8 9]

print(a[1:])
# [1 2 3 4 5 6 7 8 9]

print(a[1:3])
# [1 2]

print(a[1:-1])
# [1 2 3 4 5 6 7 8]

print(a[::2])
# [0 2 4 6 8]

print(a[1::2])
# [1 3 5 7 9]

print(a[::-1])
# [9 8 7 6 5 4 3 2 1 0]

print(a[:1:-2])
# [9 7 5 3]

print(a[-1:1:-2])
# [9 7 5 3]