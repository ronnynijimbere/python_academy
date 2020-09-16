# Day 1
# x = 50 // 11
# print(x)
# output 4

#Day 2
# print(3 * 'un' + 'ium')
#output: unununium

# Day 3
# x = 'silent'
# print(x[2] + x[1] + x[0] + x[5] + x[3] + x[4])
#output : listen

# Day 4
# python = ['cool']
# x = python in python
# y = 'cool' in python
# print(x)
# print(y)
#output for x: False
#output for y: True

# Day 5
# s = 'terfinx'
# s = ''.join(sorted(list(s)[3:7])+list(s)[0:3])

# print(s) #finxter

# Day 6
# x = 'cool'
# print(x[-1] + x[-2] + x[-4] + x[-3]) #output: loco

# Day 7
# l = [[]]

# if l:
#     print(True)
# else:
#     print(False)
#output: True

# Day 8
# x = 5 // -3.0 * 4
# print(x) # output -8.0

# # Day 9
# words = ['ape', 'banana', 'cat', 'bird']
# b_words = [w for w in words if w.startswith('b')]
# print(len(b_words)) # output: 2

# Day 10
# Logic Statements
A = True # Temperatures are high
B = True # Artic ice is melting
C = True # Sea Levels are rising
D = False # All regions become hot

def follows(A, B):
    """ Returns True if 'A -> B'
    in words: 'B follows from A' """
    return not A or B

# Do We have climate change
climate_change = follows(follows(A, B), C)
if not D:
    print(climate_change)
else:
    print(D)
#output: True