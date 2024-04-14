# list
li=[1,'manish',3.5]
#positive start from 0 index
print(li[0]);
#indexing, -ve indexing
#negative start from -1 index
print(li[-2]);
li=[1,'manish',3.5,'how',[2,5]]
print(li[-1])
length=len(li)
print(li[length-1])
print(li[length-1][1])

# slicing
":"
'''
inclusively:exclusive
starting:ending
'''
new_list=[1,2,4,5,7,3]
three_list=new_list[0:3]
last_list=new_list[3:]
print(last_list)

"[starting:endpoint:step]"
print('step after 2: ',new_list[2:6:2])
print(new_list[::])


# when step is negative
print('step after 2 through negative: ',new_list[-1:-5:-2])
# Program to reverse the list using slicing

print(new_list[-1::-1])
print(new_list[::-1])
# even number in decensding order
listing=[1,2,3,4,5,6,7,8,9,10]
print(listing[::-2])

#method in list
#append 
listing.append(2)
print(listing)
popelement=listing.pop()
print(popelement)
question=[3,4,5]
question[1]=8
print(f'changing list:{question}')
question.remove(8)
print(f'after remove:{question}')
# removeelement=listing.remove(9)
# extend

to_add=[11,12,13]
extendlist=listing.extend([23,32])
print(extendlist)

#tuple and list
# tuple is immutable(can't change), it consume less storage
#list is mutable(can change)
# tuple_practice=(2,3,5)
# tuple_practice[0]=4
# print(tuple_practice)

#dictionary is the key:value pair 
dictionary_practice={
    'name':'manish',
    'class':'BCA'
}
#nested dictionary
example={
    'name':'manish',
    'school':{
        'name':'greenfield'

    }
}
print(dictionary_practice['name'])
print(dictionary_practice)
print(example['school']['name'])