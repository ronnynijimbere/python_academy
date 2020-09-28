import numpy as np 

a = np.array([[1,2], [1,1], [0,0]])
print(a.shape) #(3,2)
print(a.ndim) #2
print(np.average(a)) #0.8333333333333334


b = np.array([[1,2,3], [1,1,1]])
print(np.matmul(a,b))
print(np.var(b)) # 0.5833333333333334
'''
[[3 4 5]
 [2 3 4]
 [0 0 0]]
'''

c = np.arange(20)
print(c) #[ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19]

d = np.linspace(-10, 10, 22, endpoint=False)
print(d)
'''
[-10.          -9.09090909  -8.18181818  -7.27272727  -6.36363636
  -5.45454545  -4.54545455  -3.63636364  -2.72727273  -1.81818182
  -0.90909091   0.           0.90909091   1.81818182   2.72727273
   3.63636364   4.54545455   5.45454545   6.36363636   7.27272727
   8.18181818   9.09090909]
'''

value = np.array([2000, 3000, 750, 3697])
customers = np.array(["Ronny", "Steven", "Rose", "Tracy"])
print(customers[np.argsort(value)])
#['Rose' 'Ronny' 'Steven' 'Tracy']