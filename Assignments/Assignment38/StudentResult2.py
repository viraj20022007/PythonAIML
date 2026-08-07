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