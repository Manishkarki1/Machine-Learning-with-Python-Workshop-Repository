academic  = {
    "name":"manish",
    "school":"GNC"
    }
# deleting the key,value
# del academic['name']
print(academic)
#clearing the dictionary
# academic.clear()
print(academic)
# get method
result  = academic.get('name',None)
print(result)
profession  = {
    'professionname':'developer'

    }
academic.update(profession)
print(academic)
key =academic.keys()
print(key)
# items give tuple 
print(academic.items())

for i in key:
    print(academic[i])

# unpacking
a,b,c =(2,3,4)
print(a,b,c)

for key,value in academic.items():
    print('key is {} and value is {}'.format(key,value))
# in operator-> membership test

my_dictionary ={
    'name':'saroj',
    'age':23

    
    }
new_dict  ={**my_dictionary,**academic}
print(new_dict)
# set-> it doesn't allow dublicate value, unordered(we can't do work in indexed),
set1  ={'value',True,True,'val',False,0}
set2 ={1,23,4,'hey'}
print(set1)
set1.add('hey')
# set1.remove('hey')
result =set1.intersection(set2)
print(result)
# truthy and falsy value
# truthy value =1,true,{33}
#falsy value =none,0,false
a  = False
if a:
    print('falsy value')
else:
    print('truthy value')

'''
important question
set,list
list vs tuple
why tuple prefered over list
dictionary,
extend vs append
mutable vs immutable
'''
list =[1,2,43,5,5]
unique =[]
print(unique)
#loop
for i in list:
    if i in unique:
        pass
    else:
        unique.append(i)
print(unique)
# not operator
for i in list:
    if i not in unique:
        unique.append(i)
print(unique)

divisible=[]
for i in range(1,6):
    if 5%i==0:
        divisible.append(i)
print(divisible)

for i in range(0,10,5):
    print(i)

# def hey():
#     print('Are you looking for me?\n yeah i am here.')
# hey()
def about(a,b=5):
    # print(name)
    sum=a+b
    return sum

result=about(5)
print(result)
# range()
