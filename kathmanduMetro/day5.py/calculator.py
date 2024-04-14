class Calculator:
    
    def __init__(self,a,b):
        self.a = a 
        self.b = b
    def add(self):
        try:
            print(f"sum is {self.a+self.b}")
        except Exception as exe:
            print(exe)
    def sub(self):
        try:
            print(f"difference is {self.a-self.b}")
        except Exception as exe:
            print("please")
    def mul(self):
        try:
            print(f"product is {self.a*self.b}")
        except Exception as exe:
            print(exe)
    def div(self):
        try:
            print(f"quotient is {self.a/self.b}")
        except Exception as exe:
            print(exe)     

def getValue(show):
    try:
        return int(input(show))
    except Exception as exe:
        print(f'${exe}')
        return getValue(show)
num1=getValue("Enter the first number:") 
num2=getValue("Enter the second:")     
op=input("Enter the operator:")
obj=Calculator(num1,num2)
# match case is same to switch case
match op:
    case '+':
        obj.add()
    case '-':
        obj.sub()
    case '*':
        obj.mul()
    case '/':
        obj.div()

    
