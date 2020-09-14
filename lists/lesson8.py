"""
The list.index(value) method returns the index of the value argument in the list. 
You can use optional start and stop arguments to limit the index range where to search for the value in the list.
If the value is not in the list, the method throws a ValueError. 
"""

# lst = ["Ronny", 26, "Mike", 126, "Kelly",55]
# # lst.index("Mike") # 2
# # lst.index(55) # 5
# lst.index(26,68,25) 

# def index(value, lst):
#     for i, el in enumerate(lst):
#         if el==value:
#             return i
#     raise Exception('ValueError')

# print(index(42, [1, 2, 42, 99])) #output 2

# print(index("Ronny", [1, 2, 3])) # ValueError

"""
The index() method has linear runtime complexity in the number of list elements. For n elements, 
the runtime complexity is O(n) because, in the worst case, you need to iterate over each element 
in the list to find that the element does not appear in it.
"""

# Create a list of customers
c = ['Ronny', 'Sam', 'Simon', 'Adela']

# Extract all names of customers starting with 'A'
indices_of_A = [c.index(x) for x in c if x[0] == 'A']

# Print the resulting customers
print(list(c[i] for i in indices_of_A)) #out ['Adela']