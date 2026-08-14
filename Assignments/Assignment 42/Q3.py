import math

# Euclidean Distance Function
def Distance(P1, P2):
    return math.sqrt((P1['Hours'] - P2['Hours'])**2 +
                     (P1['Attendance'] - P2['Attendance'])**2)

# KNN Function
def KNNPredict(Hours, Attendance, K=3):

    # Dataset
    Data = [
        {'Hours': 2, 'Attendance': 60, 'Result': 'Fail'},
        {'Hours': 5, 'Attendance': 80, 'Result': 'Pass'},
        {'Hours': 6, 'Attendance': 85, 'Result': 'Pass'},
        {'Hours': 1, 'Attendance': 50, 'Result': 'Fail'}
    ]

    NewPoint = {'Hours': Hours, 'Attendance': Attendance}

    # Calculate distance
    for d in Data:
        d['Distance'] = Distance(d, NewPoint)

    # Sort by distance
    SortedData = sorted(Data, key=lambda item: item['Distance'])

    # Select nearest K points
    Nearest = SortedData[:K]

    # Voting
    Votes = {}

    for n in Nearest:
        label = n['Result']
        Votes[label] = Votes.get(label, 0) + 1

    # Find maximum votes
    Prediction = max(Votes, key=Votes.get)

    return Prediction


# Main Program
StudyHours = int(input("Enter Study Hours: "))
Attendance = int(input("Enter Attendance: "))

Result = KNNPredict(StudyHours, Attendance)

print("\nPredicted Result:", Result)