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

print("Last entries from dataset are : ")
print(df.tail()) #last 5 rows 

print("Shape of Dataset : ",df.shape)

print("\nTotal rows and columns:")
print(df.shape)

print("\nColumn names:")
print(df.columns)

print("\nData types:")
print(df.dtypes)

