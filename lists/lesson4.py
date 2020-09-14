# append and extend method

# list = []
# list.append(45)
# print(list)
# list.append(787)
# print(list)

# nums = [1, 2, 3]
# nums.append(nums[:])
# print(nums)

# list1 = [2,3]
# list1.append(3)
# list1.append([1,2])
# list1.append([5,6,7,8])
# list1.append((12,13))
# print(list1)
# output - [2, 3, 3, [1, 2], [5, 6, 7, 8], (12, 13)]
'''
How can you add not one but multiple elements to a given list? Use the extend() method in Python.
'''
list = [1,2,3]
list.extend([4,5,6])
print(list)
#output [1, 2, 3, 4, 5, 6]

'''
Summary: both methods append() and extend() modify an existing list object and have no return value. 
But the former adds only a single element while the latter can add multiple elements to the list.
'''