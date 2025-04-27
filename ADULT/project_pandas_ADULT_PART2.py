import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
data=pd.read_csv("D:/python/project\k/adult.csv")




#0. Get Overall Statistics About The Dataframe
j=data.describe(include='all')
print(j)

#11. Drop The Columns education-num, capital-gain, and capital-loss

data.drop(['educational-num','capital-gain','capital-loss'],axis=1,inplace=True)

print(data.columns)

#univiratedd anylsisss
#Univariate analysis is a statistical technique used to analyze a single variable or feature in isolation.
#  The goal is to summarize and understand the distribution, central tendency, 
# and dispersion of that variable. It focuses on exploring and describing the characteristics of one variable at a time.

#12. What Is The Distribution of Age Column?
'''j=data['age'].describe()
print(j)

r=data['age'].hist()
plt.show()
'''
#13. Find Total Number of Persons Having Age Between 17 To 48 (Inclusive) Using Between Method
'''g=sum((data['age']>=17) & (data['age']<=48))
print(g)'''
f=sum(data['age'].between(17,48))
print(f)


#14. What is The Distribution of Workclass Column?
'''v=data['workclass'].describe()
print(v)
plt.figure(figsize=(10,10))
V=data['workclass'].hist()
plt.show()'''

#15. How Many Persons Having Bachelors and Masters Degree?
k=data[data['education'].str.contains('Bachelors|Masters',case=False, na=False)]
print(k)

K=sum(data['education'].isin(['Bachelors','Masters']))
print(K)

#16. Bivariate Analsis
#Bivariate analysis involves examining the relationship between two variables.
#  It is used to understand how two variables interact 
# and whether they are related to each other in some way.
#  This type of analysis can help in identifying patterns,
#  correlations, and potential causal relationships between the variables.

'''sns.boxplot(x='income',y='age',data=data)
plt.show()'''




#17. Replace Salary Values With 0 and 1(<=50K and >=50K)
print(data['income'].unique())
data['income'].replace({'<=50K': 0, '>50K': 1}, inplace=True)
print(data)


#18. Which Workclass Getting The Highest Salary?

# Group by 'workclass', calculate the mean income, and sort the values in descending order
x = data.groupby('workclass')['income'].mean().sort_values(ascending=False)

# Display the result
print(x)

#19.How Has Better Chance To Get Salary greater than 50K Male or Female?
# Group by 'workclass', calculate the mean income, and sort the values in descending order
p = data.groupby('gender')['income'].mean().sort_values(ascending=False)

# Display the result
print(p)

#20. Covert workclass Columns Datatype To Category Datatype
d=data.info()
print(d)

# Convert 'workclass' column to categorical datatype
data['workclass'] = data['workclass'].astype('category')

# Display the DataFrame to verify the conversion
print(data.dtypes)

data.to_csv("D:/python/project\k/adultrrrrrr.csv", index=False)
