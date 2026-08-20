import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Q1: Create a DataFrame
data = {
    'Name': ['Amit', 'Sagar', 'Pooja'],
    'Math': [85, 90, 78],
    'Science': [92, 88, 80],
    'English': [75, 85, 82]
}

df = pd.DataFrame(data)

print("DataFrame:")
print(df)

print("\nShape:")
print(df.shape)

print("\nColumns:")
print(df.columns)

print("\nData Types:")
print(df.dtypes)


# Q2: Descriptive Statistics
print("\nDescriptive Statistics:")
print(df.describe())


# Q3: Add Total column
df['Total'] = df['Math'] + df['Science'] + df['English']

print("\nDataFrame with Total:")
print(df)


# Q4: Students who scored more than 85 in Science
print("\nStudents who scored more than 85 in Science:")
print(df[df['Science'] > 85])


# Q5: Replace Pooja with Puja
df['Name'] = df['Name'].replace('Pooja', 'Puja')

print("\nAfter replacing Pooja with Puja:")
print(df)


# Q6: Sort by Total in descending order
sorted_df = df.sort_values(by='Total', ascending=False)

print("\nSorted DataFrame:")
print(sorted_df)


# Q7: Bar plot of Student Names vs Total Marks
plt.bar(df['Name'], df['Total'])
plt.xlabel('Student Name')
plt.ylabel('Total Marks')
plt.title('Student Names vs Total Marks')
plt.show()


# Q8: Line chart of Amit's marks
amit = df[df['Name'] == 'Amit']

subjects = ['Math', 'Science', 'English']
marks = [amit['Math'].values[0],
         amit['Science'].values[0],
         amit['English'].values[0]]

plt.plot(subjects, marks, marker='o')
plt.xlabel('Subjects')
plt.ylabel('Marks')
plt.title("Amit's Marks Across All Subjects")
plt.show()


# Q9: DataFrame with missing values
data2 = {
    'Name': ['Amit', 'Sagar', 'Pooja'],
    'Math': [np.nan, 76, 88],
    'Science': [91, np.nan, 85]
}

df2 = pd.DataFrame(data2)

print("\nDataFrame with Missing Values:")
print(df2)

# Fill missing values with column mean
df2['Math'] = df2['Math'].fillna(df2['Math'].mean())
df2['Science'] = df2['Science'].fillna(df2['Science'].mean())

print("\nAfter Filling Missing Values:")
print(df2)


# Q10: Drop English column
df_dropped = df.drop('English', axis=1)

print("\nDataFrame after dropping English column:")
print(df_dropped)