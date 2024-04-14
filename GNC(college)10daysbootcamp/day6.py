'''
file handling=> create
                write  
                update
                delete
'''
'''
different mode in file operation
r= read mode
w= write mode
a= append mode
r+= read write mode
w+= write read mode
'b'= binary
't'= text 
'''
# file=open('name.txt','r') 
# content=file.read()
# print(content)
# file.close()

# context manager
# with open('name.txt','r') as f:
#     content=f.read()
#     print(content)

# with open('name.txt','a') as f:
#     f.write(' we are excited')
with open('name.txt','r+') as f:
    # content=f.read()
    # f.write(content+'hey my dear!are you alright?')
    # print(content)
    content=f.readline()
    print(content)
    allcontent=f.readlines()
    print(allcontent)
    f.seek(20)  
    f.write('after 20') #it will write after 20 index
    print(f.tell())
   
#    Namespace in python
    # it solve variable conflict

# recursion
def fact(num):
    if num==1:
        return 1
    else:
        return num*fact(num-1)
factorial1=int(input('Enter the number: '))
factorial=fact(factorial1)
print(factorial)

# fibonacci series
li=[1,5,6,8]

# def fibonacci(nterm):
#     if nterm==0 or nterm==1:
#         print('give other 1 or 0')
#     else:
#         for i in range(1,nterm):
#             li.append(li[-1]+li[-2])



# fibonacci(4)
# print(li)
def fibonacci(nth):
    if nth==1:
        return 1
    else:
        return fibonacci(nth)+fibonacci()

number=int(input('Enter the number: '))

for i in range(1,number):
   result= fibonacci(i)
   print(result)

