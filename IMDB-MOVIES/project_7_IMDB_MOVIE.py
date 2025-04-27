import pandas as  pd
import seaborn as sns 
import matplotlib.pyplot as plt
import numpy as np 
data=pd.read_csv("D:/python/project/IMDB-Movie-Data.csv")
#1. Display Top 10 Rows of The Dataset
H=data.head(10)
print([H])
#2. Check Last 10 Rows of The Dataset
T=data.tail(10)
print(T)

#3. Find Shape of Our Dataset (Number of Rows And Number of Columns)
print("TOTAL NUMBER OF ROWS:::", data.shape[0])
print("TOTAL NUMBER OF COLUMNS:::", data.shape[1])



#4. Getting Information About Our Dataset Like Total Number Rows, Total Number of Columns, Datatypes of Each Column And Memory Requirement
I=data.info()
print(I)



#5. Check Missing Values In The Dataset
sns.heatmap(data.isnull())
plt.show()
N=data.isnull().sum()
print(N)



#6. Drop All The  Missing Values
data.dropna(axis=0,inplace=True)
NN=data.isnull().sum()
print(NN)

#7. Check For Duplicate Data
D=data.duplicated().sum()
print("DUPLICATED DATA ARE::",  D)

#8. Get Overall Statistics About The DataFrame
descr=data.describe()
print(descr)

#9. Display Title of The Movie Having Runtime Greater Than or equal to 180 Minutes
f=data[data['Runtime (Minutes)']>=180]
ss=f['Title']
print(ss)

#10. In Which Year There Was The Highest Average Voting?

average_votes_per_year = data.groupby('Year')['Votes'].mean()

year_with_highest_average_votes = average_votes_per_year.idxmax()
highest_average_votes = average_votes_per_year.max()

print(f"The year with the highest average voting is {year_with_highest_average_votes} with an average of {highest_average_votes} votes.")



#11. In Which Year There Was The Highest Average Revenue?
f=data.groupby('Year')['Revenue (Millions)'].mean()
year_with_highest_revenue=f.idxmax()
j=f.max()
print(f"THE YEAR WITH HIIGESR REVENUE is  {year_with_highest_revenue}  with averge is    {j}")


#12. Find The Average Rating For Each Director
Average_Rating_For_Each_Director=data.groupby('Director')['Rating'].mean()
print(Average_Rating_For_Each_Director)


#13. Display Top 10 Lengthy Movies Title and Runtime
Lengthy_Movies_Title_and_Runtime=data.sort_values(by="Runtime (Minutes)",ascending=False)
lll=Lengthy_Movies_Title_and_Runtime['Title']
fff=lll.head(10)
print(fff)



#14. Display Number of Movies Per Year
k=data['Year'].value_counts().sort_index()

print(k)

#15. Find Most Popular Movie Title (Highest Revenue)
Higest_revenue=data['Revenue (Millions)'].max()
ssd=data[data['Revenue (Millions)']==Higest_revenue]['Title']


print(ssd)

#16. Display Top 10 Highest Rated Movie Titles And its Directors
HIGHEST_RATED=data.sort_values('Rating',ascending=False)
e=HIGHEST_RATED.head(10)
dss=e[['Title','Director']]
print(dss)

#17. Display Top 10 Highest Revenue Movie Titles
t=data.sort_values('Revenue (Millions)',ascending=False)
d=t.head(10)
pp=d['Title']
print(pp)

#18.  Find Average Rating of Movies Year Wise
average_rating_per_year = data.groupby('Year')['Rating'].mean()

print(average_rating_per_year)



#19. Does Rating Affect The Revenue?
plt.figure(figsize=(10, 6))
plt.scatter(data['Rating'], data['Revenue (Millions)'], color='blue', alpha=0.5)
plt.title('Rating vs. Revenue')
plt.xlabel('Rating')
plt.ylabel('Revenue (Millions)')
plt.grid(True)
plt.show()

#20. Classify Movies Based on Ratings [Excellent, Good, and Average]
def classify_rating(rating):
    if rating >= 8:
        return 'Excellent'
    elif rating >= 7:
        return 'Good'
    else:
        return 'Average'

# Apply classification
data['Classification'] = data['Rating'].apply(classify_rating)
print(data)
#21. Count Number of Action Movies
'''ll=data['Genre'].str.contains('Action')
www=ll.count()
print(www)'''
action_movies = data['Genre'].str.contains('Action').sum()

#num_action_movies = action_movies.sum()

print(f"Number of Action Movies: {action_movies}")
#22. Find Unique Values From Genre 
wwww=len(data['Genre'].unique())

print(wwww)
#23. How Many Films of Each Genre Were Made?
genre_counts = data['Genre'].value_counts()

print(genre_counts)



data.to_csv('D:/python/project/UPDATE_IMDB-Movie-Data.csv',index=False)
