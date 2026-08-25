import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report

# =========================================================
# Q1. Calculate Mean
# =========================================================

data = [6, 7, 8, 9, 10, 11, 12]

mean = np.mean(data)

print("Q1. Mean =", mean)


# =========================================================
# Q2. Calculate Variance and Standard Deviation
# =========================================================

variance = np.var(data)
standard_deviation = np.std(data)

print("\nQ2. Variance =", variance)
print("Q2. Standard Deviation =", standard_deviation)


# =========================================================
# Q3. Feature Scaling using StandardScaler
# =========================================================

data2 = np.array([
    [25, 20000],
    [30, 40000],
    [35, 80000]
])

scaler = StandardScaler()

scaled_data = scaler.fit_transform(data2)

print("\nQ3. Scaled Dataset:")
print(scaled_data)


# =========================================================
# Q4. Euclidean Distance Before and After Scaling
# =========================================================

# Distance between first and third points
distance_before = np.linalg.norm(data2[0] - data2[2])

distance_after = np.linalg.norm(
    scaled_data[0] - scaled_data[2]
)

print("\nQ4. Euclidean Distance Before Scaling =",
      distance_before)

print("Q4. Euclidean Distance After Scaling =",
      distance_after)


# =========================================================
# Q5 & Q6. Classification Report Metrics
# =========================================================

print("\nQ5 & Q6.")
print("Classification Report contains:")
print("Precision, Recall, F1-score, Support and Accuracy")


# =========================================================
# Q7. Calculate TP, TN, FP, FN
# =========================================================

actual =    [1, 1, 1, 1, 0, 0, 0, 0]
predicted = [1, 1, 0, 1, 0, 1, 0, 0]

TP = 0
TN = 0
FP = 0
FN = 0

for a, p in zip(actual, predicted):

    if a == 1 and p == 1:
        TP += 1

    elif a == 0 and p == 0:
        TN += 1

    elif a == 0 and p == 1:
        FP += 1

    elif a == 1 and p == 0:
        FN += 1

print("\nQ7. True Positive (TP) =", TP)
print("Q7. True Negative (TN) =", TN)
print("Q7. False Positive (FP) =", FP)
print("Q7. False Negative (FN) =", FN)


# =========================================================
# Q8. Calculate TP, TN, FP, FN using arrays
# =========================================================

print("\nQ8. TP, TN, FP, FN")
print("TP =", TP)
print("TN =", TN)
print("FP =", FP)
print("FN =", FN)


# =========================================================
# Q9. Classification Report using Scikit-learn
# =========================================================

print("\nQ9. Classification Report:")
print(classification_report(actual, predicted))