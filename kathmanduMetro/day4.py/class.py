# class PracticeClass:
#     bank='text'  #class variable
#     def __init__(self,name):  # it is the constructor of class
#         self.name=name
#     def sum(self,a):  #here a is local variable
#         print(a+4)

# obj=PracticeClass()
# obj.sum(4)
# obj1=PracticeClass('Ram')

# obj2=PracticeClass('hari')

class About:
    def __init__(self,name):
        self.__name=name
    def __str__(self):
        return f"{self.__name}"
    def detail(self,age,college):
        print(f"my name is {self.__name}\nage is {age}\ncollege is {college}")
    def setter(self,name):
        self.__name=name
   

obj1=About('Manish')
'''
default= name
protective=_name
private=__name

'''
# print(obj1)

obj1.__name='bye' # it cannot change because  it is private 
obj1.detail(21,"Acme college")
# everything is object
# obj1._About__name='ram'   #this process shouldn't be use to change the private variable
# name magling
# print(obj1._About__name) 

obj1.setter('Ram')  #this helps to change the value 
obj1.detail(21,"Acme")

#inheritance

# try:
#     class Employee:
        
#         def show(self):
#             print("I am employee")
#     class Salary(Employee):
#         def salary(self):
#             print("1000")
#     class Multi(Salary):
#         def nothing(self):
#             print('hey')
#     class Person(Multi):
#         def shows(self):
#             print("i am person")

# except Exception as e:
#     print('hey the error is here')
# p1=Person()
# p1.show()
# p1.salary()  
# p2=Multi()
# p2.salary() #multilevel inheritence

# hierarchical 
try: 
    class Father:
        def name(self,n):
            print(n)
    class Daughter(Father):
        def name(self,n):
            print(n)
    class Son(Father):
        def name(self,n):
            print(n)
except:
    print('error')

sonobj=Son()
sonobj.name("Joshn")