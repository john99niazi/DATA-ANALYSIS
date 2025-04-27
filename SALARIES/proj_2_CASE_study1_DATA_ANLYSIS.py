import pandas as pd

#data=pd.read_csv("D:/python/project/Salaries.csv")
data = pd.read_csv('D:/python/project/Salaries.csv',dtype={'BasePay': str, 'OvertimePay': str,
                                                            'OtherPay': str, 'TotalPay': str, 'TotalPayBenefits': str,
                                                            'Benefits':str,'Status':str})





#1.Display Top 10 Rows of The Dataset
'''j=data.head(10)
print(j)'''



#2. Check Last 10 Rows of The Dataset
'''A=data.tail(10)
print(A)'''

#3. Find Shape of Our Dataset (Number of Rows And Number of Columns)
'''b=data.shape
print(b)
'''
#4.  Getting Information About Our Dataset Like Total Number Rows, Total Number of Columns, Datatypes of Each Column And Memory Requirement
'''i=data.info()
print(i)'''


#5. Check Null Values In all The Dataset
'''t=data.isnull().sum(axis=0)
print(t)'''

#6. Drop ID, Notes, Agency, and Status Columns
#axis 0 for rows and axis 1 for columns
'''data.drop(["Id","Notes","Agency","Status"],axis=1,inplace=True)
print(data)
'''

#7. Get Overall Statistics About The Dataframe
'''k=data.describe(include='all')
print(k)'''


#8. Find Occurrence of The Employee Names  (Top 5)
#df['EmployeeName'].value_counts(): Counts how many times each unique value appears in the 'EmployeeName' column.
#.head(5): Selects the top 5 results from the counts.
'''j=data["EmployeeName"].value_counts()
l=j.head(5)
print(l)'''

#9. Find The Number of Unique Job Titles
'''e=data["JobTitle"].nunique()

print(e)'''


#10.Total Number of Job Titles Contain Captain
#=False makes the search case-insensitive.
#na=False ensures that NaN values are not included in the search results.
j = len(data[data['JobTitle'].str.contains('Captain')])



print(j)


#11. Display All the Employee Names From Fire Department
'''fire_dept_employees = data[data["JobTitle"].str.contains("FIRE DEPARTMENT")][["EmployeeName","BasePay"]]
print(fire_dept_employees)
#print(fire_dept_employees) it will display all the data

'''

#12. Find Minimum, Maximum, and Average BasePay

data['BasePay'] = pd.to_numeric(data['BasePay'], errors='coerce')

data['BasePay'].fillna(data['BasePay'].mean(), inplace=True)


'''average_basepay = data['BasePay'].mean()
max_basepay = data['BasePay'].max()
min_basepay = data['BasePay'].min()

# Print the results
print(f"Average BasePay: {average_basepay}")
print(f"Max BasePay: {max_basepay}")'''

#13. Replace 'Not Provided' in EmployeeName' Column to NaN 
'''
#j=data['EmployeeName'].replace('Not provided', pd.NA)
j=data["EmployeeName"].replace("Not provided",pd.NA)
print(j)
'''


#14. Drop The Rows Having 5 Missing Values
'''data1 = data.drop(data[data.isnull().sum(axis=1) == 5].index,axis=0,inplace=True)

k=data.isnull().sum(axis=1)
print(k)'''

#15. Find Job Title of ALBERT PARDINI
'''job_title = data[data['EmployeeName'] == 'Albert Pardini']['JobTitle'].values
print(job_title)'''

#16. How Much ALBERT PARDINI Make (Include Benefits)?
'''total = data[data['EmployeeName'] == 'Albert Pardini']['Benefits'].values

print(total)'''

#17.Display Name of The Person Having The Highest BasePay
'''j=data['BasePay'].max()
k=data[data['BasePay']== j][['EmployeeName','BasePay']].values
print(k)
'''
#18.Find Average BasePay of All Employee Per Year 
# Group by 'Year' and calculate the mean BasePay for each year
'''average_base_pay_per_year = data.groupby('Year')['BasePay'].mean()
print(average_base_pay_per_year)

'''

#19. Find Average BasePay of All Employee Per JobTitle 
'''average_base_pay_per_year = data.groupby('JobTitle')['BasePay'].mean()
print(average_base_pay_per_year)'''



#20. Find Average BasePay of Employee Having Job Title ACCOUNTANT  
'''accountants = data[data['JobTitle'] == 'ACCOUNTANT']

# Calculate the average BasePay for accountants
average_base_pay_accountants = accountants['BasePay'].mean()

print(average_base_pay_accountants)'''

#21. Find Top 5 Most Common Jobs
'''top_5_common_jobs = data['JobTitle'].value_counts().head(5)

print(top_5_common_jobs)'''