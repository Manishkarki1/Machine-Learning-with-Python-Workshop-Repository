# String 
'''
features:
1. index
2. ordered
3. immutable

'''
# slicing in string
# string = "hey! It's me manish karki"
# for i in string:
#     print(i)

li=["college","school","university"]
# enumerate
for index,el in enumerate(li):
    print(index,el)
#slicing
myst='hey how are'
myst.replace('hey','hello')
print(myst)
print(myst.upper())
print(myst.lower())


string_split=myst.split() #it provide everything in list spliting by space
email='karki@manish411@gmail.com'
print(email.split('@',1)) #it will only split once when it sees @ so there will be 1.
print(string_split)

my_list=['str','char','int']
add_el='@'.join(my_list)
print(my_list,add_el)

# some operator in string
#repetation *
b='ho'
print(b*3)
c='yes'
print(b+c)
digit='2345'
print(digit.isdigit())

# print(c==reverse_c)
# function to print palindrome or not
# def isPalindrome(name):
#     reverse_c=name[::-1]
#     if name==reverse_c:
#         return True
#     else:
#         return False

# name=isPalindrome('radr')
# print(name)

# print('yeah it is palindrome' if name==True else name==False)
isPalindrome=lambda name:'yeah it is palindrome' if name[::-1]==name else False
print(isPalindrome('radar'))

# print(myst[7:])
# print(myst[-1::-1])
print('last 3 char is: {}'.format(myst[:-4:-1]))

# error=> the problem which can't be solved by manaually
#exception=>The problem which we can handle manually
def divide(number,divisor):
    try:
        print(number/divisor)
        # li=[1,2,43]
        # print(li[4])
    except ZeroDivisionError:
        print('exception')
    except:
        print('out of index')
    else:
        print('is execute if try bloc execute without exception')
    finally:
        print('yes, succesfully learn the exception handling')

divide(10,5)
divide(10,0)
#to give the custom exception

def exceptionraise(string):
    try:
        if not string.isdigit():
            raise "not digit"
        else:
          print(string)
    except:
        print('not digit')

exceptionraise('asdfa')

# flow-control (break continue pass)
for el in range(1,5):
    if el==3:
        break
    else:
        print(el)

# for else
for el in [1,3,5,5,7,8]:
    if el==100:
        break
    else:
        print(el)
else:
    print('Else is executed')

#question
#Wap to check prime number using for else
num = int(input("Enter a number: "))

if num > 1:
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            print(f"{num} is not a prime number")
            break
    else:
        print(f"{num} is a prime number")
        
else:
    print(f"{num} is not a prime number")