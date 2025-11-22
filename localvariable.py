'''class student:
    def __init__(self):
        x=10
        print(x)
    def new(self):
        y=10
        print(y)
        print(x)
obj=student()
#obj.new()'''

class book:
    price =100
    def __init__(self,title,total_page):
        self.t=title
        self.tp=total_page
    @classmethod
    def update_price(cls,p):
        cls.price=p
obj=book('python',500)
print(obj.t,obj.tp,book.price)
x=float(input("enter updated price:"))
obj.update_price(x)
obj1=book('python',510)
print(obj.t,obj.tp,book.price )
