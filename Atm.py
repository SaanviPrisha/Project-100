
class Atm(object):
    def __init__(self, cardNo, pinNo):
        self.cardNo = cardNo
        self.pinNo = pinNo

    def balance(self):
        print("Your balance is 103114")

    def withdrawal(self, withdrawal):

        withdrawedAmount = 103114 - withdrawal
        
        if withdrawal < 103114:
            print(str(withdrawal) + " withdrawed. Amount left " + str(withdrawedAmount))
        elif withdrawal > 103114:
            print("You don't have enough balance. You have 103114 in your account")

    def loan(self, p, t):
        print("Rate of interest is 4.2%")

        finalAmount = (int(p) * 4.2 * int(t))/100

        print("You will have to pay Rs. " + str(finalAmount) + " at the end.")


cardNo = input("input card number: ")
pinNo = input("input pin number: ")

customer = Atm(cardNo, pinNo)

question = int(input("What would you like to do: \n 1. Check  your balance \n 2. Withdraw money \n 3. Take a loan \n Input activity number: "))

if question == 1:
    customer.balance()
    
elif question == 2:

    amount = int(input("Enter desired amount: "))
    customer.withdrawal(amount)

elif question == 3:

    principal = input("Enter amount you wish to loan: ")
    time = input("Enter the time duration you wish to loan it for: ")

    customer.loan(principal, time)

else:
    print("Write a valid number.")
        
