import pandas as pd 
import seaborn as sbn

data=pd.read_csv('fortune.csv') #it is the way to open or read the csv data 
d1=sbn.load_dataset('iris')
print(d1)
# slicing 
# loc doesn't support -1 indexing
x=d1.loc[0:,"sepal_length":"petal_width"]
print(x)
# iloc support indexing of -1 too
y=d1.iloc[0:,-1:]

print(y)
# merge
li={"city":["kathmandu","pokhara","birgunj"],"temperature":[5,10,50]}
data1=pd.DataFrame(li)
print(data1)
l2={"city":["kathmandu","dharan","biratnagar"],"temperature":[9,1,5]}
data2=pd.DataFrame(l2) #it will provide the 2d table
print(data2)

print("merge data: ")
mergeData=pd.merge(data1,data2)
print(mergeData) # it will only give the inner(intersection) data

mergeData1=pd.merge(data1,data2,how="outer") #we have how attribute to give the condition
print(mergeData1) # it will only give the outer data
mergeData2=pd.merge(data1,data2,on="temperature",how="outer") #merging throught the temperature
print(mergeData2)

# grouping
group=data.groupby(by="Industry") #it will give the object of the group
getting=group.get_group("IT Services") #it will give data by grouping the specific column
print(getting)

# 
print(data["Growth"].dtype) #it will give the data type
data["Growth"]=data["Growth"].replace("%","",regex=True) #it will replace the % from black data
print(data["Growth"].dtype)
data["Growth"]=pd.to_numeric(data["Growth"])  #it will convert the data to float 
print(data.sort_values("Growth")) #if difference is not huge=mean otherwise = median
m1=data["Growth"].mean() # it will provide the mean

data["Growth"]=data["Growth"].fillna(m1) #it will fill the data to the empty cells
print(data["Growth"])

data["Expenses"]=data["Expenses"].replace(",","",regex=True)
data["Expenses"]=data["Expenses"].replace("Dollars","",regex=True)
print(data["Expenses"])
data["Expenses"]=pd.to_numeric(data["Expenses"])
print(data["Expenses"].dtype)
m2=data["Expenses"].median()     #here  we have huge difference among the data so we used median
data["Expenses"]=data["Expenses"].fillna(m2)
print(data["Expenses"])