What are arrays and matrices in NumPy?

Are you confused about the terms matrices, arrays, vectors?

Don’t despair. In NumPy, there is only one data structure: NumPy arrays. A NumPy array can be one-dimensional, two-dimensional, or 1000-dimensional. It’s one concept to rule them all.

The NumPy array is the core object of the whole library. You have to know it by heart before you can go on and understand the operations provided by the NumPy library. So what is a NumPy array?

It’s a data structure that stores a bunch of numerical values. But there are important restrictions of which values to store.
First, all numerical values have the same data type. In many NumPy tutorials, you will find the terminology: “numpy arrays are homogeneous”.

This means the same thing: all values have the same type. In particular, these are the possible data types of a NumPy array:
bool: The default boolean data type in Python (1 Byte).
int: The default Python integer data type in Python (4 or 8 Bytes).
float: The default float data type in Python (8 Bytes).
complex: The default complex data type in Python (16 Bytes).
np.int8: An integer data type (1 Byte).
np.int16: An integer data type (2 Bytes).
np.int32: An integer data type (4 Bytes).
np.int64: An integer data type (8 Bytes).
np.float16: A float data type (2 Bytes).
np.float32: A float data type (4 Bytes).
np.float64: A float data type (8 Bytes).
