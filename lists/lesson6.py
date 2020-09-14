#The list.insert(i, element) method adds an element element to an existing list at position i. 
#All elements j>i will be moved by one index position to the right.

list1 = [1,2,3,4,5,6,7,8,9]
list1.insert(5, 78)
print(list1)
#output: [1, 2, 3, 4, 5, 78, 6, 7, 8, 9]

list2 = ["ronny", "ade", "shoes", "muzi", "smanga"]
list2.insert(-2, "kelly")
print(list2)
#output: ['ronny', 'ade', 'shoes', 'kelly', 'muzi', 'smanga']

'''
Python List insert() Complexity

Time Complexity: The insert() method has constant time complexity O(1) no matter the number of elements in the list. 
The reason is that Python lists are implemented with variable-length array lists so accessing a certain position is fast. 
Also inserting an element into the array list is fast because you only have to modify the pointers of the preceding and 
following elements in the list.
'''