import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


def CheckAccuracy(X, Y, K):

    classifier = KNeighborsClassifier(n_neighbors=K)

    X_train, X_test, Y_train, Y_test = train_test_split(
        X,
        Y,
        test_size=0.5,
        random_state=42
    )

    classifier.fit(X_train, Y_train)

    Y_pred = classifier.predict(X_test)

    Accuracy = accuracy_score(Y_test, Y_pred)

    print("K =", K)
    print("Accuracy =", Accuracy * 100, "%")
    print("-" * 50)


def MarvellousKNNClassifier(K=3):

    Border = "-" * 50

    # ------------------------------------------------
    # Step 1 - Get Data
    # ------------------------------------------------

    print(Border)
    print("Step 1 - Get Data")
    print(Border)

    Data = pd.read_csv("MarvellousInfosystems_PlayPredictor.csv")

    print(Data)

    print(Border)

    # ------------------------------------------------
    # Step 2 - Clean, Prepare and Manipulate Data
    # ------------------------------------------------

    print("Step 2 - Clean, Prepare and Manipulate Data")
    print(Border)

    # Create LabelEncoder objects

    WeatherEncoder = LabelEncoder()
    TemperatureEncoder = LabelEncoder()
    PlayEncoder = LabelEncoder()

    # Convert string values into numerical values

    Data["Wether"] = WeatherEncoder.fit_transform(Data["Wether"])

    Data["Temperature"] = TemperatureEncoder.fit_transform(Data["Temperature"])

    Data["Play"] = PlayEncoder.fit_transform(Data["Play"])

    print(Data)
    print(Border)

    # ------------------------------------------------
    # Separate Independent and Dependent Variables
    # ------------------------------------------------

    X = Data[["Wether", "Temperature"]]

    Y = Data["Play"]

    # ------------------------------------------------
    # Step 3 - Train Data
    # ------------------------------------------------

    print("Step 3 - Train Data")
    print(Border)

    classifier = KNeighborsClassifier(n_neighbors=K)

    # Train using whole dataset
    classifier.fit(X, Y)

    print("Training completed successfully")

    print(Border)

    # ------------------------------------------------
    # Step 4 - Test Data
    # ------------------------------------------------

    print("Step 4 - Test Data")
    print(Border)

    # Take test values from user

    WetherValue = input("Enter Weather (Sunny/Overcast/Rainy): ")

    TemperatureValue = input("Enter Temperature (Hot/Mild/Cool): ")

    # Convert test values into numerical values

    Wether = WeatherEncoder.transform([WetherValue])[0]

    Temperature = TemperatureEncoder.transform([TemperatureValue])[0]

    # Create test data

    TestData =[[Wether, Temperature]]

    # Prediction

    Prediction = classifier.predict(TestData)

    # Convert numerical prediction back to original label

    Result = PlayEncoder.inverse_transform(Prediction)

    print(Border)
    print("Test Data")
    print(Border)

    print("Wether :", WetherValue)
    print("Temperature :", TemperatureValue)
    print("Prediction :", Result[0])

    print(Border)

    # ------------------------------------------------
    # Step 5 - Calculate Accuracy
    # ------------------------------------------------

    print("Step 5 - Calculate Accuracy")
    print(Border)

    print("Checking Accuracy for different values of K")
    print(Border)

    for i in range(1, 6):

        CheckAccuracy(
            X,
            Y,
            i
        )

    print(Border)


def main():

    # K = 3 as given in the question

    MarvellousKNNClassifier(3)


if __name__ == "__main__":

    main()