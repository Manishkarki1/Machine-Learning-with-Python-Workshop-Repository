# *args = packing
#  
# def add(*args):
#     print(args)
# add(3,4,6)

# Wap n which accept positional arguments, return sum of n elment

# def sum(*args):
#     total = 0
#     for i in args:
#         total += i
#     return total
# result = sum(3,5,6)
# print(result)

# keyword arguments
# it always return dictionary
def greet(**kwargs):
    for key,value in kwargs.items():
        print(key,value,sep=':')
greet(name='manish', lastname='karki')

# remember in default parameter
# default always should be in last(that is after the postional argument)

def add(b,a=3):
    pass

# lambda function
# syntax -> lamda arg:expression

sum=lambda *args: args
print(sum(2,4,5,6))

# higher order function
# map, filter
list = [1,3,4,5,7]
square_list=[]
for i in list:
   square_list.append(i*i)
print(square_list)

map_square=[]
# map
# for i in list:

#     map({
#     map_square.append(i*i)
#     },list)
# print(map_square)

el=[2,5,6,3,4]
# def cube(e):
#     return e*e*e

square=lambda i:i*i
for i in el:
    print(square(i))

# short
cube=set(map(lambda e:e*e*e,el))
print(cube)
# filter
def even(e):
    if e%2==0:
        return e
    
filter_result=set(filter(even,el))
print(filter_result)

even=set(filter(lambda e:e%2==0,el))
odd=set(filter(lambda e:not(e%2==0),el))
print(odd)

# list comprehension
# comprehension is used because it is memory effiency
list_compre=[23,4,5,8]
new_list=[el * el for el in list_compre]
print(new_list)
# [elname loop condition]
odd=[e for e in list_compre if not(e%2==0)]
print(odd)
# dictionary comprehension
element =[1,2,4,3] 
# syntax {key:value for loop}
new_dict ={el:el*el for el in element}
print(new_dict)
#decision making
gender='male'
if gender=='male':
    print('he is male')
else:
    print('she is female')

# ternary 
print('he is male' if gender=='male' else gender=='female')
