'''map #######
l=(1,2,3,4,5)
def square(n):
    return n*n
result=map(square,l)
print(result)
print(tuple(result))'''

'''map (fun_name,collection1,collection2, collection3)

l1=[1,3,5,7]
l2=[1,2,3]
l3=[1,2,3,4,5,6,7]
def add (x,y,z):
    return x+y+z
result=list(map(add,l1,l2,l3))
print(result)'''

'''filter ###
l=[1,2,3,4,5,6]
def even(n):
    if n%2==0:
        return n
result=filter(even ,l)
print(result)
print(list(result))'''

'''filter #####
l=[2,3,4,5,6,7]
def evenodd(n):
    if n%2==0:
        return 'even'
    else:
        return 'odd'
result=list(map(evenodd,l))
print(result)  '''
 

'''sum
import functools
l=[1,2,3,4,5,6]
def add (x,y):
    return x+y
result= functools.reduce (add,l)
print(result)'''

'''max number
from functools import reduce
l=[10,2,5,20,6,9]
def max (x,y):
    if x>y:
        return x
    else:
        return y
result=reduce(max , l)
print(result)'''


'''from functools import reduce
l=[10,2,5,20,6,9]
def min (x,y):
    if x<y:
        return x
    else:
        return y
result=reduce(min/'' , l)
print(result)'''