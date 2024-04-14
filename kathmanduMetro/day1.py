a =5
print(b) #undefined variables error arise

print(a)

# NAME (here capital determine constant)
name ='manish'
print(name)
namelower =name.lower()
print(namelower)
print(name.upper())
# print(name.lower)
# print(name.join('karki'))


# taking input
# number1 = int(input('Enter first number: '))
# number = int(input('Enter second number: '))
# sum =number+number1
# print(f'answer: {sum}')
    
# doc string
# ''' '''

#csb and tsb

li=[1,'manish',3.5,5,6]
#positive start from 0 index
print(li[0]);
li.insert(1,34)
print(type(li))
print(li)
li[2]='karki'
print(li)
print(li[0:3])
print(li[0::2])

#even
# li=[1,2,3,4,5,6]
# print(li[1::2])
# even=[]
# odd=[]
# for i in li:
#     if i%2==0:
#         even.append(i)
#     else:
#         odd.append(i)
# print(even)
# print(odd)
# popdeleting=li.pop()
# print(popdeleting)
# print(li)
# removeprac=li.remove(2)
# print(li)

# we have to give comma to make single value tuple

li =(1,)
li1 = (1)
print(type(li))
print(type(li1))

# pass should be use in empty print if/else
# tuple_practice=(2,4,6)
# tuple_practice[0]=4
# print(tuple_practice)
# li=[1,2,3,40,20,10]
#python use trim short
# print(li.sort())
# li2=sorted(li)
# print(li2)

# li[0]=5
# print(li)
# tuple=(1,2,3)
# tuple[0]=5
# print(tuple)

# set
set_practice={2,34,5,67,76,67}
print(set_practice)
set_practice.discard(34)
print(set_practice)
set_practice1={2,3,4,5,67}
set_inter=set_practice.intersection(set_practice1)
print(set_inter)


# Batch learning
# online learning

# exception handling
try: 
    a=21
    print(b)
    print(a/0)


except NameError as exe:
    print(exe)
except Exception as exe:
    print('oops! something went wrong')
except:
    print("Error occurs")
finally:
    print("finally again you are here")
print('hey my dear')
