"""
The list.copy() method copies all list elements into a new list. The new list is 
the return value of the method.
"""
# lst = [2,4,6,7,8,9,3]
# print(lst.copy()) #[2, 4, 6, 7, 8, 9, 3]

"""
Python List Copy Shallow

In object-oriented languages such as Python, everything is an object. The list is an object 
and the elements in the list are objects, too. A shallow copy of the list creates a new list 
object—the copy—but it doesn’t create new list elements but simply copies the references to these objects.
"""

# lst_1 = [7,9, [2,4,6,8], "Ronny"]
# lst_2 = lst_1.copy()
# lst_2[2].append(34)
# print(lst_2) # [7, 9, [2, 4, 6, 8, 34], 'Ronny']
# print(lst_1) # [7, 9, [2, 4, 6, 8, 34], 'Ronny']

"""
Python List Copy Deep

Having understood the concept of a shallow copy, it’s now easy to understand the concept of a deep copy.
 
    A shallow copy only copies the references of the list elements.
    A deep copy copies the list elements themselves which can lead to a highly recursive behavior because 
    the list elements may be lists themselves that need to be copied deeply and so on.
"""

import copy
lst = [3, 5, [8, 9], "Nijimbere"]
lst_2 = copy.deepcopy(lst)
lst_2[2].append(89)
print(lst[2]) #[8, 9]
print(lst_2) # [3, 5, [8, 9, 89], 'Nijimbere']