'''
You'll learn about three extremely important methods:
 

    list.remove(element)
    list.pop(index)
    list.clear()
'''

'''
The list.remove(element) method removes the first occurrence of the element from an existing list. 
It does not, however, remove all occurrences of the element in the list!
'''
# list1 = [2,4,9,8,7,9,12]
# list1.remove(9)
# print(list1)
#output: [2, 4, 8, 7, 9, 12]

'''
Removing an element from a list has linear runtime complexity (the growth of the runtime is restricted by a linear 
function O(n) for n elements). The reason is that you have to check all elements in the list 
if the searched element doesn't exist in the list. For n elements, you have n comparisons.

    If the list has 1000 elements, you need 1000 comparisons.
    If it has 2000 elements, you'll need 2000 comparisons and so on.
'''

'''
The list.pop() method removes and returns the last element from an existing list. The list.pop(index) 
method with the optional argument index removes and returns the element at the position index. 
'''

# list2 = [2,4,6,7,8,9,12]
# list2.pop()
# print(list2)
#output: [2, 4, 6, 7, 8, 9]

'''
The time complexity of the pop() method is constant O(1). No matter how many elements are in the list, 
popping an element from a list takes the same time (plus or minus constant factors).

The reason is that lists are implemented with arrays in cPython. Retrieving an element from an array 
has constant complexity. Removing the element from the array also has constant complexity. 
Thus, retrieving and removing the element as done by the pop() method has constant runtime complexity too.
'''


'''
The list.clear() method removes all elements from an existing list. The list becomes empty again.
'''
# list3 = [5,7,9,8,7,8,6]
# list3.clear()
# print(list3)
#output: []
#The runtime complexity of list.clear() is O(n) for a list with n elements.

'''
del — Remove Elements by Index or Slice
'''

# list4 = [2,6,7,9,8,2,1,4]
# del list4[2]
# del list4[-1] #output [2, 6, 9, 8, 2, 1]
# del list4[::2] # output [6, 8, 1]
# print(list4)
#output: [2, 6, 9, 8, 2, 1, 4]

list1 = list(range(20))

#output [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
# del list1[6]
# del list1[:7]
# print(list1)
lst = list(range(10))
lst_new = [x for x in lst if x%2==1]
print(lst_new)
#output [1, 3, 5, 7, 9]