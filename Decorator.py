'''def outer(x):
    def inner ():
        print("welcome")
        x()
    return inner
def display():
    print("hello")
res= outer(display)
res()'''


'''internal working

def outer(x):
    def inner (p,q):
        p=p+5
        q=q+10
        x(p,q)
    return inner
@outer
def display(x,y):
    print(x+y)
display(10,20)'''


'''def decorator(x):
    def inner(p,q,r):
        p=p+5
        q=q+10
        r=r+15
        z=x(p,q,r)
        return z
    return inner 
@decorator
def add(a,b,c):
    return a+b+c
res=add(2,4,6)
print(res)'''

'''short  

def decorator (add):
    def inner (x,y,z):
        x=2*x
        y=3*y
        z=4*z
        add(x,y,z)
    return inner
@decorator
def add(p,q,r):
    print(p+q+r)
add(10,20,30)'''


def decorator(even_no):
    def inner (p,q,r):
        p=p-1
        even_no(p,q+1,r)
    return inner
@decorator
def even_no(start,stop,step):
    for i in range(start,stop,step):
        print(i)
s=2
e=101
sd=2
even_no(s,e,sd)

def decorator(even_no):
    def inner (p,q,r):
       print("hello")
    return inner
@decorator
def even_no(start,stop,step):
    for i in range(start,stop,step):
        print(i)
s=2
e=101
sd=2
even_no(s,e,sd)
