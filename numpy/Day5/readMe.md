How does indexing and slicing work in Python?
Indexing and slicing in NumPy are very similar to indexing and slicing in Python. If you have mastered slicing in Python, understanding slicing in NumPy is easy.

Now, let’s dive into slicing in Python.
The idea of slicing is simple. You carve out a subsequence from a sequence by defining the start index and the end index. While indexing retrieves only a single character, slicing retrieves a whole substring within an index range.

For slicing, use the bracket notation with the start and end position identifiers. For example, word[i:j] returns the substring starting from index i (included) and ending in index j (excluded).

You can also skip the position identifier before or after the slicing colon. This indicates that the slice starts from the first or last position, respectively. For example, word[:i] + word[i:] returns the same string as word.

1. How to skip slicing indices (e.g. s[::2])?
   The Python interpreter assumes certain default values for s[start:stop:step]. They are: start=0, stop=len(s), and step=1 (in the slice notation: s[::]==s[0:len(s):1]).

2. When to use the single colon notation (e.g. s[:]) and when double colon notation (e.g. s[::2])?
   A single colon (e.g. s[1:2]) allows for two arguments, the start and the end index. A double colon (e.g. s[1:2:2]) allows for three arguments, the start index, the end index, and the step size. If the step size is set to the default value 1, we can use the single colon notation for brevity.

3. What does a negative step size mean (e.g. s[5:1:-1])?
   This is an interesting feature in Python. A negative step size indicates that we are not slicing from left to right, but from right to left. Hence, the start index should be larger or equal than the end index (otherwise, the resulting sequence is empty).

4. What are the default indices when using a negative step size (e.g. s[::-1])?
   In this case, the default indices are not start=0 and end=len(s) but the other way round: start=len(s)-1 and end=-1. Note that the start index is still included and the end index still excluded from the slice. Because of that, the default end index is -1 and not 0.

5. We have seen many examples for string slicing. How does list slicing work?
   Slicing works the same for all sequence types. For lists, consider the following example:

l = [1, 2, 3, 4]
print(l[2:])

# [3, 4]

Slicing of tuples works in a similar way.

6. Why is the last index excluded from the slice?
   The last index is excluded because of two reasons. The first reason is language consistency, e.g. the range function also does not include the end index. The second reason is clarity - here’s an example of why it makes sense to exclude the end index from the slice.

customer_name = 'Hubert'
k = 3 # maximal size of database entry
x = 1 # offset
db_name = customer_name[x:x+k]

Now suppose the end index would be included. In this case, the total length of the db_name substring would be k + 1 characters. This would be very counterintuitive.
