import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler

# Create the DataFrame from previous assignment
data = {
    'Name': ['Amit', 'Sagar', 'Pooja'],
    'Math': [85, 90, 78],
    'Science': [92, 88, 80],
    'English': [75, 85, 82]
}

df = pd.DataFrame(data)

# Add Total column
df['Total'] = df['Math'] + df['Science'] + df['English']

print("Original DataFrame:")
print(df)


# Q1: Normalize Math scores using Min-Max Scaling

scaler = MinMaxScaler()

df['Math_Normalized'] = scaler.fit_transform(df[['Math']])

print("\nQ1 - Math scores after Min-Max Scaling:")
print(df[['Name', 'Math', 'Math_Normalized']])


# Q2: Create Gender column and perform One-Hot Encoding

df['Gender'] = ['Male', 'Male', 'Female']

gender_encoded = pd.get_dummies(df['Gender'], prefix='Gender')

df = pd.concat([df, gender_encoded], axis=1)

print("\nQ2 - One-Hot Encoding:")
print(df)


# Q3: Group students by Gender and calculate average marks

average_marks = df.groupby('Gender')[['Math', 'Science', 'English', 'Total']].mean()

print("\nQ3 - Average marks by Gender:")
print(average_marks)


# Q4: Pie chart of subject marks for Sagar

sagar = df[df['Name'] == 'Sagar']

subjects = ['Math', 'Science', 'English']
marks = [
    sagar['Math'].values[0],
    sagar['Science'].values[0],
    sagar['English'].values[0]
]

plt.pie(marks, labels=subjects, autopct='%1.1f%%')
plt.title("Sagar's Subject Marks")
plt.show()


# Q5: Add Status column

df['Status'] = df['Total'].apply(
    lambda x: 'Pass' if x >= 250 else 'Fail'
)

print("\nQ5 - Student Status:")
print(df[['Name', 'Total', 'Status']])


# Q6: Count how many students passed

passed_students = (df['Status'] == 'Pass').sum()

print("\nQ6 - Number of students passed:")
print(passed_students)


# Q7: Export final DataFrame to CSV

df.to_csv('student_final.csv', index=False)

print("\nQ7 - DataFrame exported successfully to student_final.csv")


# Q8: Histogram of Math marks

plt.hist(df['Math'], bins=5)
plt.xlabel('Math Marks')
plt.ylabel('Number of Students')
plt.title('Distribution of Math Marks')
plt.show()


# Q9: Rename Math column to Mathematics

df = df.rename(columns={'Math': 'Mathematics'})

print("\nQ9 - After renaming Math to Mathematics:")
print(df)


# Q10: Boxplot for English marks

plt.boxplot(df['English'])
plt.ylabel('English Marks')
plt.title('Boxplot of English Marks')
plt.show()