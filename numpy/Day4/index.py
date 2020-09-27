import numpy as np


# a = np.array([1, 2, 3])
# print(a)
# # [1 2 3]

# b = np.array((1, 2, 3))
# print(b)
# # [1 2 3]

# c = np.array([1.0, 2.0, 3.0])
# print(c)
# # [1. 2. 3.]




# 2D numpy array
a = np.array([[1, 2, 3], [4, 5, 6]]) 
print(a.shape)

# 3D numpy array
b = np.array([[[1, 2], [3, 4], [5, 6]],
              [[1, 2], [3, 4], [5, 6]]])
print(b.shape)
'''
The shape of array a is (2, 3) because the first axis has two elements and the second axis has three elements. 
The shape of array b is (2, 3, 2) because the first axis has two elements (sequences of sequences), 
the second axis has three elements (sequences), and the third axis has two elements (integers).
'''