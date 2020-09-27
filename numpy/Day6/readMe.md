How does indexing and slicing work in Numpy?
When using the NumPy library, you have to differentiate between one-dimensional arrays and multi-dimensional arrays because slicing works differently for both.

Let’s move on to multi-dimensional slices.

For multi-dimensional slices, you can use one-dimensional slicing for each axis separately. You define the slices for each axis, separated by a comma.

The most important information to remember is that you can slice each axis separately. If you don’t specify the slice notation for a specific axis, the interpreter applies the default slicing (i.e., the colon :).

I will skip a detailed explanation of the NumPy dot notation …- just note that you can “fill in” the remaining default slicing colons by using three dots.

Here is an example
import numpy as np

a = np.arange(3\*\*3)
a = a.reshape((3,3,3))
print(a)
##[[[ 0 1 2]

## [ 3 4 5]

## [ 6 7 8]]

##

## [[ 9 10 11]

## [12 13 14]

## [15 16 17]]

##

## [[18 19 20]

## [21 22 23]

## [24 25 26]]]

print(a[0, ..., 0])

# Select the first element of axis 0

# and the first element of axis 2.

# Keep the rest.

# [0 3 6]

# Equal to a[0, :, 0]

Having mentioned this detail, I will introduce a very important and beautiful feature for NumPy indexing. This is critical for your success so stay with me for a moment.

Instead of defining the slice to carve out a sequence of elements from an axis, you can select an arbitrary combination of elements from the NumPy array.

How? Simply specify a boolean array with exactly the same shape.

If the boolean value at position (i,j) is True, the element will be selected, otherwise not. As simple as that.

Here is an example:
import numpy as np

a = np.arange(9)
a = a.reshape((3,3))
print(a)

# [[0 1 2]

# [3 4 5]

# [6 7 8]]

b = np.array(
[[ True, False, False],
[ False, True, False],
[ False, False, True]])
print(a[b])

# Flattened array with selected

# values from a

# [0 4 8]

The matrix b with shape (3,3) is a parameter of a’s indexing scheme. Beautiful, isn’t it?

Let me highlight an important detail. In the example, you select an arbitrary number of elements from different axes. How is the Python interpreter supposed to decide about the final shape?

For example, you may select four rows for column 0 but only 2 rows for column 1 – what’s the shape here? There is only one solution: the result of this operation has to be a one-dimensional NumPy array.

If you need to have a different shape, feel free to use the reshape() operation to bring your array back into your preferred format.
