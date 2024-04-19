import pandas as pd
#1. Explore the data
data=pd.read_csv('./car details v4.csv')
print(data)
#2 Remove these columns if the percentage of missing values is less than 3%.
total_missing=(data.isnull().sum()/len(data)) *100
required_missing=total_missing[total_missing<3].index
remain_data=data.drop(columns=required_missing)
print(remain_data)

#3.  Fill the missing value using appropriate technique
newData=data.bfill()
print(newData)

# 4, Count the total number of missing values in each data column, as well as the total number of missing values in the entire dataset.

total_missing_per_column = data.isnull().sum()
total_missing = total_missing_per_column.sum()
print(total_missing_per_column)
print(total_missing)

# 5, display only the missing value row and the overall missing value column.
missing_row=data[data.isnull().any(axis=1)]
print("Rows with missing value:" )
print(missing_row)