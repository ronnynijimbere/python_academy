'''
list methods
    lst.append(x) - Appends element x to the list lst.
    lst.clear() - Removes all elements from the list–which becomes empty.
    lst.copy() - Returns a copy of the list. Copies only the list, not the elements in the list (shallow copy).
    lst.count(x) - Counts the number of occurrences of element x in the list.
    lst.extend(iter) - Adds all elements of an iterable iter (e.g. another list) to the list.
    lst.index(x) - Returns the position (index) of the first occurrence of value x in the list.
    lst.insert(i, x) - Inserts element x at position (index) i in the list.
    lst.pop() - Removes and returns the final element of the list.
    lst.remove(x) - Removes and returns the first occurrence of element x in the list.
    lst.reverse() - Reverses the order of elements in the list.
    lst.sort() - Sorts the elements in the list in ascending order.
'''

list = []
list.append(2)

list.copy()
list.count(2)
list.extend([2,5,7,9,8,4])

list.index(4)
list.insert(5, 1000)
list.pop()
list.reverse()
list.sort()
print(list)