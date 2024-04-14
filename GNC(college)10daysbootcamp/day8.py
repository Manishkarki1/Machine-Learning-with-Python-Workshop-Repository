'''
accessibility
visibility=> public 
             private(__)
             protected(_)

'''
class BankAccount:
    def __init__(self,name,account,balance):
        self.name=name, #public
        self._account=account,  #protected
        self.__balance=balance  #private
    def info(self): #public method
        print(f"name is {self.name}, account is {self._account}")
    def __getBalance(self): #private method
        print(self.__balance)
    def _getAccount(self):  #protected method
        print(self._account)
b1=BankAccount('A',123,1000)
b1.info()
b1._getAccount()   
# b1.__getBalance()  #lead to attribute error

'''
Types of method
1. instance method
2. class method
3. static method

'''
class A:
    college='GNC'
    @classmethod
    def __init__(cls,name):
        cls.name=name
        # print(cls.college)
    @classmethod     #it helps to represent the class(cls)
    def getCollege(cls,*args,**kwargs):
        print(cls)
        print(cls.college)
    @staticmethod
    def get_random():
        print('static method')
obj1=A('bhupendra')

obj1.getCollege()
A.getCollege()
obj1.get_random()

'''
polymorphism
 1.overloading  =>it runs in runtime (same function name but argument different)
    a) function overloading
    def add(a,b):
       pass
    def add(a,b,c):
       pass
    b) operator overloading
        a='abc'
        b='cde'
        print(a+b)
        c=[1,2]
        d=[3,4]
        print(c+d)
        e=1
        f=2
        print(e+f)
 2.overriding   => child and parent both have same method name
        it is a ability to child class to override the parent's method


'''
# class Cat:
#     def speak(self):
#         print('meow')
# class Dog(Cat):
#     def speak(self):
#         print('bark')
#         super().speak()

       
# dog1=Dog()
# result=dog1.speak()
# print(result)


'''
MRO 
=> method,resolution, order
'''
# class Cat:
#     def space(self):
#         print('meow')
# class Cow:
#     def speak(self):
#         print('cow')
#     def new_cow(self):
#         print('new cow')
# class Dog(Cat,Cow):
#     # def __str__(self):
#     #     pass
#     def speak(self):
#         print('dog')
#         super().speak()
# dog=Dog()
# print(Dog.__mro__)   #it shows how the MRO is use
# dog.speak()
# print(dog)

#python doesn't support abstract in default so we have to import it from abc module
from abc import ABC,abstractmethod
class ImplementAbstract(ABC):
    @abstractmethod
    def implement_sum(self):
        pass
class Random(ImplementAbstract):
    # pass
    def implement_sum(self):

        print('sum all')
obj=Random()
obj.implement_sum()