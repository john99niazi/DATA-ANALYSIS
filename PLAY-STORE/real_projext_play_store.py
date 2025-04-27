import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
data=pd.read_csv("D:/python/project/googleplaystore.csv")
print([data])

#1. Display Top 5 Rows of The Dataset
R=data.head(5)
print(R)

#2. Check the Last 3 Rows of The Dataset
l=data.tail(3)
print([l])


#3. Find Shape of Our Dataset (Number of Rows & Number of Columns)


e=data.shape
print(e)
print("number of rows is",data.shape[0])
print("number of columns is",data.shape[1])
#4. Get Information About Our Dataset Like Total Number Rows, Total Number of Columns, Datatypes of Each Column And Memory Requirement
R=data.info()
print(R)

#5. Get Overall Statistics About The Dataframe
F=data.describe(include='all')
print(F)

#6. Total Number of App Titles Contain Astrology
A=sum(data['App'].str.contains('Astrology'))
print("TOTAL NUMBER OF APPS CONTAIN ASTROLGY::: ", A)

#7. Find Average App Rating
averge_rating=data['Rating'].mean()
print("THE AVERGE APP RATING IS:::",averge_rating)



#8.  Find Total Number of Unique Category

w=data['Category'].nunique()
print(w)


#9. Which Category Getting The Highest Average Rating?
b=data.groupby('Category')['Rating'].mean().sort_values(ascending=False)
print(b)


#10. Find Total Number of App having 5 Star Rating

f=len(data[data['Rating']==5.0]['App'])
print(f)


#11. Find Average Value of Reviews
data['Reviews']=data['Reviews'].replace('3.0M',3.0)
data['Reviews']=data['Reviews'].astype('float')
f=data['Reviews'].dtype
print(f)

review_averge=data['Reviews'].mean()
print(review_averge)


#12. Find Total Number of Free and Paid Apps
v=data.columns
print(v)
c=data['Type'].value_counts()
print(c)


#13.  Which App Has Maximum Reviews?
d=data[data['Reviews'].max()==data['Reviews']]
print(d)



#14. Display Top 5 Apps Having Highest Reviews
TOP=data['Reviews'].sort_values(ascending=False).head().index

f=data.iloc[TOP]['App']
print(f)



#15. Find Average Rating of Free and Paid Apps

U=data.groupby('Type')['Rating'].mean()
print(U)




# Assuming 'data' is your DataFrame
# Check the datatype of 'Installs'
s = data['Installs'].dtype
print("Original datatype of 'Installs':", s)

# Remove commas from the 'Installs' column
data['Installs_1'] = data['Installs'].str.replace(',', '')
print("After removing commas:", data['Installs_1'].head())

# Remove the '+' sign from the 'Installs' column
data['Installs_1'] = data['Installs_1'].str.replace('+', '', regex=False)
print("After removing '+':", data['Installs_1'].head())

# Handle cases where 'Installs' contains the word 'Free'
data['Installs_1'] = data['Installs_1'].str.replace('Free', '0')
print("After replacing 'Free' with '0':", data['Installs_1'].head())

# Convert the cleaned 'Installs_1' column to integer
data['Installs_1'] = data['Installs_1'].astype(int)
print("Datatype after conversion to int:", data['Installs_1'].dtype)

# Sort by 'Installs_1' in descending order and get the top 5 apps
top_5_indices = data['Installs_1'].sort_values(ascending=False).head(5).index
top_5_apps = data.iloc[top_5_indices]['App']

# Print the top 5 apps with maximum installs
print("Top 5 apps with maximum installs:")
print(top_5_apps)
