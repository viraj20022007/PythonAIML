import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Step 1: Get Data
df = pd.read_csv("Advertising.csv")

print("Original Dataset:")
print(df)

# Step 2: Clean, Prepare and Manipulate Data

# Input features
X = df[['TV', 'radio', 'newspaper']]

# Output / target
Y = df['sales']

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.5,random_state=42)

#model creation
model = LinearRegression()

# Train the model
model = model.fit(X_train,Y_train)

# Predict sales
Y_pred = model.predict(X_test)

# Step 5: Display Expected and Predicted Values

print("\nExpected Sales:")
print(Y_test.values)

print("\nPredicted Sales:")
print(Y_pred)

print("\nComparison:")
for expected, predicted in zip(Y_test, Y_pred):
    print("Expected =", expected, " Predicted =", round(predicted, 2))