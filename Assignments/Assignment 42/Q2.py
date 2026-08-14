import numpy as np
import math

# Function to calculate Euclidean Distance
def MarvellousEucDistance(P1, P2):
    Ans = math.sqrt((P1['X'] - P2['X'])**2 +
                    (P1['Y'] - P2['Y'])**2)
    return Ans


# KNN Classifier Function
def MarvellousKNNClassifier(K=3):

    Border = "-" * 50

    Data = [
        {'point': 'A', 'X': 1, 'Y': 2, 'Label': 'Red'},
        {'point': 'B', 'X': 2, 'Y': 3, 'Label': 'Red'},
        {'point': 'C', 'X': 3, 'Y': 1, 'Label': 'Blue'},
        {'point': 'D', 'X': 5, 'Y': 6, 'Label': 'Blue'},
        {'point': 'E', 'X': 4, 'Y': 4, 'Label': 'Blue'}
    ]

    print(Border)
    print("KNN Classifier")
    print("K =", K)
    print(Border)

    new_point = {'X': 3, 'Y': 3}

    print("New Point :", new_point)
    print(Border)

    # Calculate distance
    for d in Data:
        d['Distance'] = MarvellousEucDistance(d, new_point)

    print("Distance of all points")
    print(Border)

    for d in Data:
        print(d)

    print(Border)

    # Sort according to distance
    sorted_data = sorted(Data, key=lambda item: item['Distance'])

    print("Sorted Data")
    print(Border)

    for d in sorted_data:
        print(d)

    print(Border)

    # Select nearest K neighbours
    nearest = sorted_data[:K]

    print(f"Nearest {K} members are")
    print(Border)

    for d in nearest:
        print(d)

    print(Border)

    # Voting
    Votes = {}

    for neighbours in nearest:
        Label = neighbours['Label']
        Votes[Label] = Votes.get(Label, 0) + 1

    print("Voting Result")
    print(Border)

    for d in Votes:
        print("Label :", d, "Votes :", Votes[d])

    print(Border)

    # Final Prediction
    iMax = 0
    Name = ""

    for d in Votes:
        if Votes[d] > iMax:
            iMax = Votes[d]
            Name = d

    print("Final Prediction is :", Name)
    print(Border)

    return Name


# Main Function
def main():

    print("\nPrediction Results\n")

    print("K = 1")
    result1 = MarvellousKNNClassifier(1)

    print("\nK = 3")
    result3 = MarvellousKNNClassifier(3)

    print("\nK = 5")
    result5 = MarvellousKNNClassifier(5)

    print("-" * 30)
    print("K = 1 ->", result1)
    print("K = 3 ->", result3)
    print("K = 5 ->", result5)


if __name__ == "__main__":
    main()