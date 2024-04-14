#printing statement with end parameter
#everything in python is object
print('hello  namaste',end=',',)
print('hey')
#printing statement with sep parameter
content='learning python'
tutor='BCA Student'
print(content,tutor,sep='-',)
fruit1='apple'
fruit2='orange'
fruit3='banana'
print("My favorite fruits are "+fruit1,fruit2,fruit3,sep=',')

# String format
day="sunday"
date=2081

print("our new year is in {}. we are moving to {}".format(day,date))
#f string 
# a=f'my name is {'manish'}'
print(f"our new year is in {day}. we are moving to {date}")

# print(a)
# doc formatting
#multiline comment

def sum(a,b):
    print(a+b)

    '''
    This is the function for the sum of two number 
    so here i have passed the two number 3 and 4
    '''
sum(3,4)
# variable naming convention
# container
# letter
first_name='jpt'

print(first_name)
first_name=2000

print(type(first_name))
