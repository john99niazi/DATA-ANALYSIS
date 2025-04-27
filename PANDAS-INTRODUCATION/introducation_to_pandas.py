'''with open("D:/python/opp_in_python/faculty_data.csv") as data_file:
    data=data_file.readlines()
    print(data)'''

'''import csv
with open("D:/python/opp_in_python/faculty_data.csv")as data_file:
     data=csv.reader(data_file)
     print(data)
     qualifiacation=[]
     for row in data: 
        if row[0]!="Name":
            
            print(row[0]) # print(row) all data arrange in row form accirately when we print row[1] only first index is print
'''




#know we work with pandas     ####pandas are simple and so powerfull when you trying to process and anlyze data
#it always used better pandas
'''import pandas
data=pandas.read_csv("D:/python/opp_in_python/faculty_data.csv")
print(data["Name"])'''


'''
import pandas
data=pandas.read_csv("C:/Users/kashif pc/OneDrive/Desktop/SCRAPEE DATA/price oye/IPHONE PRICE OYE.csv")
#print(type(data))

print(type(data["name"]))


'''
######################################################
# LOADING THE DATA
'''import pandas as pd

# Load data from a CSV file
df = pd.read_csv('file.csv')

# Load data from an Excel file
df = pd.read_excel('file.xlsx')

# Load data from a SQL database
# df = pd.read_sql(query, connection)

# Load data from a JSON file
df = pd.read_json('file.json')'''

# INSPECTING THE DATA
'''# Display the first few rows of the dataframe
print(df.head())

# Display the last few rows of the dataframe
print(df.tail())

# Get a concise summary of the dataframe
print(df.info())

# Get the summary statistics of the dataframe
print(df.describe())

# Display the column names
print(df.columns)

# Check the shape of the dataframe (rows, columns)
print(df.shape)'''

# DATA CLEANING
# Handling missing values
'''df = df.dropna()  # Drop rows with missing values
df = df.fillna(value)  # Fill missing values with a specified value

# Removing duplicates
df = df.drop_duplicates()

# Converting data types
df['column_name'] = df['column_name'].astype('int')
'''
#    DATA TRANFORAMTION
'''# Filtering data
filtered_df = df[df['column_name'] > 50]

# Sorting data
sorted_df = df.sort_values(by='column_name', ascending=False)

# Grouping data and performing aggregations
grouped_df = df.groupby('column_name').sum()

# Applying functions
df['new_column'] = df['existing_column'].apply(lambda x: x + 10)

#converting into dictionary
'''


# DATA ANLYSIS
'''# Descriptive statistics
mean_value = df['column_name'].mean()
median_value = df['column_name'].median()
mode_value = df['column_name'].mode()

# Correlation matrix
correlation_matrix = df.corr()

# Value counts
value_counts = df['column_name'].value_counts()
'''


# VISIULAZATION
'''import matplotlib.pyplot as plt
import seaborn as sns

# Line plot
df['column_name'].plot(kind='line')
plt.show()

# Histogram
df['column_name'].plot(kind='hist')
plt.show()

# Scatter plot
df.plot(kind='scatter', x='column1', y='column2')
plt.show()

# Correlation heatmap
sns.heatmap(df.corr(), annot=True)
plt.show()
'''


# SAVING THE DATA
'''# Exporting to CSV
df.to_csv('output.csv', index=False)

# Exporting to Excel
df.to_excel('output.xlsx', index=False)

# Exporting to JSON
df.to_json('output.json', orient='records')
'''


# HANDLING LARGE DATA SET
'''# Load a large dataset with specific data types to save memory
df = pd.read_csv('large_file.csv', dtype={'column1': 'int32', 'column2': 'float32'})

# Reading data in chunks
chunk_size = 10000
for chunk in pd.read_csv('large_file.csv', chunksize=chunk_size):
    process(chunk)
'''


#LIST COMPREHSENISON

#SYNTAX  [expression for item in iterable if condition]

#SQUARE
#  squares = [x**2 for x in range(10)]
#print(squares)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

#EVEN
#evens = [x for x in range(10) if x % 2 == 0]
#print(evens)  # Output: [0, 2, 4, 6, 8]


#STRING TO UPPER CASE

#words = ["hello", "world", "python"]
#upper_words = [word.upper() for word in words]
#print(upper_words)  # Output: ['HELLO', 'WORLD', 'PYTHON']

#LENGTH OF WORDS
#words = ["apple", "it", "banana", "dog"]
#lengths = [len(word) for word in words if len(word) > 3]
#print(lengths)  # Output: [5, 6]

#BENIFITS
#Conciseness: List comprehensions reduce the number of lines of code compared to traditional loops.
#Readability: They can be easier to read and understand for simple transformations and filters.
#Efficiency: List comprehensions can be faster than using traditional for loops because they are optimized internally.








