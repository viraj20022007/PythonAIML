import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

Border = "-" * 40

# ------------------------------------------------
# Step 1 - collect a data
# ------------------------------------------------

print(Border)
print("Step 1 - collect a data")
print(Border)

Datapath = "WinePredictor.csv"
df = pd.read_csv(Datapath)

print("Dataset loaded Successfully")

# ------------------------------------------------
# Step 2 - Data Cleaning
# ------------------------------------------------

print(Border)
print("Step 2 - Data Cleaning")
print(Border)

df.dropna(inplace=True)

print("Missing values removed")
print("Shape of dataset : ", df.shape)

# ------------------------------------------------
# Step 3 - Visualisation
# ------------------------------------------------

print(Border)
print("Step 3 - Visualisation")
print(Border)

plt.scatter(
    df["Alcohol"],
    df["Malic acid"],
    alpha=0.8,
    label="Wine Samples"
)

plt.title("Wine Dataset Scatter Plot")
plt.xlabel("Alcohol")
plt.ylabel("Malic acid")
plt.grid()
plt.legend()
plt.show()

# ------------------------------------------------
# Step 4 - separate dependent and independent variables
# ------------------------------------------------

print(Border)
print("Step 4 - separate dependent and independent variables")
print(Border)

X = df.drop(columns=["Class"])
Y = df["Class"]

print("Shape of X : ", X.shape)
print("Shape of Y : ", Y.shape)

# ------------------------------------------------
# Step 5 - split the dataset for training and testing
# ------------------------------------------------

print(Border)
print("Step 5 - split the dataset for training and testing")
print(Border)

X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.2, random_state=42
)

print("Shape of X_train : ", X_train.shape)
print("Shape of X_test : ", X_test.shape)
print("Shape of Y_train : ", Y_train.shape)
print("Shape of Y_test : ", Y_test.shape)

# ------------------------------------------------
# Step 6 - Build and fit the model
# ------------------------------------------------

print(Border)
print("Step 6 - Build and fit the model")
print(Border)

model = DecisionTreeClassifier(random_state=42)

model = model.fit(X_train, Y_train)

print("Model trained successfully")

# ------------------------------------------------
# Step 7 - Prediction
# ------------------------------------------------

print(Border)
print("Step 7 - Prediction")
print(Border)

Y_pred = model.predict(X_test)

print("Predicted values : ")
print(Y_pred)

# ------------------------------------------------
# Step 8 - Accuracy
# ------------------------------------------------

print(Border)
print("Step 8 - Accuracy")
print(Border)

accuracy = accuracy_score(Y_test, Y_pred)

print("Testing Accuracy is : ", accuracy * 100)

# ------------------------------------------------
# Final Conclusion
# ------------------------------------------------

print(Border)
print("Final Conclusion")
print(Border)

print("Decision Tree model was trained on Wine dataset.")
print("The model predicted wine classes successfully.")
print("Testing accuracy is :", accuracy * 100)