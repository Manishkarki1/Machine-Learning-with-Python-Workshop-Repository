city=['ktm','pokhara','dhangadi','butwal']
population=[1000,9000,2000,300]
list1=[]
for index,el in enumerate(city):
    print(f"{el}:{population[index]}")

for el in zip(city,population):
    list1.append(el)
print(list1)
for key,value in list1:
       print(f"{key}:{value}")

newlist=list(zip(city,population))
newdict=dict(zip(city,population))
print(newlist)
print(newdict)