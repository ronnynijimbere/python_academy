"""
Definition and Usage: The list.sort() method sorts the list elements in place in an ascending manner. 
To customize the default sorting behavior, use the optional key argument by passing a function that 
returns a comparable value for each element in the list. With the optional Boolean reverse 
argument, you can switch from ascending (reverse=False) to descending order (reverse=True). 
"""

# lst = [22,2,4,6,87,33,66,4,45]
# lst.sort()
# print(lst) #[2, 4, 4, 6, 22, 33, 45, 66, 87]

# #sort the list (leading number)
# lst.sort(key=lambda x: str(x) [0])
# print(lst) #[2, 22, 33, 4, 4, 45, 6, 66, 87]

# #sort descending
# lst.sort(reverse=True)
# print(lst) #[87, 66, 45, 33, 22, 6, 4, 4, 2]

'''
The list.sort() method takes another function as an optional key argument that allows you to modify 
the default sorting behavior.

The key function is then called on each list element and returns another value based on which the sorting 
is done. Hence, the key function takes one input argument (a list element) and returns one output value 
(a value that can be compared).
'''

lst1 = [(1,2), (3,2), (3,3), (1,0), 
(0,1), (4,2), (1,1), (0,2), (0,0)]
lst1.sort()
print(lst1) # [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (3, 2), (3, 3), (4, 2)]

lst1.sort(key=lambda x: x[0])
print(lst1) # [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (3, 2), (3, 3), (4, 2)]

lst1.sort(key=lambda x: x[1])
print(lst1) # [(0, 0), (1, 0), (0, 1), (1, 1), (0, 2), (1, 2), (3, 2), (4, 2), (3, 3)]

'''
You can see that in the first two examples, the list is sorted according to the first tuple value first. 
In the third example, the list is sorted according to the second tuple value first.

You achieve this by defining a key function key=lambda x: x[1] that takes one list element x (a tuple)
 as an argument and transforms it into a comparable value x[1] (the second tuple value).
'''
