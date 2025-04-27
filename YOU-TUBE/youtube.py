import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np 

data=pd.read_csv("D:/python/project/top-5000-youtube-channels.csv")
#print([data])
#1. Display All Rows Except the Last 5 rows Using Head Method
row=data.head(-5)
print(row)

#2. Display All Rows Except the First 5 Rows Using Tail Method
roww=data.tail(-5)
print(roww)
#3. Find Shape of Our Dataset (Number of Rows And Number of Columns)
s=data.shape
print(s)
print("NUMBER OF ROWS ARE::", data.shape[0])
print("NUMBER OF COLUMNS ARE::", data.shape[1])
#4. Get Information About Our Dataset Like Total Number Rows, Total Number of Columns, Datatypes of Each Column And Memory Requirement
inform=data.info()
print(inform)
#5. Get Overall Statistics About The Dataframe

stat=data.describe()
print(stat)
#6. DATA CLEANING
data.replace('--', pd.NA,regex=True, inplace=True)
# Display the updated DataFrame
print(data)


#7. Check Null Values In The Dataset
sns.heatmap(data.isnull())
plt.show()
n=data.isnull()
N=n.sum()
print(N)

#percentage
nnn=data.isnull().sum()*100/len(data)
print(nnn)
#DROP

data.dropna(axis=0,inplace=True)
sns.heatmap(data.isnull())
plt.show()
#8. Data Cleaning [ Rank Column ]
data['Rank']=data['Rank'].str[0:-2]# slicing removed th
data['Rank']=data['Rank'].str.replace(',','')
data['Rank']=data['Rank'].astype('int')
x = data.dtypes
print(x)

#9. Data Cleaning [ Video Uploads & Subscribers ]
data['Video Uploads']=data['Video Uploads'].astype('int')
data['Subscribers']=data['Subscribers'].astype('int')
xx = data.dtypes
print(xx)


#10. Data Cleaning [ Grade Column ]
# Map the grades to numerical values
# Ensure that the 'Grade' column is of type object
data['Grade'] = data['Grade'].astype(str)

# Clean and standardize the values: remove spaces and convert to uppercase
data['Grade'] = data['Grade'].str.strip().str.upper()

# Define your grade mapping
grade_mapping = {'A++': 5, 'A+': 4, 'A': 3, 'A-': 2, 'B+': 1}

# Apply the mapping to convert grades to numerical values
data['Grade'] = data['Grade'].map(grade_mapping)

# Print the first 6 rows to see the changes
print(data.head(6))
xxx = data.dtypes
print(xxx)




#11. Find Average Views For Each Channel
data['AVERGE VIEW']=data['Video views']/data['Video Uploads']
print(data.head(5))



#12. Find Out Top Five Channels With Maximum Number of Video Uploads
# Sort the data by the 'Video Uploads' column in descending order
sorted_data = data.sort_values(by='Video Uploads', ascending=False)

# Select the top five rows
top_five_channels = sorted_data.head(5)

# Print the result
print(top_five_channels[['Channel name', 'Video Uploads']])




#13. Find Correlation Matrix








#14.  Which Grade Has A Maximum Number of Video Uploads?
# Group by 'Grade' and sum the 'Video Uploads'
uploads_by_grade = data.groupby('Grade')['Video Uploads'].sum()

# Find the grade with the maximum number of video uploads
max_uploads_grade = uploads_by_grade.idxmax()
max_uploads_value = uploads_by_grade.max()

# Print the result
print(f"Grade {max_uploads_grade} has the maximum number of video uploads: {max_uploads_value}")




#15.Which Grade Has The Highest Average Views?
# Group by 'Grade' and calculate the mean of 'Views'
average_views_by_grade = data.groupby('Grade')['Video views'].mean()

# Find the grade with the highest average views
max_average_views_grade = average_views_by_grade.idxmax()
max_average_views_value = average_views_by_grade.max()

# Print the result
print(f"Grade {max_average_views_grade} has the highest average views: {max_average_views_value}")





#16.  Which Grade Has The Highest Number of Subscribers?
# Group by 'Grade' and sum the 'Subscribers'
subscribers_by_grade = data.groupby('Grade')['Subscribers'].sum()

# Find the grade with the highest number of subscribers
max_subscribers_grade = subscribers_by_grade.idxmax()
max_subscribers_value = subscribers_by_grade.max()

# Print the result
print(f"Grade {max_subscribers_grade} has the highest number of subscribers: {max_subscribers_value}")
 



#17. Which Grade Has The Highest Video Views? 
# Group by 'Grade' and sum the 'Views'
views_by_grade = data.groupby('Grade')['Video views'].sum()

# Find the grade with the highest video views
max_views_grade = views_by_grade.idxmax()
max_views_value = views_by_grade.max()

# Print the result
print(f"Grade {max_views_grade} has the highest video views: {max_views_value}")


data.to_csv("D:/python/project/upadte_top-5000-youtube-channels.csv", index=False)

