import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, confusion_matrix

# 3 separate uni-models
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier

from sklearn.ensemble import VotingClassifier


#------------------------------------#
# Step 1 - Load the data set
#------------------------------------#

Border = "-" * 50

print(Border)
print("Step 1 - Load the data set")
print(Border)

df = pd.read_csv("Customer_Loan_Approval.csv")

print("Shape of Dataset : ", df.shape)

print("First 5 records : ")
print(df.head())


#---------------------------------------#
# Step 2 - Check Missing Values
#---------------------------------------#

print(Border)
print("Step 2 - Check Missing Values")
print(Border)

print(df.isnull().sum())


#---------------------------------------#
# Step 3 - Separate Features and Labels
#---------------------------------------#

print(Border)
print("Step 3 - Separate Features and Labels")
print(Border)

X = df.drop("LoanApproved", axis=1)
Y = df["LoanApproved"]

print("X Shape : ", X.shape)
print("Y Shape : ", Y.shape)


#-----------------------------------------------------#
# Step 4 - Split the dataset for training and testing
#-----------------------------------------------------#

print(Border)
print("Step 4 - Split the dataset for training and testing")
print(Border)

X_train, X_test, Y_train, Y_test = train_test_split(
    X,
    Y,
    test_size=0.2,
    random_state=42
)


#-----------------------------------------------------#
# Step 5 - Scale the features
#-----------------------------------------------------#

print(Border)
print("Step 5 - Scale the features")
print(Border)

Scaler = StandardScaler()

X_train = Scaler.fit_transform(X_train)

X_test = Scaler.transform(X_test)


#-----------------------------------------------------#
# Step 6 - Create the individual models
#-----------------------------------------------------#

print(Border)
print("Step 6 - Create the individual models")
print(Border)

model_log = LogisticRegression(max_iter=1000)

model_det = DecisionTreeClassifier(random_state=42)

model_knn = KNeighborsClassifier(n_neighbors=5)


#-----------------------------------------------------#
# Step 7 - Train Individual Models
#-----------------------------------------------------#

print(Border)
print("Step 7 - Train Individual Models")
print(Border)

model_log.fit(X_train, Y_train)

model_det.fit(X_train, Y_train)

model_knn.fit(X_train, Y_train)


#-----------------------------------------------------#
# Step 8 - Calculate Individual Accuracies
#-----------------------------------------------------#

print(Border)
print("Step 8 - Individual Model Accuracies")
print(Border)

Y_pred_log = model_log.predict(X_test)

Y_pred_det = model_det.predict(X_test)

Y_pred_knn = model_knn.predict(X_test)

accuracy_log = accuracy_score(Y_test, Y_pred_log)

accuracy_det = accuracy_score(Y_test, Y_pred_det)

accuracy_knn = accuracy_score(Y_test, Y_pred_knn)

print("Logistic Regression Accuracy : ", accuracy_log * 100)

print("Decision Tree Accuracy       : ", accuracy_det * 100)

print("KNN Accuracy                 : ", accuracy_knn * 100)


#-----------------------------------------------------#
# Step 9 - Create Hard Voting Classifier
#-----------------------------------------------------#

print(Border)
print("Step 9 - Create Hard Voting Classifier")
print(Border)

hard_model = VotingClassifier(
    estimators=[
        ('logistic', model_log),
        ('decision_tree', model_det),
        ('knn', model_knn)
    ],
    voting='hard'
)


#-----------------------------------------------------#
# Step 10 - Train Hard Voting Classifier
#-----------------------------------------------------#

print(Border)
print("Step 10 - Train Hard Voting Classifier")
print(Border)

hard_model.fit(X_train, Y_train)


#-----------------------------------------------------#
# Step 11 - Hard Voting Accuracy
#-----------------------------------------------------#

print(Border)
print("Step 11 - Hard Voting Accuracy")
print(Border)

Y_pred_hard = hard_model.predict(X_test)

hard_accuracy = accuracy_score(Y_test, Y_pred_hard)

print("Hard Voting Accuracy : ", hard_accuracy * 100)

print("Confusion Matrix : ")

print(confusion_matrix(Y_test, Y_pred_hard))


#-----------------------------------------------------#
# Step 12 - Create Soft Voting Classifier
#-----------------------------------------------------#

print(Border)
print("Step 12 - Create Soft Voting Classifier")
print(Border)

soft_model = VotingClassifier(
    estimators=[
        ('logistic', model_log),
        ('decision_tree', model_det),
        ('knn', model_knn)
    ],
    voting='soft'
)


#-----------------------------------------------------#
# Step 13 - Train Soft Voting Classifier
#-----------------------------------------------------#

print(Border)
print("Step 13 - Train Soft Voting Classifier")
print(Border)

soft_model.fit(X_train, Y_train)


#-----------------------------------------------------#
# Step 14 - Soft Voting Accuracy
#-----------------------------------------------------#

print(Border)
print("Step 14 - Soft Voting Accuracy")
print(Border)

Y_pred_soft = soft_model.predict(X_test)

soft_accuracy = accuracy_score(Y_test, Y_pred_soft)

print("Soft Voting Accuracy : ", soft_accuracy * 100)

print("Confusion Matrix : ")

print(confusion_matrix(Y_test, Y_pred_soft))


#-----------------------------------------------------#
# Step 15 - Compare
#-----------------------------------------------------#

print(Border)
print("Step 15 - Comparison")
print(Border)

print("Logistic Regression : ", accuracy_log * 100)

print("Decision Tree       : ", accuracy_det * 100)

print("KNN                 : ", accuracy_knn * 100)

print("Hard Voting         : ", hard_accuracy * 100)

print("Soft Voting         : ", soft_accuracy * 100)

print(Border)