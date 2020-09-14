"""
Specification: The list.count(x) method counts the number of occurrences of the element x in the list.
"""

lst = [2,5,4,2,6,3,5,4,2,6,3,2]
print(lst.count(2)) #output: 4

"""
Return value: The method list.count(value) returns an integer value set to the number of times the argument 
value appears in the list. If the value does not appear in the list, the return value is 0. 
"""

"""
To summarize, the list.count(value) method counts the number of times a list element is equal to value 
(using the == comparison). Here’s a reference implementation:
"""

def count(lst, value):
    ''' Returns the number of times
    a list element is equal to value'''

    count = 0
    for element in lst:
        count += element == value

    return count


lst = [1, 1, 1, 1, 2]

print(lst.count(1))
# 4

print(lst.count(2))
# 1

print(lst.count(3))
# 0
