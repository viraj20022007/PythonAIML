import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns


Border = "-"*30

print(Border)
print("Step 1 - Load the dataset")
print(Border)

DataPath = "student_performance_ml.csv"
df = pd.read_csv(DataPath) 

print("Dataset loaded Successfully")
print("Intial entries from dataset are : ")
print(df.head()) #first 5 rows 

print(Border)

print("Last entries from dataset are : ")
print(df.tail()) #last 5 rows 

print(Border)

print("Shape of Dataset : ",df.shape)

print(Border)

print("\nTotal rows and columns:")
print(df.shape)

print(Border)

print("\nColumn names:")
print(df.columns)

print(Border)

print("\nData types:")
print(df.dtypes)

print(Border)

print("Total number of students:")
totalstu = len(df)
print(totalstu)

print(Border)

result_count = df["FinalResult"].value_counts()
print("Passed :", result_count[1])
print("Failed :", result_count[0])

print(Border)

avg = df["StudyHours"].mean()
print("average study hrs : ",avg)

avg = df["Attendance"].mean()
print("average attendance : ",avg)

MaxScore = df["PreviousScore"].max()
print("Max previous score : ", MaxScore)

MaxSleephr = df["SleepHours"].max()
print("Max sleep hrs : ", MaxSleephr)

print(Border)
print("Step 4 - Check Dataset Balance")
print(Border)

result_count = df["FinalResult"].value_counts()

print("Passed Students :", result_count[1])
print("Failed Students :", result_count[0])

if result_count[1] == result_count[0]:
    print("Dataset is perfectly balanced.")
else:
    print("Dataset is not perfectly balanced.")

print(Border)
print("Step 5 - Analysis of StudyHours and Attendance")
print(Border)

# Average StudyHours for Passed and Failed students
pass_study = df[df["FinalResult"] == 1]["StudyHours"].mean()
fail_study = df[df["FinalResult"] == 0]["StudyHours"].mean()

print("Average StudyHours of Passed Students :", pass_study)
print("Average StudyHours of Failed Students :", fail_study)

# Average Attendance for Passed and Failed students
pass_att = df[df["FinalResult"] == 1]["Attendance"].mean()
fail_att = df[df["FinalResult"] == 0]["Attendance"].mean()

print("Average Attendance of Passed Students :", pass_att)
print("Average Attendance of Failed Students :", fail_att)

print("\nObservations:")
print("1. Students who study more hours generally have a higher chance of passing.")
print("2. Students with better attendance tend to achieve better final results.")
print("3. Lower study hours and attendance are associated with a higher chance of failure.")
print("4. Both StudyHours and Attendance positively influence FinalResult.")

print(Border)
print("Step 6 - Histogram of StudyHours")
print(Border)

plt.figure(figsize=(8,5))
plt.hist(df["StudyHours"], bins=10, edgecolor='black')
plt.title("Histogram of StudyHours")
plt.xlabel("Study Hours")
plt.ylabel("Number of Students")
plt.show()

print("Explanation:")
print("The histogram shows how StudyHours are distributed among students.")
print("The tallest bars represent the range where most students study.")
print("It helps identify whether students generally study fewer or more hours.")

print(Border)
print("Step 7 - Scatter Plot")
print(Border)

plt.figure(figsize=(8,5))
plt.scatter(df["StudyHours"], df["PreviousScore"])
plt.title("StudyHours vs PreviousScore")
plt.xlabel("StudyHours")
plt.ylabel("PreviousScore")
plt.show()

print("Explanation:")
print("Each point represents one student.")
print("The plot helps observe the relationship between StudyHours and PreviousScore.")
print("If points show an upward trend, students who study more tend to have higher previous scores.")

print(Border)
print("Step 8 - Boxplot for Attendance")
print(Border)

plt.figure(figsize=(6,5))
sns.boxplot(y=df["Attendance"])

plt.title("Boxplot of Attendance")
plt.ylabel("Attendance")
plt.show()

print("Observation:")
print("Points appearing outside the whiskers are considered outliers.")
print("If no points are outside the whiskers, then significant outliers are not present.")

print(Border)
print("Step 9 - AssignmentsCompleted vs FinalResult")
print(Border)

plt.figure(figsize=(7,5))
sns.countplot(x="AssignmentsCompleted", hue="FinalResult", data=df)

plt.title("AssignmentsCompleted vs FinalResult")
plt.xlabel("AssignmentsCompleted")
plt.ylabel("Count of Students")
plt.legend(title="FinalResult", labels=["Fail", "Pass"])
plt.show()

print("Observation:")
print("Students who completed more assignments tend to have a higher pass count.")
print("Students with fewer completed assignments show a higher failure count.")
print("Assignment completion appears to positively influence FinalResult.")

print(Border)
print("Step 10 - SleepHours vs FinalResult")
print(Border)

plt.figure(figsize=(7,5))
sns.boxplot(x="FinalResult", y="SleepHours", data=df)

plt.title("SleepHours vs FinalResult")
plt.xlabel("FinalResult (0 = Fail, 1 = Pass)")
plt.ylabel("SleepHours")
plt.show()

print("Observation:")
print("The plot compares sleep hours of passed and failed students.")
print("Sleeping more may help concentration and health, but it does not guarantee success.")
print("StudyHours, Attendance, and AssignmentsCompleted also play important roles.")
print("Success depends on multiple factors, not only SleepHours.")