'''class web:
    def __init__(self,name):
        self.n=name
    def great():
        print("welcome to my web page")
obj=web
obj.great()'''
    
'''error aayega self update ho jaiga'''
class web:
    def __init__(self,name):
        self.n=name
    @staticmethod
    def great():
        print("welcome to my web page")
obj=web('ecomm')
obj.great()
    