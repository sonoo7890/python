'''def data():
    for i in range(1,1000):
        yield i 
x=data()
print(x)'''

'''def data():
    for i in range(1,10):
        yield i 
x=data()
for i in x:
    print (i)'''

'''def data():
    for i in range(1,10):
        yield i 
x=data()
print(next(x))
print(next(x))
print("hello")'''

'''def data():
    for i in range(1,10):
        yield i 
x=data()
print(next(x))
print(next(x))
print("hello")
print(next(x))
for i in x:
    print(i)'''


'''x=range(1,10)
for i in range(1,10):
    if 1==1 or i==2 or i==3:
        print(i)
for i in range(1,10):
    print(i)'''

'''iterator#########

l=[1,2,3,4,5,'python']
l1=iter(l)
#print(l1)
print(next(l1))'''

res=map()
print(list(res))