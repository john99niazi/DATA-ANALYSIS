import pandas as pd 
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
data=pd.read_csv("D:/python/project/udemy_courses.csv",parse_dates=['published_timestamp'])
print([data])

print(data.dtypes)

#1. Display Top 10 Rows of The Dataset
ROW=data.head(10)
print([ROW])
#2. Check Last 5 Rows of The Dataset
LAST_ROWS=data.tail(5)
print(LAST_ROWS)
#3. Find Shape of Our Dataset (Number of Rows And Number of Columns)
r=data.shape
print(r)
print("NUMBER OF ROWS ARE:::",data.shape[0])
print("NUMBER OF COLUMNS ARE::",data.shape[1])
# 4. Getting Information About Our Dataset Like Total Number Rows, Total Number of Columns, Datatypes of Each Column And Memory Requirement

infor=data.info()
print(infor)
#5. Check Null Values In The Dataset

NULLS=data.isnull()
f=NULLS.sum()
print(f)
#6. Check For Duplicate Data and Drop Them

DUP=data.duplicated().sum()
print("duplicated data are::", DUP)

DUP_DROP=data.drop_duplicates(inplace=True)

AGAIN_DUP=data.duplicated().sum()
print("duplicated data are::", AGAIN_DUP)

#7. Find Out Number of Courses Per Subjects
CHECK_COLUMNS=data.columns
print(CHECK_COLUMNS)
g=data['subject'].value_counts()
print("NUMBER OF COURSESS PER SUBJECT IS::", g)


'''
sns.countplot(data=data, x='subject')
plt.xlabel("Subjects",fontsize=13)
plt.ylabel("NUMBER OF COURSES PER SUBJECT",fontsize=13)
plt.xticks(rotation=65)
plt.show()'''

#8. For Which Levels, Udemy Courses Providing The Courses
LEVELLS=data['level'].value_counts()
print(LEVELLS)

'''sns.countplot(data=data, x='level')
plt.xlabel("level",fontsize=13)
plt.ylabel("NUMBER OF LEVEELS PER SUBJECT",fontsize=13)
plt.xticks(rotation=65)
plt.show()'''


courses_by_level = data.groupby('level')['course_title'].apply(list)
print("\nCourses by Level:")
print(courses_by_level)

#9. Display The Count of Paid and Free Courses 
paid_free=data['is_paid'].value_counts()
print(paid_free)

'''sns.countplot(data=data, x='is_paid')
plt.xlabel("is_paid",fontsize=10)
plt.ylabel("NUMBER OF free courses",fontsize=10)
plt.xticks(rotation=65)
plt.show()'''

#10. Which Course Has More Lectures (Free or Paid)?
mean_lectures = data.groupby('is_paid')['num_lectures'].mean()

print("Average Number of Lectures by Course Type:")
print(mean_lectures)


#11. Which Courses Have A Higher Number of Subscribers Free or Paid?
HIGHER_SUBS = data.groupby('is_paid')['num_subscribers'].mean()

print("Average Number of SUBSCRIBER by Course Type:")
print(HIGHER_SUBS)

sns.barplot(x='is_paid',y='num_subscribers',data=data)
plt.show()

#12. Which Level Has The Highest Number of Subscribers?
sns.barplot(x='level',y='num_subscribers',data=data)
plt.show()
W = data.groupby('level')['num_subscribers'].mean()

print("Average Number of SUBSCRIBER by Course Type:")
print(W)


#13. Find Most Popular Course Title
F=data[data['num_subscribers'].max()==data['num_subscribers']]['course_title']
print(F)




#14. Display 10 Most Popular Courses As Per Number of Subscribers
'''d=data.sort_values(by='num_subscribers',ascending=False)
s=d['course_title']
gs=s.head(10)    #method one
print(gs)'''

d=data.sort_values(by='num_subscribers',ascending=False).head(10)
sns.barplot(x='num_subscribers',y='course_title',data=d)
plt.show()






#15. Find The Course Which Is Having The Highest Number of Reviews.
revieW= data.loc[data['num_reviews'].idxmax()]
print("MAXIMUM REVIEW IS\n",revieW)

sns.barplot(x='subject',y='num_reviews',data=data)
plt.show()




#16. Does Price Affect the Number of Reviews?
plt.figure(figsize=(15, 8))  # Corrected figsize parameter (width, height)
sns.scatterplot(x='price', y='num_reviews', data=data)

# Set labels and title for the plot
plt.xlabel('Price')
plt.ylabel('Number of Reviews')
plt.title('Price vs. Number of Reviews')

# Show the plot
plt.show()



#17. Find Total Number of Courses Related To Python
pp=len(data[data['course_title'].str.contains('Python',case=False)])
print(pp)

#18. Display 10 Most Popular Python Courses As Per Number of Subscribers
pt=data[data['course_title'].str.contains('Python',case=False)].sort_values(by='num_subscribers',ascending=False).head(10)
print(pt)



#19. In Which Year The Highest Number of Courses Were Posted?
data['year'] = data['published_timestamp'].dt.year

# Count the number of courses posted each year and store it back in the DataFrame
# Using `value_counts` doesn't modify the DataFrame in place, but you can store the result in a new variable
courses_per_year = data['year'].value_counts()

# Find the year with the highest number of courses
# Using `idxmax()` to get the index (year) with the maximum value
year_with_max_courses = courses_per_year.idxmax()
max_courses_count = courses_per_year.max()

# Print the result
print(f"The year with the highest number of courses posted is {year_with_max_courses} with {max_courses_count} courses.")




#20. Display Category-Wise Count of Posted Subjects [Year Wise] 
vvv=data.groupby('year')['subject'].value_counts()
print(vvv)

data.to_csv("D:/python/project/UPDATEudemy_courses.csv", index=False)