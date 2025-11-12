'''map

x=lambda paramerters: expression
x(arguments)
p=lambda x,y: print(x+y)
p(4,5)
print(p(3,4))'''

'''p= lambda x,y:print(x+y)
z=p(4,5)'''



'''p= lambda x,y:print(x+y)
z=p(4,5)
print (z)
print(z)'''


''' lambda to square 
l=[1,2,3,4,5]
result=(list(map(lambda n: n*n,l)))
print(result)'''


'''l1=[1,2,3]
l2=[2,4,5]
l3=[0,4,5]
result=(list(map(lambda x,y,z: x+y+z,l1,l2,l3)))
print(result)'''

'''lambda filter(if-else) 

l=[1,2,3,4,5,6,7,8]
print(list(filter(lambda n:n if n%2==0 else None,l)))'''

'''l=[1,2,3,4,5,6,7,8]
print(list(map(lambda n:'even'if n%2==0 else 'odd',l)))'''

'''import functools
l=[1,2,3,4,5]
print(functools.reduce(lambda x,y:x+y,l))'''

'''import functools
l=[1,2,3,4,5]
print(functools.reduce(lambda x,y:x if x>y else y,l))'''