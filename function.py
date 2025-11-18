'''funtion,,,,,,


def display():
    print ("hello")
display()'''

'''def display():
    print ("hello")
print (display())'''

'''def display():
    print ("hello")
x=display()'''


'''def display():
    print ("hello")
x=display()
print(x)
print(x)
print(x)'''

'''
def display():
    return"hello"
display()'''



'''def display():
    return"hello"
print(display()) '''
    

'''def display():
    return"hello"
x=display()'''

'''def display():
    return"hello"
x=display()
print(x)
print(x)
print(x)''' 



'''positional argument############

def fun_name(x,y,z):
    print(f'{x,y,z}')
p=int(input("enter any value:"))
q=input("enter any value:")
r=input("enter any value:")
fun_name(p,q,r,)'''
    
    
'''def fun_name(x,y,z):
    print(f'{x,y,z}')
p=int(input("enter any value:"))
q=input("enter any value:")
r=input("enter any value:")
fun_name(p,q,r,10)'''

'''Default argument###########
def fun_name(x=0,y=0,z=0):
    print(f'{x,y,z}')
fun_name()
fun_name(10)
fun_name(20,10)
fun_name(10,20,30)'''

'''VAriable  length positional argument####
def fun_name(*args):
    print(args)
    print(type(args))
fun_name()
fun_name(10,20,30,40,50,60,70)'''

'''def fun_name(*args):
    print(args)
    print(type(args))
t=eval(input("Enter any tuple"))
fun_name(t)'''


'''def add_all(*n):
    sum=0
    for i in n:
        sum=sum+i
    print(f'sum is{sum}')

add_all(10,20,30,40,50)'''


'''def add_all(*n):
    sum=0
    for i in n:
        print(i)
        for j in i:
          sum=sum+j
    print(f'sum is{sum}')
var=eval(input("enter any collection:"))
add_all(var)'''


'''def add_all(*n):
    print(n)
        
var=eval(input("enter any collection:"))
add_all(var)'''

'''unpacking logic####

def add_all(*n):
    sum=0
    for i in n:
        sum=sum+i
    print(f'sum is{sum}')
var=eval(input("enter any collection:"))
add_all(var)'''


'''def display(x=0,y):
    print(f'{x,y}')

display(10,20)'''

'''def display(x,y=0,*z):
    print(f'{x,y,z}')

display(10,20,30,40,50)'''

'''keyword argument############

def fun_name(x,y,z):
    print(f'{x,y,z}')
fun_name(y=3,z=4,x=2)'''

'''def fun_name(x=0,y=0,z=0):
    print(f'{x,y,z}')
fun_name(y=10,x=20)'''

'''variable length keyword argument

def fun_name(**kwargs):
    print(kwargs)
    print(type(kwargs))
fun_name(x=10,y=20,z=30,p=2,q=3,r=5)'''

'''def fun_name(**kwargs):
    print(kwargs)
    print(type(kwargs))
var=eval(input("enter any dict"))
fun_name(**var)'''

'''def fun_name(**n):
    for k,v in n.items():
        print(f'{k}={v}')
    
var=eval(input("enter any dict"))
fun_name(**var)'''

'''with argument and with return ########
def show_detail(name):
    return name
x=input("enter your name")
result=show_detail(x)
print(result)    '''
    
'''error
def show_detail(age):
    pass
x=input("enter your age")
print(x)



def fun_name():
    return(x)
x=input("enter your name")
result=show_detail(x)
print(result)'''

'''Variable scope
x,y=10,20  
def add():
    print(x+y) 
add()'''


'''global scope
x,y=10,20
def add():
    p,q=30,40
    print(p,q)
    print(x,y)
add()
print(x,y)
print(p,q)'''


'''x,y=10,20
def add():
    x=10
    print(x)
add()
print(x)'''

'''x,y=10,20
def add():
    x=20
    print(x)
add()
print(x)'''

'''local variable ko global variable bna skte hai

x,y=10,20
def add():
    global z  
    z=20
    print(z)
add()
print(z)'''

'''sum
x=10
def add():
    x=20
    sum=globals()['x']+x
    print(sum)
add()'''

'''local--to gobal
def show():
    global x
    x=10
    print(x)
show()
print(x)'''




'''global to local
x=10
def show():
    x=20
    print(globals()['x'])
show()'''