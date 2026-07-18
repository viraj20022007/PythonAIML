class BankAccount:

    ROI = 10.5          # Class Variable

    def __init__(self, Name, Amount):
        self.Name = Name
        self.Amount = Amount

    def Display(self):
        print("\nAccount Holder :", self.Name)
        print("Current Balance :", self.Amount)

    def Deposit(self):
        money = float(input("Enter amount to deposit : "))
        self.Amount = self.Amount + money
        print("Amount Deposited Successfully.")

    def Withdraw(self):
        money = float(input("Enter amount to withdraw : "))

        if money <= self.Amount:
            self.Amount = self.Amount - money
            print("Amount Withdrawn Successfully.")
        else:
            print("Insufficient Balance.")

    def CalculateInterest(self):
        Interest = (self.Amount * BankAccount.ROI) / 100
        return Interest


obj1 = BankAccount("Viraj", 10000)

obj1.Display()

obj1.Deposit()
obj1.Display()

obj1.Withdraw()
obj1.Display()

print("Interest :", obj1.CalculateInterest())

print("----------------------------------")

obj2 = BankAccount("Rahul", 5000)

obj2.Display()

obj2.Deposit()
obj2.Withdraw()
obj2.Display()

print("Interest :", obj2.CalculateInterest())