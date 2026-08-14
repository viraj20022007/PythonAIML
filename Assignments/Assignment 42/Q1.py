import numpy as np
import math

def MarvellousEucDistance(P1,P2):
    Ans = math.sqrt((P1['X']-P2['X'])**2 + (P1['Y']-P2['Y'])**2)
    return Ans

def MarvellousKNNClassifier(K=3):
    Border="-"*50

    Data =[
        {'point':'A', 'X': 1, 'Y':2, 'Label' : 'Red'},
        {'point':'B', 'X': 2, 'Y':3, 'Label' : 'Red'},
        {'point':'C', 'X': 3, 'Y':1, 'Label' : 'Blue'},
        {'point':'D', 'X': 5, 'Y':6, 'Label' : 'Blue'},
    ]

    print(Border)
    print("MarvellousKNNClassifier")
    print(Border)


    for i in Data:
        print(i)

    print(Border)   

    new_point={'X' : 3 , 'Y' : 3}

    print("Distance of all points")
    print(Border)

    for d in Data:   #d is new variable for data
        d['Distance'] = MarvellousEucDistance(d,new_point) #store in data in new key 'distance'

    for d in Data:
        print(d)

    print(Border)

    sorted_data = sorted(Data,key=lambda item : item['Distance'])
    print("Sorted Data : ")
    for d in sorted_data:
        print(d)

    print(Border)
 

    nearest = sorted_data[:K]   #first 3 members only (slicing k = 3)

    print(Border)
    print("Nearest 3 members are : ")
    print(Border)

    for d in nearest:
        print(d)

    print(Border)

    #Voting which one is nearest red or blue 
    Votes={}

    for neigbhours in nearest:
        Label = neigbhours['Label']
        Votes[Label] = Votes.get(Label,0)+1

    print(Border)
    print("Voting Result is :")
    print(Border)

    for d in Votes:
        print("Name : ",d,"Number of Votes : ",Votes[d])

    print(Border)

    iMax = 0
    Name = ""

    for d in Votes:
        if(Votes[d] > iMax):
            iMax =Votes[d]
            Name= d

    print("Final Prediction is : ",Name)
    print(Border)
    

def main():
    MarvellousKNNClassifier(5)

if __name__ =="__main__":
    main()