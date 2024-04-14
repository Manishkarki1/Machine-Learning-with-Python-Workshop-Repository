class Student:
    def __init__(self,name,age): #special fucntion started and end with __
       self.name=name,
       self.age=age
    
    
    def getMarks(self,marks): #method
      return  f'marks is {marks}'

obj1=Student('manish',23) #object creation

print(obj1.name)
print(obj1.getMarks(23))
# print(obj2.getMarks(43))

'''
constructor 
    1.parameterized 
        def __init__(self,name,age):
           self.name=name,
           self.age=age
    2. non parameterized
        def __init__(self):
           pass
'''

# inheretance
'''
    types of inheritance
    1. single
    2. multiple
    3. multilevel
    4. hierarchical level
    5. hybrid level
'''

#parent class
class Animal:
   def do_speak(self):
      print('meow')

# child class
class Cat(Animal):
   def can_sleep(self):
      print('sleep call')
class CatTypes(Cat):
   def cat_types(self):
      print('white')
c1=Cat()
c1.can_sleep()
c1.do_speak()
c2=CatTypes()
c2.cat_types()
