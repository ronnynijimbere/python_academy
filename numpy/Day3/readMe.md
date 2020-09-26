We will dive deeper into NumPy arrays learning about their shape and axis properties.
NumPy does not simply store a bunch of data values in a loose fashion (you can use lists for that).
Instead, NumPy imposes a strict ordering to the data – it creates fixed-sized axes.
Don’t confuse an axis with a dimension. A point in 3D space, e.g. [1, 2, 3] has three dimensions but only a single axis.

So what is an axis in NumPy?

Think of it as the depth of your nested data. If you want to know the number of axes in NumPy, count the number of opening brackets '[' until you reach the first numerical value.

The shape gives you not only the number of axes but also the number of elements in each axis (the dimensionality).

The shape property gives you three pieces of information about each array.

First, it shows you the number of axes per array – that is – the length of the tuple. Array a has one axis, array b has two axes, and array c has three axes.

Second, it shows you the length of each axis as the numerical value. For example array a has one axis with three elements.

Hence, the shape of the array is (3, ). Don’t get confused by this weird tuple notation. The reason why the NumPy shape operation does not return a tuple with a single element (3) is: Python converts it to a numerical value 3. This has the following benefit: If you access the first element of your shape object a.shape[0], the interpreter does not throw an exception this way.

Third, it shows you the ordering of the axes. Consider array c. It has three tuple values (2, 3, 2).

Which tuple value is for which axis?

    The first tuple value is the number of elements in the first level of nested lists. In other words: how many elements are in the outermost list? The outermost list for c is [X1, X2] where X1 and X2 are nested lists themselves. Hence, the first axis consists of two elements.
    But what’s the number of elements for the second axis? Let’s check the axis X1. It has the shape X1 = [Y1, Y2, Y3] where Y1, Y2, and Y3 are lists themselves. As there are three such elements, the result is 3 for the second tuple value.
    Finally, you check the innermost axis Y1. It consists of two elements [1, 2], so there are two elements for the third axis.

In summary, the axes are ordered from the outermost to the innermost nesting level. The number of axes is stored in the ndim property. The shape property shows you the number of elements in each axis.
