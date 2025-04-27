import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
data=pd.read_csv("D:/python/project/train.csv")
print(data)
#1. Display Top 5 Rows of The Dataset
j=data.head(5)
print([j])

#2. Check the Last 3 Rows of The Dataset
k=data.tail(3)
print([k])

#3. Find Shape of Our Dataset (Number of Rows & Number of Columns)
v=data.shape
print(v)
print("number of rows",data.shape[0])
print("number of columns",data.shape[1])

#4. Get Information About Our Dataset Like Total Number Rows, Total Number of Columns, Datatypes of Each Column And Memory Requirement

k=data.info()
print([k])


#5. Get Overall Statistics About The Dataframe
l=data.describe(include="all")
print(l)


#6. Data Filtering
q=data.columns
print(q)
e=data[['Name','Age','Sex']]
print(e)

h=data['Sex']=='male'# check how many male in data
J=h.sum()
print(J)

f=data[data['Sex']=='male'][['Name','Age','Fare']]# find name of male and its age and fare
print(f)

F=data[data['Sex']=='male'] #find all in formation of male
print([F])

T=data[data['Sex']=='male'].head()
print(T)
# check how many person survied on the boat of titanic
s=data['Survived']==1
x=s.sum()
print(x)

Q=data[data['Survived']==1]['Name']
print(Q)


#7.Check Null Values In The Dataset
m=data.isnull().sum()
print(m)
'''
k = sns.heatmap(data.isnull(), cbar=False, cmap='viridis')
plt.title('Heatmap of Missing Values')
plt.show()
'''

PER_MISSING=data.isnull().sum()*100/len(data)
print(PER_MISSING)
# Drop the specified columns 'Age', 'Embarked', and 'Cabin'
data.drop(['Cabin'], axis=1, inplace=True)

# Display the updated DataFrame
p=data.isnull().sum()
print(p)




#9. Handle Missing Values
W=data['Embarked'].mode()
print(W)


W=data['Embarked'].fillna('S',inplace=True)
print(W)

u=data.isnull().sum()
print(u)


h=data['Age'].fillna(data['Age'].mean(),inplace=True)
print(h)
H=data.isnull().sum()
print(H)


#10. Categorical Data Encoding
E=data['Sex'].unique()
print(E)

# Create a new column 'GENDER' by mapping 'sex' to numeric values
X= data['Sex'].map({'male': 1, 'female': 0})

# Print the newly created 'GENDER' column
#R = data['X']
#print(R)

data.insert(5,"GENDER_NEW",X)



y=data['Embarked'].unique()
print(y)
#pd.get_dummies() is a function in pandas that converts categorical 
# variables into a form that can be provided to machine learning algorithms
#  to do a better job in prediction. This process is known as 
# one-hot encoding. It transforms each category into a new binary column, 
# indicating the presence (1) or absence (0) of the categorical feature.
pd.get_dummies(data, columns=['Embarked'])




#11 what is univirate anylsis


'''O=data['Age'].hist()
plt.show()
'''

#12 how many passenger in first class ,  second class and third class
#print([data])  Pclass
# Count the number of passengers in each class

#one method
'''first_class_count = (data['Pclass'] == 1).sum()  
second_class_count = (data['Pclass'] == 2).sum()
third_class_count = (data['Pclass'] == 3).sum()

# Print the results
print(f"First Class: {first_class_count}")
print(f"Second Class: {second_class_count}")
print(f"Third Class: {third_class_count}")'''
# second method
B=data['Pclass'].value_counts()
print(B)


k = sns.countplot(x='Pclass', data=data)

# Display the plot
plt.title('Count of Passengers in Each Class')
plt.xlabel('Passenger Class')
plt.ylabel('Number of Passengers')
plt.show()




#13 number of male and female passengers
i=data['Sex'].value_counts()
print(i)

hh = sns.countplot(x='Sex', data=data)

# Display the plot
plt.title('sex of Passengers in Each Class')
plt.xlabel('sex Class')
plt.ylabel('Number of Passengers MALE OR FEAMLE')
plt.show()


plt.hist(data['Age'])
plt.show()


sns.boxplot(data['Age'],orient='v')
plt.show()

#14 bivirative anylsisi

#how has better chance of survival  amle or female

sns.barplot(x='Pclass',y='Survived',data=data)
plt.show()

sns.barplot(x='Sex',y='Survived',data=data)
plt.show()


#feturing engenieerring
#Feature engineering is a crucial step in the data preprocessing
#  phase of machine learning and data analysis. 
# It involves creating new features or modifying existing ones to improve the
#  performance of machine learning models. Good feature engineering 
# can enhance model accuracy and enable more insightful analysis.

data['total_family'] = data['SibSp'] + data['Parch']

# Insert the new column 'total_family' at the 6th position (index 6)
data.insert(6, 'total_family', data.pop('total_family'))





data.to_csv("D:/python/project/train_update_version.csv", index=False)

