from calculation import calculate as calculator
from calculation import fun1
'''
way of importing module
1. import module_name 
2. from module_name import fun1,class
3. from module_name import * 

'''

number_1 = int(input('Enter the number'))
number_2 = int(input('Enter the second number'))
operator=input('Enter the operator: ')

result=calculator(number_1,number_2,operator)
print(f'The result is {result}')

fun1(1,2,4,5,name='Ram',address='kathmandu')

