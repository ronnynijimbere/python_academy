Here's a quick summary:

    The axis is the depth of your nested data. If you want to know the number of axes, count the number of opening brackets '[' until you reach the first numerical value.
    The shape gives you not only the number of axes but also the number of elements in each axis (the dimensionality).

How to create and initialize numpy arrays?
There are many ways to create and initialize NumPy arrays. The easiest way to create one is via the function np.array(s). You simply put in a sequence s of homogeneous numerical values and voilà – you get your NumPy array.

But how can you create multi-dimensional arrays?
Simply pass a sequence of sequences as arguments to create a two-dimensional array. Pass a sequence of sequences of sequences to create a three-dimensional array and so on.

Having at least one floating type element, the whole array is converted to a floating type array. The reason is that NumPy arrays have homogeneously typed data. Here is an example of such a situation:

import numpy as np
s
a = np.array([[1, 2, 3.0], [4, 5, 6]])
print(a)

# [[1. 2. 3.]

# [4. 5. 6.]]

Now, let’s move on to more automated ways to create NumPy arrays. For the toy examples given above, you can simply type in the whole array. But what if you want to create huge arrays with thousands of values?

You can use NumPy’s array creation routines called ones(shape) and zeros(shape).
